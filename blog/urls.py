from django.urls import path
from .views import *

urlpatterns = [
    path('',IndexBlog.as_view(),name='blog'),
    path('detail/',BlogDetail.as_view(),name='blog-detail'),
]