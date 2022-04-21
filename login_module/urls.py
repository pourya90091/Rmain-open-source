from django.urls import path
from login_module import views
from login_module.APIView import LoginView

urlpatterns = [
    path('', views.login, name='login-page'),

    # api :
    path('api', LoginView.as_view(), name='login-api')
]
