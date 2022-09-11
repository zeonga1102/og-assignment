from rest_framework import serializers
from .models import Artist
from .models import Work


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["user", "name", "gender", "birthday", "email", "phone", "signup_date", "status"]


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ["artist", "title", "price", "size"]