from django.contrib import admin

from .forms import *
from .models import *


@admin.register(Languages)
class LanguagesAdmin(admin.ModelAdmin):
    pass


@admin.register(TransValue)
class TransValueAdmin(admin.ModelAdmin):
    pass


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    form = InformationAdminForm


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    form = SliderAdminForm


@admin.register(Icon)
class IconAdmin(admin.ModelAdmin):
    pass


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    form = SpecialtyAdminForm


@admin.register(Comentary)
class ComentaryAdmin(admin.ModelAdmin):
    form = ComentaryAdminForm


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm


@admin.register(Karta)
class KartaAdmin(admin.ModelAdmin):
    pass


@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    pass


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
    admin_class = type(f"{model.__name__}Admin", (admin.ModelAdmin,), {"form": form})
    admin.site.register(model, admin_class)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass
