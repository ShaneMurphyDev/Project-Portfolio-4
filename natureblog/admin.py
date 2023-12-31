from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

#  Admin Post register
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')

# Admin Comment register
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    search_fields = ('name', 'email', 'body')
    list_filter = ('approved', 'created_on')
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    actions = ['approved_comments']

    def approved_comments(self, request, queryset):
        queryset.update(approved=True)
