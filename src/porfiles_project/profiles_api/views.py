from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    """ Test API View """
    def get(self, request, format=None):
        """ Returnns a list of APIViews features """

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to a traditional Django View'
        ]

        return Response({'message': 'hello', 'an_apiview': an_apiview})
