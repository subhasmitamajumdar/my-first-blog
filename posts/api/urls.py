from django.conf.urls import url
from posts.api.views import (PostListAPIView, PostDetailAPIView, PostUpdateAPIView, PostDeleteAPIView, PostCreateAPIView)

urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='list'),
    url(r'^create/$', PostCreateAPIView.as_view(), name='create'),
    url(r'^(?P<slug>[-\w]+)/$', PostDetailAPIView.as_view(), name='details'),
    url(r'^(?P<slug>[-\w]+)/edit/$', PostUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<slug>[-\w]+)/delete/$', PostDeleteAPIView.as_view(), name='delete'),
]