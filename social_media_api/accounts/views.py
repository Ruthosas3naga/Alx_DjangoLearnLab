from django.shortcuts import render
from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer
from .models import CustomUser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=400)


CustomUser = get_user_model()

class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        user_to_follow = CustomUser.objects.get(pk=pk)
        if request.user != user_to_follow:
            request.user.following.add(user_to_follow)
            return Response({'message': 'User followed successfully.'}, status=status.HTTP_200_OK)
        return Response({'error': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)

class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        user_to_unfollow = CustomUser.objects.get(pk=pk)
        if request.user != user_to_unfollow:
            request.user.following.remove(user_to_unfollow)
            return Response({'message': 'User unfollowed successfully.'}, status=status.HTTP_200_OK)
        return Response({'error': 'You cannot unfollow yourself.'}, status=status.HTTP_400_BAD_REQUEST)