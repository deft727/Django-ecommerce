from django.urls import path
from .views import *

urlpatterns = [
    path('',IndexBlog.as_view(),name='blog'),
    path('post/<str:slug>/',BlogDetail.as_view(),name='post'),
    path('category/<str:slug>/',PostsByCategory.as_view(),name='category'),
    path('tag/<str:slug>/',PostsByTag.as_view(),name='tag'),
    path('searchblog/',Search.as_view(),name='search'),

]