from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ScreenShots
from datetime import datetime
from django.core.files.images import ImageFile
# Create your views here.

class Images(APIView):
    def post(self, request, format=None):

        ScreenShots.objects.create(img=request.FILES['myfile'])
        my_file = ScreenShots.objects.get(id=1)
        print(my_file.filename())
        return Response('Wszystko', status=status.HTTP_200_OK)