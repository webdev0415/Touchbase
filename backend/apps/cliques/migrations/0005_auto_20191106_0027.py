# Generated by Django 2.1.1 on 2019-11-06 00:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cliques', '0004_auto_20190904_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='clique',
            name='token',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Token'),
        ),
        migrations.AlterField(
            model_name='clique',
            name='thumbnail',
            field=models.URLField(default='https://tbdev.nyc3.cdn.digitaloceanspaces.com/m/blank-face.png', verbose_name='profile_pic'),
        ),
    ]
