from django.shortcuts import redirect
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer


class UserView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'sign_up.html'

    def get(self, request):
        return Response({"message": "정상"}, status=status.HTTP_200_OK)
    
    # 회원가입
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            return redirect('login')
            
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        return Response({'message': 'put method'})
    
    def delete(self, request):
        return Response({'message': 'delete method'})


class UserApiView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'sign_in.html'

    def get(self, request):
        return Response({"message": "정상"}, status=status.HTTP_200_OK)

    # 로그인
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return redirect('index')

    # 로그아웃
    def delete(self, request):
        logout(request)
        return Response({"message": "정상"}, status=status.HTTP_200_OK)


class IndexView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        return Response({"message": "정상"}, status=status.HTTP_200_OK)