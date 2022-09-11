from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status

class RegisterArtistView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "artist/register_artist.html"

    def get(self, request):
        return Response(status=status.HTTP_200_OK)