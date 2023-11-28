from . import views
from django.urls import path
from .views import create_post, AboutView, custom_404

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path("", views.PostList.as_view(), name="home"),
    path('index.html/', views.IndexView.as_view(), name='index.html'),
    path('create/', create_post, name='create_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/edit/', views.PostUpdate.as_view(), name='post_edit'),
    path('<slug:slug>/delete/', views.PostDelete.as_view(), name='post_delete'),
]