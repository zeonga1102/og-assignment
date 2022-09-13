from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException
from rest_framework import status

from artist.models import Artist


class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code=status_code
        super().__init__(detail=detail, code=code)


class IsNotSignedupUser(BasePermission):
    message = "접근 권한이 없습니다."

    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            response ={
                    "detail": "서비스를 이용하기 위해 로그인 해주세요.",
                }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)

        if user.is_admin:
            return False

        is_applicant = user.artist_set.all().last()
        if not is_applicant:
            return True
        
        if is_applicant.status.status == "반려":
            return True
        
        return False


class IsArtist(BasePermission):
    message = "접근 권한이 없습니다."

    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            response ={
                    "detail": "서비스를 이용하기 위해 로그인 해주세요.",
                }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)
        
        if user.is_admin:
            return False

        if Artist.objects.filter(user=user, status_id=1).last():
            return True

        return False