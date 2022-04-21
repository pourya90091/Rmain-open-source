from django.contrib import admin
from videos_module import models

# Register your models here.

admin.site.register(models.ActionVideos)
admin.site.register(models.DramaVideos)
admin.site.register(models.HorrorVideos)
admin.site.register(models.Director)
