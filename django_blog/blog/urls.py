from django.urls import path
from django.contrib.auth import views as auth_views
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import add_comment, edit_comment, delete_comment

urlpatterns = [
    path('login/', auth_views.LoginView.auth_view(), name='login'),
    path('logout/', auth_views.LogoutView.auth_view(), name='logout'),
    path('register/', auth_views.register.as_view(), name='register'),
    path('profile/', auth_views.profile.as_view(), name='profile'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_id>/comment/', add_comment, name='add-comment'),
    path('comment/<int:comment_id>/edit/', edit_comment, name='edit-comment'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete-comment')
]