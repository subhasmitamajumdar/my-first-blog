from django.conf.urls import url
from comments.api.views import CommentListAPIView, CommentDetailAPIView

urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name='thread'),
]