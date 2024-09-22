from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, FeedView, LikePostView, UnlikePostView


# Register viewsets with the router
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

# Define URL patterns
urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feed'), 
    path('', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
    path('<int:pk>/', PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='post-detail'),
    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),  # Add like route
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),  # Add unlike route
    path('comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
]

