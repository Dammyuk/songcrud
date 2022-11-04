from xml.etree.ElementInclude import include
from django.urls import path

from musicapp import admin
from . import viewsets
from . import detailview

urlpatterns =[
    path('', viewsets.UserViewSet.as_view({'get':'first_name'}) ),
    path('<int:pk>/', detailview.artist_detail_view, name='detiails'),
    path('<int:pk>/', detailview.song_detail_view, name='detiails'),
    path('<int:pk>/', detailview.lyric_detail_view, name='detiails'),
    

]