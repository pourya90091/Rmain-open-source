from django.urls import path
from blogs_module import views
from blogs_module import APIView

urlpatterns = [
    path('', views.blogs, name='blogs-page'),
    path('joke', views.joke, name='joke-page'),
    path('weather', views.weather, name='weather-page'),
    path('resume', views.resume, name='resume-page'),

    # api:
    path('joke/show-more', APIView.ShowMore.as_view())
]
