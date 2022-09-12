from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status

from artist.models import Artist

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