# Generated by Django 4.0 on 2022-02-12 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musics_module', '0003_alter_artis_options_alter_hypemusics_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Artis',
            new_name='MusicArtist',
        ),
        migrations.AlterModelOptions(
            name='musicartist',
            options={'verbose_name': 'هنرمند موسیقی', 'verbose_name_plural': 'هنرمندان موسیقی'},
        ),
    ]
