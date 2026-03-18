from django.contrib import admin

from .forms import *
from .models import *


admin.site.site_header = "Shymkent College әкімші панелі"
admin.site.site_title = "Shymkent College Admin"
admin.site.index_title = "Контент пен бөлімдерді жылдам басқарыңыз"


class BaseAdmin(admin.ModelAdmin):
    list_per_page = 20
    search_fields = ("id",)
    list_filter = ("lang",)
    ordering = ("-id",)


class OrderedContentAdmin(BaseAdmin):
    list_display = ("id", "__str__", "lang", "status", "rating")
    list_editable = ("status", "rating")
    list_filter = ("lang", "status", "is_main")
    ordering = ("rating", "-id")


class LinkContentAdmin(OrderedContentAdmin):
    readonly_fields = ("asset_preview",)

    @admin.display(description="Превью")
    def asset_preview(self, obj):
        asset_url = getattr(obj, "photo", "") or getattr(obj, "logo", "")
        if not asset_url:
            return "Ссылка на изображение не добавлена"
        return (
            f'<a href="{asset_url}" target="_blank" rel="noopener">Открыть файл</a><br>'
            f'<img src="{asset_url}" alt="preview" '
            'style="margin-top:12px;max-width:220px;border-radius:16px;box-shadow:0 10px 30px rgba(15,23,42,.18);" />'
        )

    def _editable_columns(self):
        model_fields = {field.name for field in self.model._meta.fields}
        return tuple(name for name in ("is_main", "status", "rating") if name in model_fields)

    def get_list_display(self, request):
        model_fields = {field.name for field in self.model._meta.fields}
        columns = ["id", "__str__", "lang"]
        for name in ("is_main", "status", "rating"):
            if name in model_fields:
                columns.append(name)
        return tuple(columns)

    def get_list_editable(self, request):
        return self._editable_columns()

    def get_list_filter(self, request):
        model_fields = {field.name for field in self.model._meta.fields}
        filters = ["lang"]
        for name in ("status", "is_main"):
            if name in model_fields:
                filters.append(name)
        return tuple(filters)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields
        return tuple()

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        photo_field = form.base_fields.get("photo") or form.base_fields.get("logo")
        if photo_field:
            photo_field.widget.attrs.update(
                {
                    "placeholder": "https://drive.google.com/... немесе CDN сілтемесі",
                    "style": "max-width: 38rem;",
                }
            )
        return form

    class Media:
        css = {"all": ("admin/css/custom_admin.css",)}


@admin.register(Languages)
class LanguagesAdmin(BaseAdmin):
    list_display = ("id", "title", "code", "extra_title")
    search_fields = ("title", "code", "extra_title")
    list_filter = tuple()


@admin.register(TransValue)
class TransValueAdmin(BaseAdmin):
    list_display = ("id", "code", "title", "lang")
    search_fields = ("code", "title", "lang__title", "lang__code")


@admin.register(Information)
class InformationAdmin(LinkContentAdmin):
    form = InformationAdminForm
    list_display = ("id", "address", "email_info", "phone_info1", "lang", "status")
    list_editable = ("status",)
    search_fields = ("address", "email_info", "phone_info1", "phone_info2")
    readonly_fields = ("asset_preview",)


@admin.register(Slider)
class SliderAdmin(LinkContentAdmin):
    form = SliderAdminForm
    list_display = ("id", "main_title", "lang", "status", "rating")
    search_fields = ("main_title", "mini_description")


@admin.register(Icon)
class IconAdmin(OrderedContentAdmin):
    list_display = ("id", "title", "name", "lang", "status", "rating")
    search_fields = ("title", "name", "description", "mini_description")


@admin.register(About)
class AboutAdmin(OrderedContentAdmin):
    list_display = ("id", "name", "count", "lang", "status", "rating")
    search_fields = ("name", "logo")


@admin.register(Specialty)
class SpecialtyAdmin(LinkContentAdmin):
    form = SpecialtyAdminForm
    list_display = ("id", "title", "lang", "is_main", "status", "rating")
    search_fields = ("title", "main_title", "description", "mini_description")


@admin.register(Comentary)
class ComentaryAdmin(LinkContentAdmin):
    form = ComentaryAdminForm
    list_display = ("id", "last_name", "first_name", "position", "lang", "is_main", "status")
    list_editable = ("is_main", "status")
    search_fields = ("last_name", "first_name", "position", "mini_description")


@admin.register(News)
class NewsAdmin(LinkContentAdmin):
    form = NewsAdminForm
    list_display = ("id", "title", "name", "date", "lang", "is_main", "status", "rating")
    list_editable = ("is_main", "status", "rating")
    search_fields = ("title", "name", "date", "mini_description", "description")


@admin.register(Karta)
class KartaAdmin(BaseAdmin):
    list_display = ("id", "main_title", "address_link", "lang")
    search_fields = ("main_title", "mini_description", "address_link")


@admin.register(Register)
class RegisterAdmin(BaseAdmin):
    list_display = ("id", "last_name", "first_name", "phone", "lang")
    search_fields = ("last_name", "first_name", "phone", "message")
    ordering = ("-id",)


# Photo/link based modules.
_asset_admin_map = {
    Galery: GaleryAdminForm,
    Teacher: TeacherAdminForm,
    Baza: BazaAdminForm,
    Qabyldau: QabyldauAdminForm,
    Biliktilik: BiliktilikAdminForm,
    KollejTarihi: KollejTarihiAdminForm,
    License: LicenseAdminForm,
    Tulekter: TulekterAdminForm,
    Acredatsiya: AcredatsiyaAdminForm,
    Qurylym: QurylymAdminForm,
    Missiya: MissiyaAdminForm,
    OquAdisteme: OquAdistemeAdminForm,
    Jemqorlyq: JemqorlyqAdminForm,
    AdistemelikKabinet: AdistemelikKabinetAdminForm,
    JasMaman: JasMamanAdminForm,
    Birlestikter: BirlestikterAdminForm,
    Jetistikter: JetistikterAdminForm,
    StudenttikKenes: StudenttikKenesAdminForm,
    Bitirushiler: BitirushilerAdminForm,
    StudenttikOmir: StudenttikOmirAdminForm,
    Qashyqtyq: QashyqtyqAdminForm,
    OquUrdisi: OquUrdisiAdminForm,
    Oqu: OquAdminForm,
    SabaqKeste: SabaqKesteAdminForm,
    StudentJetistik: StudentJetistikAdminForm,
    Aqparat: AqparatAdminForm,
    JumysqaOrnalasu: JumysqaOrnalasuAdminForm,
    Seriktester: SeriktesterAdminForm,
    Saualnama: SaualnamaAdminForm,
    Talapker: TalapkerAdminForm,
    KenesJospary: KenesJosparyAdminForm,
}

for model, form in _asset_admin_map.items():
    admin_class = type(
        f"{model.__name__}Admin",
        (LinkContentAdmin,),
        {
            "form": form,
            "search_fields": ("title", "name", "short_description", "link"),
        },
    )
    admin.site.register(model, admin_class)


@admin.register(Video)
class VideoAdmin(OrderedContentAdmin):
    list_display = ("id", "title", "vide_link", "lang", "status", "rating")
    search_fields = ("title", "description", "vide_link", "link")
