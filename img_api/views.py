from django.shortcuts import render
from rest_framework.views import APIView
from django.views import View
from rest_framework.response import Response
from rest_framework import status
from .models import ScreenShots
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponseRedirect
from datetime import datetime
from django.urls import reverse

# Create your views here.

class ImagesApiView(APIView):
    def post(self, request, format=None):

        try:
            img = ScreenShots.objects.create(img=request.FILES['screen_shot'])
            file_name = img.filename
            A_index = file_name.index('A')
            B_index = file_name.index('B')
            C_index = file_name.index('C')
            time = file_name[0:A_index]
            latitude = file_name[A_index + 1:B_index]
            longitude = file_name[B_index + 1:C_index]

            img.created = time
            img.latitude = latitude
            img.longitude = longitude
            img.save()
            # time = datetime.strptime(time, '%Y-%b-%dT%I%M%SZ')
            # print(str(datetime.now()))
            print(time)
            print(latitude)
            print(longitude)
            return Response('Wszystko', status=status.HTTP_200_OK)
        except MultiValueDictKeyError:
            return Response("There's no file attached!",
                            status=status.HTTP_406_NOT_ACCEPTABLE)

class ListImages(View):
    def get(self, request):
        screen_shots = ScreenShots.objects.all()
        ctx = {'screen_shots': screen_shots}
        return render(request, 'img_api/index.html', ctx)


class CreateTracks(View):
    def get(self, request):
        tracks = []

        screen_shots = ScreenShots.objects.all()
        try:
            current = datetime.strptime(screen_shots[0].created,
                                        '%Y-%m-%d %I:%M:%S.%f')
        except IndexError:
            pass
        working_track = ''

        for screen in screen_shots:
            screen_d = datetime.strptime(str(screen.created),
                                         '%Y-%m-%d %I:%M:%S.%f')
            if (screen_d - current) < 2:
                working_track += screen.latitude
                working_track += screen.longitude
                working_track += '\n'
                current = screen_d
            else:
                tracks.append(working_track)
                working_track = ''

        for i in range(0, len(tracks)):
            with open('{}.txt'.format(i), "+w") as f:
                f.write(tracks[i])
        ctx = {'done': 'Tracks files were generated'}
        return HttpResponseRedirect(reverse('index'))
