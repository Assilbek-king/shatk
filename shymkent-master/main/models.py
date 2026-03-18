from django.db import models

class Languages(models.Model):
    title = models.TextField(blank=True)
    code = models.TextField(blank=True)
    extra_title = models.TextField(blank=True)
    def __str__(self):
        return self.title

class TransValue(models.Model):
    code = models.TextField(blank=True)
    title = models.TextField(blank=True)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)

    def __str__(self):
        return self.title + ' ' + self.code
# Create your models here.
class Information(models.Model):
    knopka = models.TextField(blank=True)
    knopka_link = models.TextField(blank=True)
    address = models.TextField(blank=True)
    address_name = models.TextField(blank=True)
    facebook_info = models.TextField(blank=True)
    instagram_info = models.TextField(blank=True)
    whatsapp_info = models.TextField(blank=True)
    youtube_info = models.TextField(blank=True)
    email_info = models.TextField(blank=True)
    email_info_link = models.TextField(blank=True)
    phone_info1 = models.TextField(blank=True)
    phone_info1_link = models.TextField(blank=True)
    phone_info2 = models.TextField(blank=True)
    phone_info2_link = models.TextField(blank=True)
    partner_info1 = models.TextField(blank=True)
    partner_info1_link = models.TextField(blank=True)
    partner_info2 = models.TextField(blank=True)
    partner_info2_link = models.TextField(blank=True)
    partner_info3 = models.TextField(blank=True)
    partner_info3_link = models.TextField(blank=True)
    menu_info1 = models.TextField(blank=True)
    menu_info1_link = models.TextField(blank=True)
    menu_info2 = models.TextField(blank=True)
    menu_info2_link = models.TextField(blank=True)
    menu_info3 = models.TextField(blank=True)
    menu_info3_link = models.TextField(blank=True)
    status = models.IntegerField(default=0, blank=True)
    logo = models.ImageField(upload_to='upload', blank=True)
    lang = models.ForeignKey(Languages,  on_delete=models.CASCADE, default=1, blank=True)

    def __str__(self):
        return self.address

class Slider(models.Model):
    main_title = models.TextField(blank=True)
    photo = models.ImageField(upload_to='upload')
    mini_description = models.CharField(max_length=500, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)


    def __str__(self):
        return self.main_title


class Icon(models.Model):
    main_title = models.TextField(blank=True)
    description = models.CharField(max_length=500, blank=True)
    #icon = models.ImageField(upload_to='upload', blank=True)
    name = models.TextField(blank=True)
    title = models.TextField(blank=True)
    mini_description = models.CharField(max_length=500, blank=True)
    link = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)

    def __str__(self):
        return self.title

class About(models.Model):
    # icon = models.ImageField(upload_to='upload', blank=True)
    logo = models.TextField(blank=True)
    name = models.TextField(blank=True)
    count = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)

    def __str__(self):
        return self.name


class Specialty(models.Model):
    main_title = models.TextField(blank=True)
    mini_description = models.CharField(max_length=500, blank=True)
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    is_main = models.BooleanField(default=0, blank=True)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    link = models.TextField(blank=True)


    def __str__(self):
        return self.title

class Comentary(models.Model):
    photo = models.ImageField(upload_to='upload')
    last_name = models.CharField(max_length=300)
    first_name = models.CharField(max_length=300)
    position = models.CharField(max_length=300)
    mini_description = models.CharField(max_length=500, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    is_main = models.BooleanField(default=0, blank=True)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)


    def __str__(self):
        return self.last_name + ' ' + self.lang.code

class News(models.Model):
    title = models.TextField(blank=True)
    mini_description = models.TextField(blank=True)
    photo1 = models.ImageField(upload_to='upload')
    photo2 = models.ImageField(upload_to='upload')
    photo3 = models.ImageField(upload_to='upload')
    name = models.TextField(blank=True)
    date = models.TextField(blank=True)
    description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    is_main = models.BooleanField(default=0, blank=True)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    link = models.TextField(blank=True)




    def __str__(self):
        return self.name


class Karta(models.Model):
    main_title = models.TextField(blank=True)
    mini_description = models.CharField(max_length=500, blank=True)
    address_link = models.CharField(max_length=500, blank=True)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)

    def __str__(self):
        return self.main_title + ' ' + self.lang.code

class Register(models.Model):
    last_name = models.CharField(max_length=300)
    first_name = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    message = models.TextField()
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    def __str__(self):
        return self.last_name

class Galery(models.Model):
    name = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='upload')
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    is_main = models.BooleanField(default=0, blank=True)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    photo = models.ImageField(upload_to='upload')
    last_name = models.TextField(blank=True)
    first_name = models.TextField(blank=True)
    surname = models.TextField(blank=True)
    position = models.TextField(blank=True)
    facebook = models.TextField(blank=True)
    instagram = models.TextField(blank=True)
    whatsapp = models.TextField(blank=True)
    telegram = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    is_main = models.BooleanField(default=0, blank=True)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)

    def __str__(self):
        return self.last_name


class Baza(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    link = models.TextField(blank=True)


    def __str__(self):
        return self.title


class Qabyldau(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    link = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Biliktilik(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    link = models.TextField(blank=True)


    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.TextField(blank=True)
    vide_link = models.TextField(blank=True)
    description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    link = models.TextField(blank=True)


    def __str__(self):
        return self.title

class KollejTarihi(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    link = models.TextField(blank=True)


    def __str__(self):
        return self.title

class License(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    link = models.TextField(blank=True)
    pdf = models.FileField(blank=True)
    word = models.FileField(blank=True)
    pdf_title = models.TextField(blank=True)
    word_title = models.TextField(blank=True)


    def __str__(self):
        return self.title



class Tulekter(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    link = models.TextField(blank=True)


    def __str__(self):
        return self.title

class Acredatsiya(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    def __str__(self):
        return self.title

class Qurylym(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    def __str__(self):
        return self.title

class Missiya(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    link = models.TextField(blank=True)

    def __str__(self):
        return self.title

class OquAdisteme(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    def __str__(self):
        return self.title

class Oqu(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    link = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Jemqorlyq(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    link = models.TextField(blank=True)

    def __str__(self):
        return self.title


class AdistemelikKabinet(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    link = models.TextField(blank=True)
    pdf = models.FileField(blank=True)
    word = models.FileField(blank=True)
    pdf_title = models.TextField(blank=True)
    word_title = models.TextField(blank=True)

    def __str__(self):
        return self.title

class JasMaman(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    link = models.TextField(blank=True)
    link = models.TextField(blank=True)
    pdf = models.FileField(blank=True)
    word = models.FileField(blank=True)
    pdf_title = models.TextField(blank=True)
    word_title = models.TextField(blank=True)


    def __str__(self):
        return self.title

class Birlestikter(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    def __str__(self):
        return self.title

class KenesJospary(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    link = models.TextField(blank=True)
    pdf = models.FileField(blank=True)
    word = models.FileField(blank=True)
    pdf_title = models.TextField(blank=True)
    word_title = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Jetistikter(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    link = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Qashyqtyq(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    def __str__(self):
        return self.title

class OquUrdisi(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    link = models.TextField(blank=True)
    pdf = models.FileField(blank=True)
    word = models.FileField(blank=True)
    pdf_title = models.TextField(blank=True)
    word_title = models.TextField(blank=True)

    def __str__(self):
        return self.title



class SabaqKeste(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    def __str__(self):
        return self.title

class StudentJetistik(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    link = models.TextField(blank=True)


    def __str__(self):
        return self.title

class StudenttikKenes(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    link = models.TextField(blank=True)
    pdf = models.FileField(blank=True)
    word = models.FileField(blank=True)
    pdf_title = models.TextField(blank=True)
    word_title = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Aqparat(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    def __str__(self):
        return self.title

class JumysqaOrnalasu(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    link = models.TextField(blank=True)
    pdf = models.FileField(blank=True)
    word = models.FileField(blank=True)
    pdf_title = models.TextField(blank=True)
    word_title = models.TextField(blank=True)


    def __str__(self):
        return self.title

class Seriktester(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    link = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Saualnama(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    link = models.TextField(blank=True)

    def __str__(self):
        return self.title



class Bitirushiler(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    def __str__(self):
        return self.title

class StudenttikOmir(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    link = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Talapker(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    lang = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1, blank=True)
    def __str__(self):
        return self.title


