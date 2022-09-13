from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status

from .models import Artist
from .models import Work
from .models import Exhibition

from .serializers import ArtistSerializer
from .serializers import WorkSerializer
from .serializers import ExhibitionSerializer

from open_gallery.permissions import IsNotSignedupUserOrAnonymous
from open_gallery.permissions import IsArtist

class RegisterArtistView(APIView):
    permission_classes = [IsNotSignedupUserOrAnonymous]

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
    permission_classes = [IsArtist]

    renderer_classes = [TemplateHTMLRenderer]
    template_name = "artist/dashboard.html"

    def get(self, request):
        """
        작가 페이지의 대시보드를 보여줍니다.
        작가 정보, 작품 정보, 전시 정보를 전송합니다.
        is_dashboard는 현재 보고있는 페이지가 대시보드라고 나타내는 플래그 용도로,
        현재 페이지에서 대시보드로 이동하는 링크를 생성하지 않기 위해 전송합니다.
        """
        artist = Artist.objects.filter(user=request.user, status_id=1).last()
        serialized_artist_data = ArtistSerializer(artist).data

        work_data = Work.objects.filter(artist=artist)
        serialized_work_data = WorkSerializer(work_data, many=True).data

        exhibition_data = Exhibition.objects.filter(artist=artist)
        serialized_exhibition_data = ExhibitionSerializer(exhibition_data, many=True).data

        response_data = {"artist": serialized_artist_data,
                         "works": serialized_work_data,
                         "exhibition_list": serialized_exhibition_data,
                         "is_dashboard": True}

        return Response(response_data, status=status.HTTP_200_OK)


class RegisterWorkView(APIView):
    permission_classes = [IsArtist]

    renderer_classes = [TemplateHTMLRenderer]
    template_name = "artist/register_work.html"

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        """
        작품을 등록합니다.
        """
        data = request.data.copy()

        data["artist"] = Artist.objects.get(user=request.user).id
        data["price"] = data.get("price", "").replace(",", "")

        work_serializer = WorkSerializer(data=data)
        if work_serializer.is_valid():
            work_serializer.save()
            return redirect("artist:work")

        return Response(status=status.HTTP_400_BAD_REQUEST)


class RegisterExhibitionView(APIView):
    permission_classes = [IsArtist]

    renderer_classes = [TemplateHTMLRenderer]
    template_name = "artist/register_exhibition.html"

    def get(self, request):
        work_data = Work.objects.filter(artist__user=request.user)
        serialized_work_data = WorkSerializer(work_data, many=True).data
        return Response({"works": serialized_work_data}, status=status.HTTP_200_OK)

    def post(self, request):
        """
        전시를 등록합니다.
        """
        data = request.data.copy()

        data["artist"] = Artist.objects.get(user=request.user).id
        exhibition_serializer = ExhibitionSerializer(data=data)
        if exhibition_serializer.is_valid():
            exhibition_serializer.save()
            return redirect("artist:exhibition")

        return Response(status=status.HTTP_400_BAD_REQUEST)