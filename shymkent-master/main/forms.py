from django import forms
from django.core.exceptions import ImproperlyConfigured, ValidationError

from .google_drive import GoogleDriveUploader
from .models import (
    Information, Slider, Specialty, Comentary, News,
    Teacher, Galery, Baza, Qabyldau, Biliktilik,
    KollejTarihi, License, Tulekter, Acredatsiya, Qurylym,
    Missiya, OquAdisteme, Oqu, Jemqorlyq, AdistemelikKabinet,
    JasMaman, Birlestikter, KenesJospary, Jetistikter,
    Qashyqtyq, OquUrdisi, SabaqKeste, StudentJetistik,
    StudenttikKenes, Aqparat, JumysqaOrnalasu, Seriktester,
    Saualnama, Bitirushiler, StudenttikOmir, Talapker
)


class GoogleDriveAdminForm(forms.ModelForm):
    upload_file = forms.FileField(
        required=False,
        help_text="Можно выбрать файл здесь — он автоматически загрузится в Google Drive, а в модель сохранится ссылка.",
    )
    asset_field_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.asset_field_name and self.asset_field_name in self.fields:
            self.fields[self.asset_field_name].help_text = (
                "Вставьте публичную ссылку Google Drive/другого CDN или загрузите файл через поле ниже."
            )

    def clean(self):
        cleaned_data = super().clean()
        upload = cleaned_data.get("upload_file")

        if upload and self.asset_field_name:
            try:
                uploaded = GoogleDriveUploader().upload(upload, filename=upload.name)
                cleaned_data[self.asset_field_name] = uploaded.web_url
            except ImproperlyConfigured as exc:
                raise ValidationError(str(exc))

        return cleaned_data


# ======= Обычные формы =======

class InformationAdminForm(GoogleDriveAdminForm):
    asset_field_name = "logo"

    class Meta:
        model = Information
        fields = "__all__"


class SliderAdminForm(GoogleDriveAdminForm):
    asset_field_name = "photo"

    class Meta:
        model = Slider
        fields = "__all__"


class SpecialtyAdminForm(GoogleDriveAdminForm):
    asset_field_name = "photo"

    class Meta:
        model = Specialty
        fields = "__all__"


class ComentaryAdminForm(GoogleDriveAdminForm):
    asset_field_name = "photo"

    class Meta:
        model = Comentary
        fields = "__all__"


# ======= News (3 файла) =======

class NewsAdminForm(GoogleDriveAdminForm):
    upload_file_2 = forms.FileField(required=False)
    upload_file_3 = forms.FileField(required=False)

    class Meta:
        model = News
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name in ("photo1", "photo2", "photo3"):
            if name in self.fields:
                self.fields[name].help_text = (
                    "Вставьте ссылку на изображение или загрузите файл ниже в Google Drive."
                )

        self.fields["upload_file"].label = "Загрузить фото 1"
        self.fields["upload_file_2"].label = "Загрузить фото 2"
        self.fields["upload_file_3"].label = "Загрузить фото 3"

    def clean(self):
        cleaned_data = super().clean()
        uploader = None

        for field_name, upload_name in (
            ("photo1", "upload_file"),
            ("photo2", "upload_file_2"),
            ("photo3", "upload_file_3"),
        ):
            upload = cleaned_data.get(upload_name)

            if upload:
                try:
                    uploader = uploader or GoogleDriveUploader()
                    cleaned_data[field_name] = uploader.upload(
                        upload, filename=upload.name
                    ).web_url
                except ImproperlyConfigured as exc:
                    raise ValidationError(str(exc))

        return cleaned_data


# ======= Генератор форм (ИСПРАВЛЕННЫЙ) =======

def build_link_asset_form(model, asset_field_name="photo"):
    _model = model  # ✅ фикс области видимости

    class _LinkAssetAdminForm(GoogleDriveAdminForm):
        class Meta:
            model = _model
            fields = "__all__"

    _LinkAssetAdminForm.asset_field_name = asset_field_name
    _LinkAssetAdminForm.__name__ = f"{model.__name__}AdminForm"

    return _LinkAssetAdminForm


# ======= Автогенерация форм =======

TeacherAdminForm = build_link_asset_form(Teacher)
GaleryAdminForm = build_link_asset_form(Galery)
BazaAdminForm = build_link_asset_form(Baza)
QabyldauAdminForm = build_link_asset_form(Qabyldau)
BiliktilikAdminForm = build_link_asset_form(Biliktilik)
KollejTarihiAdminForm = build_link_asset_form(KollejTarihi)
LicenseAdminForm = build_link_asset_form(License)
TulekterAdminForm = build_link_asset_form(Tulekter)
AcredatsiyaAdminForm = build_link_asset_form(Acredatsiya)
QurylymAdminForm = build_link_asset_form(Qurylym)
MissiyaAdminForm = build_link_asset_form(Missiya)
OquAdistemeAdminForm = build_link_asset_form(OquAdisteme)
OquAdminForm = build_link_asset_form(Oqu)
JemqorlyqAdminForm = build_link_asset_form(Jemqorlyq)
AdistemelikKabinetAdminForm = build_link_asset_form(AdistemelikKabinet)
JasMamanAdminForm = build_link_asset_form(JasMaman)
BirlestikterAdminForm = build_link_asset_form(Birlestikter)
KenesJosparyAdminForm = build_link_asset_form(KenesJospary)
JetistikterAdminForm = build_link_asset_form(Jetistikter)
QashyqtyqAdminForm = build_link_asset_form(Qashyqtyq)
OquUrdisiAdminForm = build_link_asset_form(OquUrdisi)
SabaqKesteAdminForm = build_link_asset_form(SabaqKeste)
StudentJetistikAdminForm = build_link_asset_form(StudentJetistik)
StudenttikKenesAdminForm = build_link_asset_form(StudenttikKenes)
AqparatAdminForm = build_link_asset_form(Aqparat)
JumysqaOrnalasuAdminForm = build_link_asset_form(JumysqaOrnalasu)
SeriktesterAdminForm = build_link_asset_form(Seriktester)
SaualnamaAdminForm = build_link_asset_form(Saualnama)
BitirushilerAdminForm = build_link_asset_form(Bitirushiler)
StudenttikOmirAdminForm = build_link_asset_form(StudenttikOmir)
TalapkerAdminForm = build_link_asset_form(Talapker)
