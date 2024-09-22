from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from notifications.models import Notification
from notifications.serializers import NotificationSerializer
from rest_framework.permissions import IsAuthenticated

class CreateNotificationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        action_type = request.data.get('action_type')
        recipient_id = request.data.get('recipient_id')  # User who will receive the notification

        if action_type == "follow":
            # Handle follow action notification
            Notification.objects.create(
                recipient_id=recipient_id,
                actor=request.user,
                verb="followed you",
                target_content_type=ContentType.objects.get_for_model(User),
                target_object_id=request.user.id,
            )
        # Handle other action types similarly...

        return Response({"detail": "Notification created successfully."}, status=201)

class NotificationListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        # Fetch notifications for the current user
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')
