from rest_framework import serializers
from django.utils import dateformat

import re

from .models import Artist
from .models import Work
from .models import Exhibition


class ArtistSerializer(serializers.ModelSerializer):
    status_status = serializers.SerializerMethodField(read_only=True)
    signup_date = serializers.SerializerMethodField()

    def get_status_status(self, obj):
        return obj.status.status

    def get_signup_date(self, obj):
        return dateformat.format(obj.signup_date, 'y.m.d H:i:s')

    def validate(self, data):
        phone_re = re.compile("^010-\d{4}-\d{4}$")
        if not phone_re.match(data.get("phone", None)):
            raise serializers.ValidationError(
                   detail={"error": "형식에 맞게 입력해주세요!"},
            )

        if not data.get("gender", None) in ("여자", "남자"):
            raise serializers.ValidationError(
                   detail={"error": "여자와 남자 중에 입력해주세요!"},
            )

        return data

    class Meta:
        model = Artist
        fields = ["id", "user", "name", "gender", "birthday", "email", "phone", "signup_date", "status", "status_status"]


class WorkSerializer(serializers.ModelSerializer):

    def validate(self, data):
        size = int(data.get("size"))
        if size < 1 or size > 500:
            raise serializers.ValidationError(
                   detail={"error": "1 ~ 500 사이의 값을 입력해주세요!"},
            )
        return data

    class Meta:
        model = Work
        fields = ["id", "artist", "title", "price", "size"]


class ExhibitionSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if len(data.get("work")) < 1:
            raise serializers.ValidationError(
                detail = {"error": "작품을 하나 이상 선택해주세요!"},
            )

        if data.get("start_date") > data.get("end_date"):
            raise serializers.ValidationError(
                detail = {"error": "종료일은 시작일보다 빠를 수 없습니다!"},
            )

        return data

    class Meta:
        model = Exhibition
        fields = ["artist", "title", "start_date", "end_date", "work"]