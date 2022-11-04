from musicapp import serializers
from .models import Artist,Lyric,Song
from requests import JSONDecodeError
from musicapp.serializers import UserSerializers,LyricSerializers,SongSerializers
from rest_framework import generics

class ArtistDetailAPIView(generics.RetrieveAPIView):
    try:
        queryset = Artist.objects.all()
        serializers_class = UserSerializers
    except:
        JSONDecodeError(raise_exception=True)

artist_detail_view = ArtistDetailAPIView.as_view()

class SongDetailAPIView(generics.RetrieveAPIView):
    try:
        queryset =Song.objects.all()
        serializers_class =SongSerializers
    except:
        JSONDecodeError(raise_exception=True)

song_detail_view = SongDetailAPIView.as_view()


class LyricDetailAPPIView(generics.RetrieveAPIView):
    try:
        queryset = Lyric.objects.all()
        serializer_class = LyricSerializers
    except:
        JSONDecodeError(raise_exception=True)

lyric_detail_view = LyricDetailAPPIView.as_view()


