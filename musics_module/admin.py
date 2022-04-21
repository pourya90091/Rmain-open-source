from django.contrib import admin
from musics_module import models

# Register your models here.

admin.site.register(models.SadMusics)
admin.site.register(models.HypeMusics)
admin.site.register(models.OldMusics)
admin.site.register(models.MusicArtist)
