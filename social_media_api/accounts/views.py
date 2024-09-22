from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions  # Changed this line
from django.contrib.auth import authenticate, get_user_model
from .serializers import RegisterSerializer

CustomUser = get_user_model()

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
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # Changed this line

    def post(self, request, pk):
        user_to_follow = get_object_or_404(CustomUser, pk=pk)
        if request.user != user_to_follow:
            request.user.following.add(user_to_follow)
            return Response({'message': 'User followed successfully.'}, status=status.HTTP_200_OK)
        return Response({'error': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)

class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # Changed this line

    def post(self, request, pk):
        user_to_unfollow = get_object_or_404(CustomUser, pk=pk)
        if request.user != user_to_unfollow:
            request.user.following.remove(user_to_unfollow)
            return Response({'message': 'User unfollowed successfully.'}, status=status.HTTP_200_OK)
        return Response({'error': 'You cannot unfollow yourself.'}, status=status.HTTP_400_BAD_REQUEST)