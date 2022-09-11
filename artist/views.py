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
        data = request.data.copy()

        data["user"] = request.user.id
        data["status"] = 2

        artist_serializer = ArtistSerializer(data=data)
        if artist_serializer.is_valid():
            artist_serializer.save()
            return redirect("index")

        return Response(status=status.HTTP_400_BAD_REQUEST)