from django.db import models
from django.utils import timezone
from employer.models import Vacancy
from profiles.models import Profile
from django.conf import settings

class Contact(models.Model):
    first_name = models.CharField(max_length=250, blank=True, verbose_name="Имя")
    last_name = models.CharField(max_length=500, blank=True, verbose_name="Фамилия")
    phone_main = models.CharField(max_length=50, unique=True, verbose_name="Телефон1")
    phone2 = models.CharField(max_length=50,  blank=True, verbose_name="Телефон2")
    phone3 = models.CharField(max_length=50,  blank=True, verbose_name="Телефон3")
    viber = models.CharField(max_length=50,  blank=True, verbose_name="Вайбер")
    telegram = models.CharField(max_length=50,  blank=True, verbose_name="Телеграм")
    email = models.CharField(max_length=50, blank=True, verbose_name="Имейл")
    age = models.IntegerField(blank=True, default=0, verbose_name="Возраст")
    sex = models.CharField(max_length=1, blank=True, choices=(("м", "Мужской"),("ж", "Женский")), verbose_name="Пол")
    is_client = models.BooleanField(default=False)
    in_sales = models.BooleanField(default=True)
    profiles = models.ManyToManyField("SkillProfile", default=None, blank=True, verbose_name="Проф. профили кандидата")
    agent = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
    source = models.ForeignKey("ContactSource", on_delete=models.CASCADE, verbose_name="Источник контакта")
    lead_quality = models.IntegerField(default=0, verbose_name="Качество лида", choices=((-2, "Отказ"), (-1, "Недозвон"), (0, "Новый"), (1, "Интересно"), (2, "Другая Вакансия"), (3, "Приоритет"), (4,"Сделка")))
    city = models.CharField(max_length=200, default='', blank=True, verbose_name="Город проживания")
    next_contact_date = models.DateTimeField(default='1980-01-01 12:12:12', verbose_name="Дата следующего контакта")
    last_contact_date = models.DateTimeField(default='1980-01-01 12:12:12')
    comment = models.CharField(max_length=1500, blank=True, verbose_name="Дополнительно")
    cv_url = models.CharField(max_length=250, blank=True, verbose_name="Ссылка на резюме")
    cv_title = models.CharField(max_length=100, blank=True, verbose_name="Заголовок резюме")
    color = models.CharField(max_length=20, blank=True, verbose_name="Цвет", choices=(("blue","Синий"),("SkyBlue","Голубой"),("green","Зеленый"),("yellow","Желтый"),("orange","Оранжевый"),("red","Красный")))
    objection = models.CharField(max_length=100, blank=True, verbose_name="Причина отказа")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name

class SkillProfile(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name="Название профиля")
    def __str__(self):
        return self.name

class Interaction(models.Model):
    agent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    result = models.CharField(max_length=500, blank=True)
    interaction_date = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=200, default="звонок", choices=(("звонок", "Звонок"),("email", "Email"),("sms", "Sms"),
                                                     ("messenger", "Messenger"), ("автопрозвон", "Автопрозвон")))
    class Meta:
        get_latest_by='id'

class Order(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    interaction = models.OneToOneField(Interaction, on_delete=models.CASCADE)
    sale_agent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sale_agent',  default=None)
    provision_agent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='provision_agent', default=None)
    status = models.CharField(max_length=50, choices=(("waiting","Ожидает оплаты"),("paid","Оплачен"),("approved","Подтвержден")))

class ContactSource(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name="Название источника")
    description = models.CharField(max_length=250, blank=False, verbose_name="Описание с примерами")
    potential_profiles = models.ManyToManyField("SkillProfile", default=None, blank=True, verbose_name="Возможные профили")
    def __str__(self):
        return self.name