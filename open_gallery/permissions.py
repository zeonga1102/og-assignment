from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException
from rest_framework import status

from artist.models import Artist


class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code=status_code
        super().__init__(detail=detail, code=code)


class IsNotSignedupUserOrAnonymousAndMethodGet(BasePermission):
    """
    한번도 작가 신청을 하지 않은 사용자와 신청을 했으나 반려당한 사용자만 접근 허용합니다.
    또한 로그인 하지 않은 유저의 접근도 GET method에 한해서 허용합니다.
    로그인 하지 않은 유저는 해당 페이지에 접근할 때 로그인 페이지로 이동시켜줍니다.
    """
    message = "접근 권한이 없습니다."

    def has_permission(self, request, view):
        user = request.user

        if user.is_anonymous and request.method =="GET":
            return True

        if user.is_anonymous:
            return False

        if user.is_admin:
            return False

        is_applicant = user.artist_set.all().last()
        if not is_applicant:
            return True
        
        if is_applicant.status.status == "반려":
            return True
        
        return False


class IsArtist(BasePermission):
    """
    승인된 작가만 접근 가능합니다.
    """
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