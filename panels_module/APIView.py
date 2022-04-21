from django.urls import reverse
from django.utils.crypto import get_random_string
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from login_module.models import Users
from panels_module.serializers import SettingsModelSerializer
from site_module.settings import base_url, site_email, protocol
from utils.send_email import send_email
from utils.hash_password import hash_password
import re

# functions


def username_check(user, username):
    if user.username == username:
        raise Exception('you currently have this username')
    try:
        Users.objects.get(username=username)
    except:
        pass
    else:
        raise Exception('this username already used')
    if ' ' in username:
        raise Exception("username doesn't accept whitespace")


def password_check_False(user, password1, password2):
    if password1 != '' and password2 != '':
        if password1 != password2:
            raise Exception('password1 should be like password2')
    else:
        raise Exception('password must be confirm')
    try:
        Users.objects.get(username=user.username, password=hash_password(password2))
    except:
        pass
    else:
        raise Exception('you currently have this password')


def password_check_True(password1, password2):
    if password1 != '' or password2 != '':
        if password1 != '' and password2 != '':
            if password1 != password2:
                raise Exception('password1 should be like password2')
        else:
            raise Exception('password must be confirm')
    else:
        raise Exception('password must be enter')


def email_check(user, email):
    if not re.search(r"^\w+@\w+\.\w{2,3}$", email):
        raise Exception("email not valid")
    if user.email == email:
        raise Exception('you currently have this email')
    try:
        Users.objects.get(email=email)
    except:
        pass
    else:
        raise Exception('this email already used')


def raise_bad_request(msg):
    data = Settings(error=msg)
    serializer = SettingsModelSerializer(data)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class Settings(object):
    def __init__(self,
                 username=None,
                 password1=None,
                 password2=None,
                 error=None,
                 url=None,
                 image=None,
                 cookie_content=None,
                 MEDIA_URL= settings.MEDIA_URL):
        self.username = username
        self.password1 = password1
        self.password2 = password2
        self.error = error
        self.url = url
        self.image = image
        self.MEDIA_URL = MEDIA_URL
        self.cookie_content = cookie_content


class EditAccount(APIView):
    def post(self, req, panel_slug):
        try:
            user = Users.objects.get(username=panel_slug)
        except:
            user = False
        if user:
            try:
                username = req.POST['username']
                password1 = req.POST['password1']
                password2 = req.POST['password2']
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

                if username == '' and password1 == '' and password2 == '' and email == '' and image is None:
                    raise Exception('username or password or image or email must be set')

                # check username:
                if username != '':
                    username_check(user, username)
                    user.username = username

                # check password:
                if password1 != '' and password2 == '' or password1 == '' and password2 != '':
                    if username == '' and image == '' and email == '':
                        raise Exception('password must be confirm')
                if password1 != '' or password2 != '':
                    password_check_False(user, password1, password2)
                    user.password = hash_password(password2)

                # check email:
                if email != '':
                    email_check(user, email)
                    user.email = email

                # check image:
                if image:
                    user.image.delete()
                    user.image = image

                user.save()

                url = reverse('panel-page', args=[user.username])
                data = Settings(username=user.username, url=url)
                serializer = SettingsModelSerializer(data)
                return Response(serializer.data, status=status.HTTP_200_OK)

            except Exception as err:
                data = Settings(error=err)
                serializer = SettingsModelSerializer(data)
                return Response(serializer.data, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return raise_bad_request('not response')


class DeleteAccount(APIView):
    def post(self, req, panel_slug):
        try:
            user = Users.objects.get(username=panel_slug)
        except:
            user = False
        if user:
            try:
                password1 = req.POST['password1']
                password2 = req.POST['password2']

                password_check_True(password1, password2)

                try:
                    Users.objects.get(username=user.username, password=hash_password(password2))
                except:
                    raise Exception('password not valid')

                user.image.delete()
                user.delete()

                return Response(status=status.HTTP_200_OK)
            except Exception as err:
                data = Settings(error=err)
                serializer = SettingsModelSerializer(data)
                return Response(serializer.data, status=status.HTTP_406_NOT_ACCEPTABLE)


class EmailVerification(APIView):
    def post(self, req, panel_slug):
        try:
            user = Users.objects.get(username=panel_slug)
        except:
            user = False
        if user.email:
            if user.is_active is False:
                try:
                    password1 = req.POST['password1']
                    password2 = req.POST['password2']

                    password_check_True(password1, password2)
                    try:
                        Users.objects.get(username=user.username, password=hash_password(password2))
                    except:
                        raise Exception('password not valid')

                    try:
                        sender = site_email
                        getter = user.email
                        password = "hey you :)"
                        subject = "email verification code"
                        message = f"{protocol}://{base_url}{reverse('email-verification-code', args=[user.username, user.verification_code])}"
                        send_email(sender, getter, password, subject, message)
                    except Exception as err:
                        raise Exception(err)

                    url = reverse('panel-page', args=[user.username])
                    data = Settings(url=url)
                    serializer = SettingsModelSerializer(data)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except Exception as err:
                    data = Settings(error=err)
                    serializer = SettingsModelSerializer(data)
                    return Response(serializer.data, status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return raise_bad_request("email already is active")
        else:
            return raise_bad_request("you don't have email")


class DeleteImage(APIView):
    def post(self, req, panel_slug):
        try:
            user = Users.objects.get(username=panel_slug)
        except:
            user = False

        if user.image:
            user.image.delete()

            data = Settings(username=user.username)
            serializer = SettingsModelSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return raise_bad_request("profile image not set")


class GetUserInfo(APIView):
    def get(self, req, panel_slug):
        user = Users.objects.get(username=panel_slug)

        data = Settings(username=user.username,
                        url=reverse('panel-page', args=[user.username]),
                        image=user.image)
        serializer = SettingsModelSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogOut(APIView):
    def get(self, req, panel_slug):
        try:
            user = Users.objects.get(username=panel_slug)
        except:
            user = False
        if user:
            user.is_active = False
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class RecoverPassword(APIView):
    def post(self, req):
        if req.POST['email'] and \
           req.headers['Referer'] == f'{protocol}://{base_url}{reverse("recover-password-page")}':
            try:
                email = req.POST['email']
                if not re.search(r"^\w+@\w+\.\w{2,3}$", email):
                    raise Exception("email not valid")
                try:
                    try:
                        user = Users.objects.get(email=email)
                    except:
                        raise Exception("email not valid")

                    sender = site_email
                    getter = email
                    password = "hey you :)"
                    subject = "recover password"
                    message = f"{protocol}://{base_url}{reverse('ACP-page', args=[user.verification_code])}"
                    send_email(sender, getter, password, subject, message)

                    return Response(status=status.HTTP_200_OK)
                except Exception as err:
                    raise Exception(err)
            except Exception as err:
                data = Settings(error=err)
                serializer = SettingsModelSerializer(data)
                return Response(serializer.data, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return raise_bad_request('please enter email')


class ACP(APIView):
    def post(self, req, code):
        try:
            user = Users.objects.get(verification_code=code)
        except Exception as err:
            data = Settings(error=err)
            serializer = SettingsModelSerializer(data)
            return Response(serializer.data, status=status.HTTP_406_NOT_ACCEPTABLE)
        if req.headers['Referer'] == f'{protocol}://{base_url}{reverse("ACP-page", args=[user.verification_code])}':
            try:
                password_check_False(user, req.POST['password1'], req.POST['password2'])
                user.password = hash_password(req.POST['password2'])
                user.verification_code = get_random_string(72)
                user.save()

                url = reverse('login-page')
                data = Settings(url=url)
                serializer = SettingsModelSerializer(data)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as err:
                data = Settings(error=err)
                serializer = SettingsModelSerializer(data)
                return Response(serializer.data, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return raise_bad_request('permission denied')
