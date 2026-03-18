"""college URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.static import serve
from college import settings
from main.views import indexHandler, NewsDetailHandler, SpecialtyDetailHandler, CourseHandler,  TeacherHandler
from main.views import AboutHandler, BazaHandler, VideoHandler, QabyldauHandler, BiliktilikHandler, LicenseHandler
from main.views import AcredatsiyaHandler, QurylymHandler, OquAdistemeHandler, AdistemelikKabinetHandler
from main.views import JasMamanHandler, BirlestikHandler, JetistikHandler, OquHandler, OquUrdisiHandler, KesteHandler
from main.views import StudentHandler, AqparatHandler, JumysqaOrnalasuHandler,  PartnerHandler, SaualnamaHandler
from main.views import MissiyaHandler, JemqorlyqHandler, KenesJosparyHandler, StudenttikKenesHandler, BitirushilerHandler
from main.views import StudenttikOmirHandler, TalapkerHandler, OquHandler, TulekterHandler


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


    url(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
    }),


    path('', indexHandler),
]
