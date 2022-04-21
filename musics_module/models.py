from django.db import models

# Create your models here.


class MusicArtist(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'هنرمند موسیقی'
        verbose_name_plural = 'هنرمندان موسیقی'


class SadMusics(models.Model):
    name = models.CharField(max_length=50)
    artist = models.ForeignKey(MusicArtist, on_delete=models.CASCADE, null=False)
    song_track = models.FileField(upload_to='musics/sad')

    def __str__(self):
        return f"{self.name} - {self.artist}"

    class Meta:
        verbose_name = 'آهنگ غمگین'
        verbose_name_plural = 'آهنگ های غمگین'


class HypeMusics(models.Model):
    name = models.CharField(max_length=50)
    artist = models.ForeignKey(MusicArtist, on_delete=models.CASCADE, null=False)
    song_track = models.FileField(upload_to='musics/hype')

    def __str__(self):
        return f"{self.name} - {self.artist}"

    class Meta:
        verbose_name = 'آهنگ شاد'
        verbose_name_plural = 'آهنگ های شاد'


class OldMusics(models.Model):
    name = models.CharField(max_length=50)
    artist = models.ForeignKey(MusicArtist, on_delete=models.CASCADE, null=False)
    song_track = models.FileField(upload_to='musics/old')

    def __str__(self):
        return f"{self.name} - {self.artist}"

    class Meta:
        verbose_name = 'آهنگ قدیمی'
        verbose_name_plural = 'آهنگ های قدیمی'
