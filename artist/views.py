from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status

from .serializers import ArtistSerializer

class RegisterArtistView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "artist/register_artist.html"

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        """
        작가 등록 신청을 합니다.
        신청이 정상적으로 완료되면 인덱스 페이지로 이동합니다.
        """
        data = request.data.copy()

        data["user"] = request.user.id
        data["status"] = 2

        artist_serializer = ArtistSerializer(data=data)
        if artist_serializer.is_valid():
            artist_serializer.save()
            return redirect("index")

        return Response(status=status.HTTP_400_BAD_REQUEST)


class DashboardView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "artist/dashboard.html"

    def get(self, request):
        return Response(status=status.HTTP_200_OK)