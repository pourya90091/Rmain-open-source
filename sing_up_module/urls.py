from django.urls import path
from sing_up_module import views
from sing_up_module.APIView import SingUpView

urlpatterns = [
    path('', views.sing_up, name='sing-up-page'),

    # api :
    path('api', SingUpView.as_view(), name='sing-up-api')
]
