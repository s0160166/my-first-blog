from django.db import models
from django.utils.translation import gettext_lazy as _


class Info(models.Model):
    professions = (
        (str(0), 'Работа в офисе/на дому/работа, не связанная с риском'),
        (str(265/365), 'Пилот'),
        (str(217/365), 'Рыбак'),
        (str(205/365), 'Водитель грузового транспорта'),
        (str(172/365), 'Лесоруб'),
        (str(165/365), 'Строитель'),
        (str(160/365), 'Моряк'),
        (str(141/365), 'Литейшик'),
        (str(139/365), 'Рабочий деревообрабатывающей промышленности'),
        (str(118/365), 'Шахтёр'),
        (str(107/365), 'Фермер'),
    )
    hobbies = (
        (str(91.2), 'Бейсджампинг'),
        (str(27.3), 'Автогонки'),
        (str(4.8), 'Дельтаплан'),
        (str(2.7), 'Мотогонки'),
        (str(1.5), 'Альпинизм'),
        (str(1.2), 'Бокс и ММА'),
        (str(0.27), 'Каякинг'),
        (str(0.17), 'Треккинг/Велосипедный спорт'),
        (str(0.08), 'Дайвинг'),
        (str(0.02), 'Парашютный спорт'),
        (str(0), 'Другое'),
    )
    GENDER = (
        ('Мужчина', 'Мужчина'),
        ('Женщина', 'Женщина'),
    )
    id = models.AutoField(primary_key=True)
    gender = models.CharField(
        max_length=7,
        choices=GENDER,
        default='Пол не выбран',
    )
    date_born = models.DateField()
    age = models.IntegerField(default=20)
    loan_balance = models.IntegerField(default=1000000)
    micromorts = models.TextField(default=0)
    cigarets = models.TextField(default=0)
    alcogol = models.TextField(default=0)
    profession = models.CharField(
        max_length=250,
        choices=professions,
        default=0,
    )
    hobby = models.CharField(
        max_length=250,
        choices=hobbies,
        default=0,
    )
    obrabotka = models.BooleanField(default=False)
    def __unicode__(self):
        return self.id

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'




class Results(models.Model):
    id = models.AutoField(primary_key=True)
    sum = models.IntegerField(default=0)

    def __unicode__(self):
        return self.id

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
