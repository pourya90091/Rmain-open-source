# Generated by Django 4.0 on 2022-02-11 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musics_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='hypemusics',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musics_module.artis'),
        ),
    ]
