# Generated by Django 4.0 on 2022-02-12 11:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
            options={
                'verbose_name': 'کارگردان',
                'verbose_name_plural': 'کارگردان ها',
            },
        ),
        migrations.CreateModel(
            name='HorrorVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('rating', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('video_file', models.FileField(upload_to='videos/horror')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos_module.director')),
            ],
            options={
                'verbose_name': 'فیلم ترسناک',
                'verbose_name_plural': 'فیلم های ترسناک',
            },
        ),
        migrations.CreateModel(
            name='DramaVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('rating', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('video_file', models.FileField(upload_to='videos/drama')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos_module.director')),
            ],
            options={
                'verbose_name': 'فیلم درام',
                'verbose_name_plural': 'فیلم های درام',
            },
        ),
        migrations.CreateModel(
            name='ActionVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('rating', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('video_file', models.FileField(upload_to='videos/action')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos_module.director')),
            ],
            options={
                'verbose_name': 'فیلم اکشن',
                'verbose_name_plural': 'فیلم های اکشن',
            },
        ),
    ]
