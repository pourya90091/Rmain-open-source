from django.urls import reverse
from django.utils.crypto import get_random_string
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from login_module.models import Users
from sing_up_module.serializers import SettingsModelSerializer
from utils.hash_password import hash_password
import re


class Settings(object):
    def __init__(self, username=None, password1=None, password2=None, error=None, url=None):
        self.username = username
        self.password1 = password1
        self.password2 = password2
        self.error = error
        self.url = url


class SingUpView(APIView):
    def post(self, req):
        try:
            username = req.POST['username']
            password = req.POST['password']
            email = req.POST['email']

            try:
                image = req.FILES['image']
                jpg = re.findall(r"(\.jpg$)", str(image))
                png = re.findall(r"(\.png$)", str(image))
                if jpg or png:
                    pass
                else:
                    raise ValueError('image format must be jpg or png')
            except ValueError as err:
                raise Exception(err)
            except:
                image = None

            if username == '' or password == '':
                raise Exception("username and password must be set")
            if ' ' in username:
                raise Exception("username doesn't accept whitespace")
            if len(username) > 20 or len(password) > 20:
                raise Exception("username or password length is long")

            if email != '':
                if not re.search(r"^\w+@\w+\.\w{2,3}$", email):
                    raise Exception("email not valid")
                try:
                    Users.objects.get(email=email)
                except:
                    pass
                else:
                    raise Exception('this email already used')
            else:
                email = None

            try:
                Users.objects.get(username=username)
            except:
                pass
            else:
                raise Exception('username already used')

            new_user = Users(username=username,
                             email=email,
                             verification_code=get_random_string(72),
                             password=hash_password(password),
                             image=image)
            new_user.save()

            url = reverse('panel-page', args=[new_user.username])

            data = Settings(username=username, url=url)
            serializer = SettingsModelSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as err:
            data = Settings(error=err)
            serializer = SettingsModelSerializer(data)
            return Response(serializer.data, status=status.HTTP_406_NOT_ACCEPTABLE)
