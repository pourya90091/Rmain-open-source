from django.db import models

# Create your models here.


class SiteSettings(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    base_url = models.URLField()
    about_us = models.TextField()
    email = models.EmailField()
    copy_right = models.TextField()
    logo = models.ImageField(upload_to='logo', null=True)
    main = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "تنظیمات"
        verbose_name_plural = "تنظیمات ها"
