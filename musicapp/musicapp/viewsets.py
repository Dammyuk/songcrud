from rest_framework import viewsets
from rest_framework import permissions
from musicapp.models import Artist,Song,Lyric
from musicapp.serializers import UserSerializers,SongSerializers, LyricSerializers


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by('-first_name')
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('-date_released')
    serializer_class = SongSerializers
    permission_classes = [permissions.IsAuthenticated]



class LyricsViewSet(viewsets.ModelViewSet):
    queryset = Lyric.objects.all().order_by('-song_id')
    serializer_class = LyricSerializers
    permission_classes = [permissions.IsAuthenticated]