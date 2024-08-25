from django.contrib import admin
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)


# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import CustomUser

# Custom forms for creating and changing users in the admin
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'profile_photo')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'profile_photo')

# Custom UserAdmin class
class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'date_of_birth', 'profile_photo', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

# Register the custom user admin
admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Post  # replace 'myapp' with your actual app name

# Get or create groups
editors_group, created = Group.objects.get_or_create(name='Editors')
viewers_group, created = Group.objects.get_or_create(name='Viewers')
admins_group, created = Group.objects.get_or_create(name='Admins')

# Get permissions
can_view_post = Permission.objects.get(codename='can_view_post')
can_create_post = Permission.objects.get(codename='can_create_post')
can_edit_post = Permission.objects.get(codename='can_edit_post')
can_delete_post = Permission.objects.get(codename='can_delete_post')

# Assign permissions to groups
editors_group.permissions.add(can_view_post, can_create_post, can_edit_post)
viewers_group.permissions.add(can_view_post)
admins_group.permissions.add(can_view_post, can_create_post, can_edit_post, can_delete_post)
