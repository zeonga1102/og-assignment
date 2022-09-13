from django.shortcuts import redirect
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from artist.models import Artist
from artist.models import Work

from .serializers import UserSerializer
from artist.serializers import ArtistSerializer
from artist.serializers import WorkSerializer


class UserView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "sign_up.html"

    def get(self, request):
        return Response(status=status.HTTP_200_OK)
    
    def post(self, request):
        """
        회원가입을 진행합니다.
        회원가입이 완료되면 로그인 페이지로 이동합니다.
        """
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            return redirect("login")
            
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserApiView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "sign_in.html"

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        """
        로그인을 진행합니다.
        사용자 인증이 올바르게 완료되면 인덱스 페이지로 이동합니다.
        """
        username = request.data.get("username", "")
        password = request.data.get("password", "")

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return redirect("index")

    def delete(self, request):
        """
        로그아웃을 합니다.
        """
        logout(request)
        return Response(status=status.HTTP_200_OK)


class IndexView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "index.html"

    def get(self, request):
        """
        인덱스 페이지를 보여줍니다.
        현재 유저가 인증된 사용자인지 아닌지 먼저 구분합니다.
        만약 인증된 사용자라면 관리자 계정인지, 작가 계정이라면 현재 등록 신청 상태는 어떠한지 또한 구분합니다.
        """
        user = request.user

        if user.is_authenticated:
            if user.is_admin:
                return Response({"user_type": "admin"}, status=status.HTTP_200_OK)

            is_artist = Artist.objects.filter(user=user.id).last()
            if is_artist:
                artist_status = is_artist.status.status
                if artist_status == "승인":
                    return Response({"user_type": "artist"}, status=status.HTTP_200_OK)
                elif artist_status == "대기":
                    return Response({"user_type": "waiting"}, status=status.HTTP_200_OK)
                else:
                    return Response({"user_type": "user"}, status=status.HTTP_200_OK)
            
        return Response({"user_type": "user"}, status=status.HTTP_200_OK)


class InfoView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "info.html"

    def get(self, request, type):
        """
        작가 혹은 작품 정보를 보여줍니다.
        작가 정보는 승인된 작가만 보여집니다.
        만약 검색을 한 것이라면 검색 결과를 보여줍니다.
        """
        keyword = request.GET.get("keyword", None)
        if len(keyword) > 30:
            keyword = keyword[:30]

        filter = request.GET.get("filter")
        
        if type == "artist":
            if keyword:
                if filter == "이름":
                    artist_data = Artist.objects.filter(status__status="승인", name__icontains=keyword).order_by("-signup_date")
                elif filter == "이메일":
                    artist_data = Artist.objects.filter(status__status="승인", email__icontains=keyword).order_by("-signup_date")
                else:
                    artist_data = Artist.objects.filter(status__status="승인", phone__icontains=keyword).order_by("-signup_date")
            else:
                artist_data = Artist.objects.filter(status__status="승인").order_by("-signup_date")
            
            serialized_artist_data = ArtistSerializer(artist_data, many=True).data
            
            return Response({"type": "artist", "artists": serialized_artist_data}, status=status.HTTP_200_OK)
        
        elif type == "work":
            if keyword:
                if filter == "제목":
                    work_data = Work.objects.filter(title__icontains=keyword).order_by("-register_date")
                else:
                    new_keyword = ""
                    for i in keyword:
                        try:
                            new_keyword += str(int(i))
                        except ValueError:
                            continue
                    if new_keyword == "":
                        return redirect("info", "work")
                    work_data = Work.objects.filter(size=new_keyword).order_by("-register_date")
            else:
                work_data = Work.objects.all().order_by("-register_date")

            serialized_work_data = WorkSerializer(work_data, many=True).data

            return Response({"type": "work", "works": serialized_work_data}, status=status.HTTP_200_OK)
        
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)