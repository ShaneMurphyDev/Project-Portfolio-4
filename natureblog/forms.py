from .models import Comment
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'featured_image', 'excerpt', 'content', 'status']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)