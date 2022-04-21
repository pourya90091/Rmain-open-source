from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from games_module.models import H
from games_module.models import J
from games_module.serializers import HModelSerializer
from games_module.serializers import JModelSerializer
from random import randint


class GetHJ(APIView):
    random = 0

    @classmethod
    def get(cls, req, HJ):
        m = min([len(H.objects.all()), len(J.objects.all())])

        random_pk = randint(1, m)
        while random_pk == cls.random:
            random_pk = randint(1, m)
        cls.random = random_pk

        if HJ == 'H':
            query = H.objects.get(pk=random_pk)
            serializer = HModelSerializer(query)
        if HJ == 'J':
            query = J.objects.get(pk=random_pk)
            serializer = JModelSerializer(query)
        return Response(serializer.data, status=status.HTTP_200_OK)
