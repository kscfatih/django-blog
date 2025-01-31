# Generated by Django 4.2.11 on 2025-01-04 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, null=True, verbose_name='Aktif mi ?')),
                ('birth_day', models.DateField(blank=True, null=True)),
                ('population', models.CharField(blank=True, choices=[('kisisel_gelisim', 'Kişisel Gelişim'), ('ders', 'Ders')], max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, null=True, verbose_name='Aktif mi ?')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, null=True, verbose_name='Aktif mi ?')),
                ('title', models.CharField(help_text='Max 100 karakter girmelisin', max_length=100, null=True, verbose_name='Başlık')),
                ('content', models.TextField(null=True, unique=True, verbose_name='İçerik')),
                ('blog_population', models.CharField(blank=True, choices=[('kisisel_gelisim', 'Kişisel Gelişim'), ('ders', 'Ders')], max_length=100, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blogs', to='blogapp.author')),
                ('category', models.ManyToManyField(blank=True, null=True, related_name='blogs', to='blogapp.category')),
            ],
            options={
                'verbose_name': 'Yazılar',
            },
        ),
    ]
