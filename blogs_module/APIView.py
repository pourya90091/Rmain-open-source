from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from blogs_module.serializers import SettingsModelSerializer
from blogs_module.models import Jokes


class Settings(object):
    def __init__(self, new_jokes=None):
        self.new_jokes = new_jokes


class ShowMore(APIView):
    def post(self, req):
        current = int(req.POST['current'])
        new_jokes = Jokes.objects.all()[current:current+5]

        jokesJ = []
        for joke in new_jokes:
            new_joke = {
                "id": joke.id,
                "title": joke.title,
                "text": joke.text,
                "rate": joke.rate
            }
            jokesJ.append(new_joke)

        data = Settings(jokesJ)
        serializer = SettingsModelSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
