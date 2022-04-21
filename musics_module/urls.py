from django.urls import path
from musics_module import views

urlpatterns = [
    path('', views.musics, name='musics-page'),
    path('sad/', views.sad, name='sad-musics-page'),
    path('hype/', views.hype, name='hype-musics-page'),
    path('old/', views.old, name='old-musics-page'),
    path('<name>', views.music, name='music-page')
]
