from django.shortcuts import render
from rest_framework.views import APIView
from django.views import View
from rest_framework.response import Response
from rest_framework import status
from .models import ScreenShots, Files
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta
from django.urls import reverse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class ImagesApiView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    def post(self, request, format=None):

        try:
            img = ScreenShots.objects.create(img=request.FILES['screen_shot'])
            file_name = request.POST['file_name']
            A_index = file_name.index('A')
            B_index = file_name.index('B')
            C_index = file_name.index('C')
            time = file_name[0:A_index]
            latitude = file_name[A_index + 1:B_index]
            longitude = file_name[B_index + 1:C_index]

            img.img_name = file_name
            img.created = time
            img.latitude = latitude
            img.longitude = longitude
            img.save()
            # time = datetime.strptime(time, '%Y-%m-%d %I:%M:%S.%f')
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
        screen_shots = ScreenShots.objects.all().order_by('created')
        ctx = {'screen_shots': screen_shots}
        return render(request, 'img_api/index.html', ctx)


class CreateTracks(View):
    def get(self, request):
        tracks = []

        screen_shots = ScreenShots.objects.all().order_by('created')
        try:
            current = datetime.strptime(screen_shots[0].created,
                                        '%Y-%m-%d %H:%M:%S.%f')
        except IndexError:
            pass
        working_track = ''

        for screen in screen_shots:
            screen_d = datetime.strptime(str(screen.created),
                                         '%Y-%m-%d %H:%M:%S.%f')
            if (screen_d - current) < timedelta(seconds=5):
                working_track += screen.latitude
                working_track += ',-'
                working_track += screen.longitude
                working_track += ',"{}",'.format(screen.created)
                working_track += '"http://207.154.253.47/static/{}","http://207.154.253.47/static/{}",'.format(
                    screen.img_name.replace(' ', '_').replace(':', ''),
                    screen.img_name.replace(' ', '_').replace(':', ''))
                working_track += '\n'
                current = screen_d
            else:
                tracks.append(working_track)
                working_track = ''
                working_track += screen.latitude
                working_track += ',-'
                working_track += screen.longitude
                working_track += ',"{}",'.format(screen.created)
                working_track += '"http://207.154.253.47/static/{}","http://207.154.253.47/static/{}",'.format(
                    screen.img_name.replace(' ', '_').replace(':', ''),
                    screen.img_name.replace(' ', '_').replace(':', ''))
                working_track += '\n'
                current = screen_d
        tracks.append(working_track)
        for j in range(0, len(tracks)):
            with open('{}.txt'.format(j), "w") as f:
                f.write(tracks[j])
        ctx = {'done': 'Tracks files were generated'}
        return HttpResponseRedirect(reverse('index'))


class FilesApiView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        try:
            file = Files.objects.create(file=request.FILES['file'])
            file_name = request.POST['file_name']

            file.file_name = file_name
            file.save()

            return Response({'status': 'ok'}, status=status.HTTP_200_OK)
        except MultiValueDictKeyError:
            return Response("There's no file attached!",
                            status=status.HTTP_406_NOT_ACCEPTABLE)

