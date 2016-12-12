from django.contrib import admin

# Register your models here.
from posts.models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ("title","__unicode__","update","timestamp")
    list_display_links = ("title","update","timestamp")
    list_filter = ("timestamp","update")
    search_fields = ("title","content")
    class Meta:
        model=Post

admin.site.register(Post,PostModelAdmin)