from rest_framework import serializers,viewsets

from musicapp.models import Artist,Song,Lyric


class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ['first_name','last_name','age']

    def create(self, validated_data):
        return Artist.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name',instance.last_name)
        instance.age = validated_data.get('age',instance.age)
        instance.save()
        return instance

class SongSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ['artist_id','title','date_released','likes']

    def create(self, validated_data):
        return Song.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.artist_id = validated_data.get('artist_id',instance.artist_id)
        instance.title = validated_data.get('title',instance.title)
        instance.date_released = validated_data.get('date_released',instance.validated)
        instance.likes = validated_data.get('likes',instance.validated)
        instance.save()
        return instance

class LyricSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lyric
        fields = ['content','song_id']

    def create(self, validated_data):
        return Lyric.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content',instance.content)
        instance.song_id = validated_data.get('song_id',instance.song_id)
        instance.save()
        return instance

