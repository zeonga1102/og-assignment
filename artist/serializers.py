from rest_framework import serializers

import re

from .models import Artist
from .models import Work


class ArtistSerializer(serializers.ModelSerializer):

    def validate(self, data):
        phone_re = re.compile("^010-\d{4}-\d{4}$")
        if not phone_re.match(data.get("phone", None)):
            raise serializers.ValidationError(
                   detail={"error": "형식에 맞게 입력해주세요!"},
               )

        return data

    class Meta:
        model = Artist
        fields = ["user", "name", "gender", "birthday", "email", "phone", "signup_date", "status"]


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ["artist", "title", "price", "size"]