from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status


class DashboardView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "manager/dashboard.html"

    def get(self, request):
        return Response({"is_dashboard": True}, status=status.HTTP_200_OK)