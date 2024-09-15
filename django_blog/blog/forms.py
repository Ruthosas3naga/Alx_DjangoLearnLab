from django import forms
from .models import Comment, Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from taggit.forms import TagField, TagWidget 

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'placeholder': 'Enter your comment here'})

 # Import TagField and TagWidget


class PostForm(forms.ModelForm):
    # Use TagField with TagWidget to manage tags
    tags = TagField(
        required=False,
        widget=TagWidget(attrs={
            'placeholder': 'Add tags separated by commas',
            'class': 'form-control',
        })
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include tags in the form
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the title of the post'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write the post content here...'
            }),
        }

