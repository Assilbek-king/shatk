import base64
import json
import mimetypes
import os
import time
import uuid
from dataclasses import dataclass
from typing import Optional
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from django.core.exceptions import ImproperlyConfigured

GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"
GOOGLE_DRIVE_UPLOAD_URL = "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart"
GOOGLE_DRIVE_PERMISSION_URL = "https://www.googleapis.com/drive/v3/files/{file_id}/permissions"
GOOGLE_DRIVE_FILE_URL = "https://drive.google.com/uc?id={file_id}"


@dataclass
class UploadedDriveFile:
    file_id: str
    web_url: str


class GoogleDriveUploader:
    def __init__(self):
        self.credentials = self._load_credentials()
        self.folder_id = os.getenv("GOOGLE_DRIVE_FOLDER_ID", "").strip()
        self.share_with_anyone = os.getenv("GOOGLE_DRIVE_PUBLIC", "1").strip() != "0"

    def _load_credentials(self):
        raw = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON", "").strip()
        path = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE", "").strip()
        if raw:
            return json.loads(raw)
        if path:
            with open(path, "r", encoding="utf-8") as fh:
                return json.load(fh)
        raise ImproperlyConfigured(
            "Google Drive upload is not configured. Set GOOGLE_SERVICE_ACCOUNT_JSON or GOOGLE_SERVICE_ACCOUNT_FILE."
        )

    def _b64url(self, data: bytes) -> str:
        return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")

    def _token(self) -> str:
        header = self._b64url(json.dumps({"alg": "RS256", "typ": "JWT"}).encode())
        now = int(time.time())
        payload = self._b64url(
            json.dumps(
                {
                    "iss": self.credentials["client_email"],
                    "scope": "https://www.googleapis.com/auth/drive.file",
                    "aud": GOOGLE_TOKEN_URL,
                    "exp": now + 3600,
                    "iat": now,
                }
            ).encode()
        )
        unsigned = f"{header}.{payload}".encode()

        try:
            from cryptography.hazmat.primitives import hashes, serialization
            from cryptography.hazmat.primitives.asymmetric import padding
        except Exception as exc:
            raise ImproperlyConfigured(
                "The 'cryptography' package is required for Google Drive uploads. Install it in the project environment."
            ) from exc

        private_key = serialization.load_pem_private_key(
            self.credentials["private_key"].encode(), password=None
        )
        signature = private_key.sign(unsigned, padding.PKCS1v15(), hashes.SHA256())
        assertion = f"{header}.{payload}.{self._b64url(signature)}"
        body = urlencode(
            {
                "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
                "assertion": assertion,
            }
        ).encode()
        request = Request(GOOGLE_TOKEN_URL, data=body, method="POST")
        request.add_header("Content-Type", "application/x-www-form-urlencoded")
        with urlopen(request) as response:
            data = json.loads(response.read().decode())
        return data["access_token"]

    def upload(self, django_file, filename: Optional[str] = None) -> UploadedDriveFile:
        token = self._token()
        filename = filename or django_file.name or f"upload-{uuid.uuid4().hex}"
        mime = getattr(django_file, "content_type", None) or mimetypes.guess_type(filename)[0] or "application/octet-stream"
        metadata = {"name": filename}
        if self.folder_id:
            metadata["parents"] = [self.folder_id]
        boundary = f"===============_{uuid.uuid4().hex}"
        body = b"".join(
            [
                f"--{boundary}\r\n".encode(),
                b"Content-Type: application/json; charset=UTF-8\r\n\r\n",
                json.dumps(metadata).encode(),
                b"\r\n",
                f"--{boundary}\r\n".encode(),
                f"Content-Type: {mime}\r\n\r\n".encode(),
                django_file.read(),
                b"\r\n",
                f"--{boundary}--\r\n".encode(),
            ]
        )
        request = Request(GOOGLE_DRIVE_UPLOAD_URL, data=body, method="POST")
        request.add_header("Authorization", f"Bearer {token}")
        request.add_header("Content-Type", f"multipart/related; boundary={boundary}")
        try:
            with urlopen(request) as response:
                data = json.loads(response.read().decode())
        except HTTPError as exc:
            detail = exc.read().decode(errors="ignore")
            raise ImproperlyConfigured(f"Google Drive upload failed: {detail}") from exc

        file_id = data["id"]
        if self.share_with_anyone:
            perm_req = Request(
                GOOGLE_DRIVE_PERMISSION_URL.format(file_id=file_id),
                data=json.dumps({"role": "reader", "type": "anyone"}).encode(),
                method="POST",
            )
            perm_req.add_header("Authorization", f"Bearer {token}")
            perm_req.add_header("Content-Type", "application/json")
            with urlopen(perm_req):
                pass
        return UploadedDriveFile(file_id=file_id, web_url=GOOGLE_DRIVE_FILE_URL.format(file_id=file_id))
