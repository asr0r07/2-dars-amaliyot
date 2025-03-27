from django.urls import path
from . import views


urlpatterns = [
    path('tags/', views.TagListCreateView.as_view(), name='tag_list'),
    path('tags/<slug:tag_slug>/posts/', views.TagDetailView.as_view(), name='tag_detail'),
]