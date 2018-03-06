from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views  import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import TemplateView
from django.views import View
import datetime
from django.utils.timezone import utc

from . models import app_1
from . serializers import app_1_Serializer
# Create your views here.

class App1List(APIView):
    
    def get(self,request, format=None):
        app_list_1= app_1.objects.all()
        serializer = app_1_Serializer(app_list_1, many=True)
        return Response(serializer.data)

 
    def post(self, request, format='json'):
        serializer = app_1_Serializer(data=request.data)
        if serializer.is_valid():
            result= serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  
class App1Individual(APIView):
    def get_object(self, pk):
        try:
            return app_1.objects.get(pk=pk)
        except app_1.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        app_list_1= self.get_object(pk)
        serializer = app_1_Serializer(app_list_1)
        return Response(serializer.data)


    def put(self, request, pk, format='json'):
        app_list_1 = self.get_object(pk)
        serializer = app_1_Serializer(app_list_1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format='json'):
        app_list_1 = self.get_object(pk)
        app_list_1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)