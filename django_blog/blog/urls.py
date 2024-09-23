from django.urls import path
from django.contrib.auth import views as auth_views
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView, search_posts, PostByTagListView, RegisterView, ProfileView 

urlpatterns = [
    path('login/', auth_views.LoginView.auth_view(), name='login'),
    path('logout/', auth_views.LogoutView.auth_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/', CommentCreateView, name='add-comment'),
    path('comment/<int:pk>/update/', CommentUpdateView, name='update-comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView, name='delete-comment'),
    path('search/', search_posts, name='search-posts'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),
]