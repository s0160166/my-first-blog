# Generated by Django 4.1.4 on 2022-12-10 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_results'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='age',
            field=models.IntegerField(default=20),
        ),
    ]
