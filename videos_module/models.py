from django.db import models
from django.core.validators import MaxValueValidator as Max, MinValueValidator as Min

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'کارگردان'
        verbose_name_plural = 'کارگردان ها'


class ActionVideos(models.Model):
    name = models.CharField(max_length=50)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=False)
    year = models.IntegerField()
    rating = models.FloatField(validators=[Min(0), Max(10)], default=0)
    video_file = models.FileField(upload_to='videos/action')

    def __str__(self):
        return f"{self.name} - {self.year}"

    class Meta:
        verbose_name = 'فیلم اکشن'
        verbose_name_plural = 'فیلم های اکشن'


class DramaVideos(models.Model):
    name = models.CharField(max_length=50)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=False)
    year = models.IntegerField()
    rating = models.FloatField(validators=[Min(0), Max(10)], default=0)
    video_file = models.FileField(upload_to='videos/drama')

    def __str__(self):
        return f"{self.name} - {self.year}"

    class Meta:
        verbose_name = 'فیلم درام'
        verbose_name_plural = 'فیلم های درام'


class HorrorVideos(models.Model):
    name = models.CharField(max_length=50)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=False)
    year = models.IntegerField()
    rating = models.FloatField(validators=[Min(0), Max(10)], default=0)
    video_file = models.FileField(upload_to='videos/horror')

    def __str__(self):
        return f"{self.name} - {self.year}"

    class Meta:
        verbose_name = 'فیلم ترسناک'
        verbose_name_plural = 'فیلم های ترسناک'
