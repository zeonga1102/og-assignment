from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status

from artist.models import Artist
from artist.models import Status

from artist.serializers import ArtistSerializer


class DashboardView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "manager/dashboard.html"

    def get(self, request):
        return Response({"is_dashboard": True}, status=status.HTTP_200_OK)


class RegisterListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "manager/register_list.html"

    def get(self, request):
        artist_data = Artist.objects.all()
        serialized_artist_data = ArtistSerializer(artist_data, many=True).data
        return Response({"artists": serialized_artist_data}, status=status.HTTP_200_OK)

    def put(self, request, new_status):
        artist_data = Artist.objects.filter(id__in=request.data.get("selectedArtists", None))

        try:
            new_status_data = Status.objects.get(id=new_status)
        except Status.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        for ad in artist_data:
            ad.status = new_status_data
            ad.save()

        return Response(status=status.HTTP_200_OK)


class StatisticsView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "manager/statistics.html"

    def get(self, request):
        return Response(status=status.HTTP_200_OK)