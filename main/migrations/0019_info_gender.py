# Generated by Django 4.1.4 on 2022-12-12 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_info_profession'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='gender',
            field=models.CharField(choices=[('Мужчина', 'Мужской'), ('Женщина', 'Женский')], default='Пол не выбран', max_length=7),
        ),
    ]
