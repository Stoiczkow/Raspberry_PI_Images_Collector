from django.shortcuts import render
from rest_framework.views import APIView
from django.views import View
from rest_framework.response import Response
from rest_framework import status
from .models import ScreenShots
from django.utils.datastructures import MultiValueDictKeyError
from datetime import datetime
from django.core.files.images import ImageFile
# Create your views here.

class ImagesApiView(APIView):
    def post(self, request, format=None):

        try:
            ScreenShots.objects.create(img=request.FILES['screen_shot'])
            return Response('Wszystko', status=status.HTTP_200_OK)
        except MultiValueDictKeyError:
            return Response("There's no file attached!",
                            status=status.HTTP_406_NOT_ACCEPTABLE)


class ListImages(View):
    def get(self, request):
        screen_shots = ScreenShots.objects.all()
        ctx = {'screen_shots': screen_shots}
        return render(request, 'img_api/index.html', ctx)