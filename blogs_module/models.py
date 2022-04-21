from django.db import models

# Create your models here.


class Jokes(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField()
    rate = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "جوک"
        verbose_name_plural = "جوک ها"


class Weather(models.Model):
    city = models.CharField(max_length=40)
    temp = models.FloatField()

    def __str__(self):
        return f"{self.city} : {self.temp}"

    class Meta:
        verbose_name = "آب و هوا"
