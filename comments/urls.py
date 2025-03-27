from django.urls import path
from . import views


urlpatterns = [
    path('posts/<slug:post_slug>/comments/', views.CommentListCreateView.as_view(), name='comment_list'),
]