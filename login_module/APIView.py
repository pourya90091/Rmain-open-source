from django.urls import reverse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from login_module.models import Users
from login_module.serializers import SettingsModelSerializer
from utils.hash_password import hash_password


class Settings(object):
    def __init__(self, username=None, password1=None, password2=None, error=None, url=None):
        self.username = username
        self.password1 = password1
        self.password2 = password2
        self.error = error
        self.url = url


class LoginView(APIView):
    def post(self, req):
        try:
            username = req.POST['username']
            password = req.POST['password']

            if username == '' or password == '':
                raise Exception('username and password must be set')
            if ' ' in username:
                raise Exception("username doesn't accept whitespace")

            try:
                Users.objects.get(username=username)
            except:
                raise Exception('this username not valid')

            try:
                Users.objects.get(username=username, password=hash_password(password))
            except:
                raise Exception('this password is wrong')

            user = Users.objects.get(username=username, password=hash_password(password))

            url = reverse('panel-page', args=[user.username])
            data = Settings(username=username, url=url)
            serializer = SettingsModelSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as err:
            data = Settings(error=err)
            serializer = SettingsModelSerializer(data)
            return Response(serializer.data, status=status.HTTP_403_FORBIDDEN)
