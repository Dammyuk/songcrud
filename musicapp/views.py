from django.shortcuts import render

from django.http import JsonResponse
from requests import delete
from musicapp.models import Artist,Lyric,Song
from musicapp.serializers import UserSerializers,SongSerializers,LyricSerializers
from rest_framework.parsers import JSONParser

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.






def snippet_list(request):
    """
    List all code snippets,or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Artist.objects.all()
        serializer = UserSerializers(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)


    elif request.method == 'GET':
        snippets = Song.objects.all()
        serializer = SongSerializers(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)


    elif request.method == 'GET':
        snippets = Lyric.objects.all()
        serializer = LyricSerializers(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


        @api_view(['GET', 'PUT', 'DELETE'])
        def snippet_detail(request, pk):
            """
            Retieve, update or delete a code snippet.
            """
            try:
                snippet = Song.objects.get(pk=pk)
                snippetLyrics = Lyric.objects.get(pk=pk)
            except Artist.DoesNotExists:
                return Response(status=status.HTTP_404_NOT_FUND)

            if request.method =='GET':
                serializer = SongSerializers(snippet)
                return Response(serializer.data)

            if request.method =='GET':
                serializer = LyricSerializers(snippetLyrics)
                return Response(serializer.data)

            elif request.method =='PUT':
                serializer = SongSerializers(snippet, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            elif request.method =='PUT':
                serializer = LyricSerializers(snippet, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            elif request.method =='DELETE':
                snippet.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)



