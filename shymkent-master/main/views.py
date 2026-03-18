from django.http import JsonResponse
from django.shortcuts import render
from main.models import Information, Slider, Icon, About, Specialty, Comentary, News, Register, Galery
from main.models import Teacher, Baza, Qabyldau, Biliktilik, Video, KollejTarihi, License, Acredatsiya, Karta
from main.models import Qurylym, OquAdisteme, AdistemelikKabinet, JasMaman, Birlestikter, Jetistikter, Qashyqtyq
from main.models import OquUrdisi, SabaqKeste, StudentJetistik, Aqparat, JumysqaOrnalasu, Seriktester, Saualnama
import math
from main.models import Languages, TransValue, Missiya, Jemqorlyq, KenesJospary, StudenttikKenes, Bitirushiler
from main.models import StudenttikOmir, Talapker, Oqu, Tulekter
# Create your views here.

def indexHandler(request):
    if request.method == 'GET':
        if request.GET.get('lang', ''):
            request.session['lang'] = request.GET.get('lang', '')

        current_lang = request.session.get('lang', 'ru')
        langs = Languages.objects.all()
        trans_values = TransValue.objects.filter(lang__code = current_lang)

        informations = Information.objects.filter(lang__code=current_lang)
        sliders = Slider.objects.filter(status=0).filter(lang__code=current_lang).order_by('-rating')
        icons = Icon.objects.filter(status=0).filter(lang__code=current_lang).order_by('-rating')
        abouts = About.objects.filter(status=0).filter(lang__code=current_lang).order_by('-rating')
        specialtys = Specialty.objects.filter(status=0).filter(lang__code=current_lang).order_by('-rating').filter(is_main=True)
        comentarys = Comentary.objects.filter(status=0).filter(lang__code=current_lang).order_by('-rating').filter(is_main=True)
        news = News.objects.filter(status=0).filter(lang__code=current_lang).order_by('-rating').filter(is_main=True)[:3]
        galerys = Galery.objects.filter(status=0).filter(lang__code=current_lang).order_by('-rating').filter(is_main=True)
        kartas = Karta.objects.filter(lang__code=current_lang)


        return render(request, 'index.html', {
            'langs':langs,
            'trans_values': trans_values,
            'informations': informations,
            'sliders': sliders,
            'icons': icons,
            'abouts': abouts,
            'specialtys': specialtys,
            'comentarys': comentarys,
            'news': news,
            'galerys': galerys,
            'kartas': kartas
        })


    else:
        r = Register()
        last_name = request.POST.get('last_name', '')
        first_name = request.POST.get('first_name', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')


        r.last_name = last_name
        r.phone = phone
        r.first_name = first_name
        r.message = message
        r.save()

        return JsonResponse({'success': True, 'errorMsg': '', '_success': True})



def NewsDetailHandler(request, news_id):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)


    news_items = News.objects.get(id=int(news_id))

    informations = Information.objects.filter(lang__code=current_lang)
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    news = News.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    return render(request, 'news-detail.html', {
        'news': news,
        'news_items': news_items,
        'informations': informations,
        'galerys': galerys,
        'langs': langs,
        'trans_values': trans_values
    })



def SpecialtyDetailHandler(request, specialty_id):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)


    specialty_items = Specialty.objects.get(id=int(specialty_id))

    informations = Information.objects.filter(lang__code=current_lang)
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    specialtys = Specialty.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    return render(request, 'specialty-detail.html', {
        'specialty_items': specialty_items,
        'informations': informations,
        'galerys': galerys,
        'specialtys': specialtys,
        'langs': langs,
        'trans_values': trans_values
    })


def CourseHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)


    informations = Information.objects.filter(lang__code=current_lang)
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    specialtys = Specialty.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    return render(request, 'courses.html', {
        'informations': informations,
        'galerys': galerys,
        'specialtys': specialtys,
        'langs': langs,
        'trans_values': trans_values
    })


def TeacherHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang)
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    teachers = Teacher.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    return render(request, 'teacher.html', {
        'informations': informations,
        'galerys': galerys,
        'teachers': teachers,
        'langs': langs,
        'trans_values': trans_values
    })


def AboutHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    about = KollejTarihi.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)

    return render(request, 'about.html', {
        'informations': informations,
        'galerys': galerys,
        'about': about,
        'langs': langs,
        'trans_values': trans_values
    })



def BazaHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    baza = Baza.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)

    return render(request, 'baza.html', {
        'informations': informations,
        'galerys': galerys,
        'baza': baza,
        'langs': langs,
        'trans_values': trans_values
    })



def VideoHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    video = Video.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)

    return render(request, 'video.html', {
        'informations': informations,
        'galerys': galerys,
        'video': video,
        'langs': langs,
        'trans_values': trans_values
    })


def QabyldauHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    qabyldau = Qabyldau.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)

    return render(request, 'qabyldau.html', {
        'informations': informations,
        'galerys': galerys,
        'qabyldau': qabyldau,
        'langs': langs,
        'trans_values': trans_values
    })




def BiliktilikHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    biliktilik = Biliktilik.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)

    return render(request, 'biliktilik.html', {
        'informations': informations,
        'galerys': galerys,
        'biliktilik': biliktilik,
        'langs': langs,
        'trans_values': trans_values
    })



def LicenseHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    license = License.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)

    return render(request, 'license.html', {
        'informations': informations,
        'galerys': galerys,
        'license': license,
        'langs': langs,
        'trans_values': trans_values
    })


def AcredatsiyaHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    acredatsiya = Acredatsiya.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)

    return render(request, 'acredatsiya.html', {
        'informations': informations,
        'galerys': galerys,
        'langs': langs,
        'trans_values': trans_values,
        'acredatsiya': acredatsiya
    })


def QurylymHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)


    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    qurylym = Qurylym.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)

    return render(request, 'qurylym.html', {
        'informations': informations,
        'galerys': galerys,
        'qurylym': qurylym,
        'langs': langs,
        'trans_values': trans_values
    })

def MissiyaHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)


    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    missiya = Missiya.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)

    return render(request, 'qurylym.html', {
        'informations': informations,
        'galerys': galerys,
        'missiya': missiya,
        'langs': langs,
        'trans_values': trans_values
    })




def OquAdistemeHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    adisteme = OquAdisteme.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)

    return render(request, 'oqu-adisteme.html', {
        'informations': informations,
        'galerys': galerys,
        'adisteme': adisteme,
        'langs': langs,
        'trans_values': trans_values
    })

def JemqorlyqHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    jemqorlyq = Jemqorlyq.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)

    return render(request, 'oqu-adisteme.html', {
        'informations': informations,
        'galerys': galerys,
        'jemqorlyq': jemqorlyq,
        'langs': langs,
        'trans_values': trans_values
    })


def AdistemelikKabinetHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    kabinet = AdistemelikKabinet.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)

    return render(request, 'adisteme-kabineti.html', {
        'informations': informations,
        'galerys': galerys,
        'kabinet': kabinet,
        'langs': langs,
        'trans_values': trans_values
    })


def JasMamanHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    maman = JasMaman.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)

    return render(request, 'jas-maman.html', {
        'informations': informations,
        'galerys': galerys,
        'maman': maman,
        'langs': langs,
        'trans_values': trans_values
    })


def BirlestikHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang).filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    birlestik = Birlestikter.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)

    return render(request, 'birlestik.html', {
        'informations': informations,
        'galerys': galerys,
        'birlestik': birlestik,
        'langs': langs,
        'trans_values': trans_values
    })

def KenesJosparyHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang).filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    kenes = KenesJospary.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)

    return render(request, 'birlestik.html', {
        'informations': informations,
        'galerys': galerys,
        'kenes': kenes,
        'langs': langs,
        'trans_values': trans_values
    })


def JetistikHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    jetistik = Jetistikter.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)


    return render(request, 'jetistik.html', {
        'informations': informations,
        'galerys': galerys,
        'jetistik': jetistik,
        'langs': langs,
        'trans_values': trans_values
    })


def OquHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    oqu = Oqu.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)


    return render(request, 'oqu.html', {
        'informations': informations,
        'galerys': galerys,
        'oqu': oqu,
        'langs': langs,
        'trans_values': trans_values
    })


def OquUrdisiHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    oqu = OquUrdisi.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)


    return render(request, 'oqu-urdisi.html', {
        'informations': informations,
        'galerys': galerys,
        'oqu': oqu,
        'langs': langs,
        'trans_values': trans_values
    })


def KesteHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    keste = SabaqKeste.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)


    return render(request, 'keste.html', {
        'informations': informations,
        'galerys': galerys,
        'keste': keste,
        'langs': langs,
        'trans_values': trans_values
    })


def StudenttikKenesHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    student = StudenttikKenes.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)


    return render(request, 'studenttik-kenes.html', {
        'informations': informations,
        'galerys': galerys,
        'student': student,
        'langs': langs,
        'trans_values': trans_values
    })




def StudentHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    jetistik = StudentJetistik.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)


    return render(request, 'student-jetistikteri.html', {
        'informations': informations,
        'jetistik': jetistik,
        'galerys': galerys,
        'langs': langs,
        'trans_values': trans_values
    })



def AqparatHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    aqparat = Aqparat.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)
    news = News.objects.filter(status=0).filter(lang__code=current_lang).order_by('-rating').filter(is_main=True)

    return render(request, 'aqparat.html', {
        'informations': informations,
        'galerys': galerys,
        'langs': langs,
        'news': news,
        'trans_values': trans_values
    })


def JumysqaOrnalasuHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    jumys = JumysqaOrnalasu.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)


    return render(request, 'jumysqa-ornalasu.html', {
        'informations': informations,
        'galerys': galerys,
        'jumys': jumys,
        'langs': langs,
        'trans_values': trans_values
    })


def PartnerHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    partner = Seriktester.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)


    return render(request, 'partner.html', {
        'informations': informations,
        'galerys': galerys,
        'langs': langs,
        'partner': partner,
        'trans_values': trans_values
    })


def SaualnamaHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    saualnama = Saualnama.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)


    return render(request, 'saualnama.html', {
        'informations': informations,
        'galerys': galerys,
        'saualnama': saualnama,
        'langs': langs,
        'trans_values': trans_values
    })


def BitirushilerHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    bitirushiler = Bitirushiler.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)


    return render(request, 'bitirushiler.html', {
        'informations': informations,
        'galerys': galerys,
        'bitirushiler': bitirushiler,
        'langs': langs,
        'trans_values': trans_values
    })


def StudenttikOmirHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    omir = StudenttikOmir.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)


    return render(request, 'studenttik-omir.html', {
        'informations': informations,
        'galerys': galerys,
        'omir': omir,
        'langs': langs,
        'trans_values': trans_values
    })


def TalapkerHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    talapker = Talapker.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)


    return render(request, 'talapker.html', {
        'informations': informations,
        'galerys': galerys,
        'talapker': talapker,
        'langs': langs,
        'trans_values': trans_values,
        'talapker': talapker
    })


def TulekterHandler(request):
    current_lang = request.session.get('lang', 'ru')
    langs = Languages.objects.all()
    trans_values = TransValue.objects.filter(lang__code=current_lang)

    informations = Information.objects.filter(lang__code=current_lang)

    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True).filter(lang__code=current_lang)
    tulekter = Tulekter.objects.filter(status=0).order_by('-rating').filter(lang__code=current_lang)


    return render(request, 'tulekter.html', {
        'informations': informations,
        'galerys': galerys,
        'langs': langs,
        'trans_values': trans_values,
        'tulekter': tulekter
    })