from .models import Comment
from django import forms
from .models import Post

# Form for creating a post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'featured_image', 'excerpt', 'content', 'status']

# Form for leaving A comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)