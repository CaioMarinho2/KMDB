from asyncore import read
from rest_framework import serializers
from user.models import User
from reviews.models import Review



class CriticSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=["id","first_name","last_name"]


class ReviewSerializer(serializers.ModelSerializer):
    critic =CriticSerializer(read_only=True)

    class Meta:
        model= Review
        fields=["id","stars","review","spoilers","recomendation","movie_id","critic"]
        read_only_fields=["movie_id"]