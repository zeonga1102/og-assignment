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
        username = request.data.get("username", "")
        password = request.data.get("password", "")

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return redirect("index")

    def delete(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class IndexView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "index.html"

    def get(self, request):
        user = request.user

        if user.is_authenticated:
            if user.is_admin:
                return Response({"user_type": "admin"}, status=status.HTTP_200_OK)

            is_artist = Artist.objects.filter(user=user.id).first()
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
        if type == "artist":
            artist_data = Artist.objects.filter(status__status="승인")
            serialized_artist_data = ArtistSerializer(artist_data, many=True).data
            return Response({"type": "artist", "artists": serialized_artist_data}, status=status.HTTP_200_OK)
        elif type == "work":
            work_data = Work.objects.all()
            serialized_work_data = WorkSerializer(work_data, many=True).data
            return Response({"type": "work", "works": serialized_work_data}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)