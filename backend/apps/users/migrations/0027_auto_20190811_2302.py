# Generated by Django 2.1.1 on 2019-08-11 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_auto_20190810_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersettings',
            name='hasp_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usersettings',
            name='hasp_celebrity',
            field=models.BooleanField(default=False),
        ),
    ]
