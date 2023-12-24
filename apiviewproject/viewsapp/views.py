from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *


# Create your views here.

class StudentAPI(APIView):
    def get(self,request):
        student_objs=Student.objects.all()
        serializers=StudentAPI

    def post(self,request):
        pass

    def put(self,request):
        pass


    def patch(self,request):
        pass
        



        
