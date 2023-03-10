# Generated by Django 4.1.7 on 2023-02-22 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('smak', '0003_rename_departmaneti_programi_departamenti'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
                ('atesia', models.CharField(blank=True, max_length=250)),
                ('titulli', models.CharField(choices=[('1', 'Msc.'), ('2', 'Dr'), ('3', 'Prof.Dr'), ('4', 'Doc')], max_length=6)),
                ('roli', models.CharField(choices=[('1', 'Pedagog'), ('2', 'ShefDep'), ('3', 'Dekan'), ('4', 'Rektor'), ('5', 'Kurrikula'), ('6', 'Admin')], default='1', max_length=10)),
                ('departamenti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dep_pedagog', to='smak.departamenti')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
