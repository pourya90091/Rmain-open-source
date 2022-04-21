from django.db import models

# Create your models here.


class H(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    description = models.TextField(max_length=500, verbose_name="توضیحات")
    punishment = models.CharField(max_length=500, verbose_name="مجازات")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'حقیقت'
        verbose_name_plural = 'حقیقت ها'


class J(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    description = models.TextField(max_length=500, verbose_name="توضیحات")
    punishment = models.CharField(max_length=500, verbose_name="مجازات")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'جرعت'
        verbose_name_plural = 'جرعت ها'
