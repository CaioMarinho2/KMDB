
from rest_framework import serializers
from genres.serializers import GenreSerializer
from genres.models import Genre
from movies.models import Movie


class MovieSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration =  serializers.CharField(max_length=10)
    premiere= serializers.DateField()
    classification= serializers.IntegerField()
    synopsis= serializers.CharField()
    
    genres=GenreSerializer(many=True)
    
    
    def create(self, validated_data):
        genres_data=validated_data.pop("genres")
        
        movie= Movie.objects.create(**validated_data)
        for genre in genres_data:
            genre_create,created=Genre.objects.get_or_create(**genre)
            movie.genres.add(genre_create)
        return movie
    
    def update(self, instance, validated_data):
         for key, value in validated_data.items():
             if key=="genres":
                 genres_list_data=[]
                 for genre in value:
                     genre,create=Genre.objects.get_or_create(**genre)
                     genres_list_data.append(genre)
                 instance.genres.set(genres_list_data)
             else:   
                 setattr(instance,key, value )
         instance.save()    
         return instance    
             
             
        
        