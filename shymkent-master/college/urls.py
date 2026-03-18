from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from college import settings

from main.views import (
    indexHandler, NewsDetailHandler, SpecialtyDetailHandler, CourseHandler, TeacherHandler,
    AboutHandler, BazaHandler, VideoHandler, QabyldauHandler, BiliktilikHandler, LicenseHandler,
    AcredatsiyaHandler, QurylymHandler, OquAdistemeHandler, AdistemelikKabinetHandler,
    JasMamanHandler, BirlestikHandler, JetistikHandler, OquHandler, OquUrdisiHandler, KesteHandler,
    StudentHandler, AqparatHandler, JumysqaOrnalasuHandler, PartnerHandler, SaualnamaHandler,
    MissiyaHandler, JemqorlyqHandler, KenesJosparyHandler, StudenttikKenesHandler, BitirushilerHandler,
    StudenttikOmirHandler, TalapkerHandler, TulekterHandler
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('news/<int:news_id>/', NewsDetailHandler),
    path('specialty/<int:specialty_id>/', SpecialtyDetailHandler),
    path('courses/', CourseHandler),
    path('about/', AboutHandler),
    path('teachers/', TeacherHandler),
    path('baza/', BazaHandler),
    path('video/', VideoHandler),
    path('qabyldau/', QabyldauHandler),
    path('biliktilik/', BiliktilikHandler),
    path('license/', LicenseHandler),
    path('acredatsiya/', AcredatsiyaHandler),
    path('missiya/', MissiyaHandler),
    path('oqu-adisteme/', OquAdistemeHandler),
    path('jemqorlyq/', JemqorlyqHandler),
    path('adisteme-kabineti/', AdistemelikKabinetHandler),
    path('jas-maman/', JasMamanHandler),
    path('birlestik/', BirlestikHandler),
    path('kenes-jospary/', KenesJosparyHandler),
    path('jetistik/', JetistikHandler),
    path('oqu/', OquHandler),
    path('jastar/', OquUrdisiHandler),
    path('studenttik-kenes/', StudenttikKenesHandler),
    path('keste/', KesteHandler),
    path('student-jetistigi/', StudentHandler),
    path('aqparat/', AqparatHandler),
    path('jumysqa-ornalasu/', JumysqaOrnalasuHandler),
    path('partner/', PartnerHandler),
    path('ata-analar/', SaualnamaHandler),
    path('bitirushiler/', BitirushilerHandler),
    path('studenttik-omir/', StudenttikOmirHandler),
    path('talapker/', TalapkerHandler),
    path('tulekter/', TulekterHandler),

    # ✅ исправлено (url → re_path)
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
    }),

    path('', indexHandler),
]
