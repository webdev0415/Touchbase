# Generated by Django 2.1.1 on 2019-07-29 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_userprofile_has_tcss'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tri_count', models.IntegerField(default=0)),
                ('has_tcss', models.BooleanField(default=False)),
                ('views_privacy', models.BooleanField(default=True)),
                ('toush_enabled', models.BooleanField(default=True)),
                ('toush_max_links', models.IntegerField(default=-1)),
                ('toush_max_concurrent_links', models.IntegerField(default=100)),
                ('toush_default_lifespan', models.IntegerField(default=86400)),
                ('toush_default_max_uses', models.IntegerField(default=-1)),
                ('haspSPF', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='has_tcss',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='haspSPF',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='toush_default_lifespan',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='toush_default_max_uses',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='toush_enabled',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='toush_max_concurrent_links',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='toush_max_links',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='views_privacy',
        ),
    ]