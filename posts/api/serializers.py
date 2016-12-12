from rest_framework.serializers import (ModelSerializer,
                                        HyperlinkedIdentityField,
                                        SerializerMethodField)
from posts.models import Post
from comments.models import Comment
class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content','publish',]

post_detail_url = HyperlinkedIdentityField(
        view_name="posts-api:details",
        lookup_field="slug"
    )
from comments.api.serializers import CommentSerializer

class PostDetailSerializer(ModelSerializer):
    user = SerializerMethodField()
    url = post_detail_url
    image = SerializerMethodField()
    comments = SerializerMethodField()
    class Meta:
        model = Post
        fields = ['url','user', 'title', 'slug', 'content','publish','image','comments']

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None

        return image

    def get_user(self, obj):
        return str(obj.user.username)

    def get_comments(self, obj):
        content_type = obj.get_content_type
        object_id = obj.id
        c_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentSerializer(c_qs, many=True).data
        return comments


class PostListSerializer(ModelSerializer):
    user = SerializerMethodField()
    url = post_detail_url
    class Meta:
        model = Post
        fields = ['url', 'user', 'title', 'content','publish']

    def get_user(self, obj):
        return str(obj.user.username)


