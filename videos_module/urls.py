from django.urls import path
from videos_module import views

urlpatterns = [
    path('', views.videos, name='videos-page'),
    path('action/', views.action, name='action-videos-page'),
    path('drama/', views.drama, name='drama-videos-page'),
    path('horror/', views.horror, name='horror-videos-page'),
    path('<name>', views.video, name='video-page')
]
