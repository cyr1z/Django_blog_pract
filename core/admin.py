from django.contrib import admin
from .models import Post, Comment
from django.utils.html import format_html
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('created', 'title', 'short_text', 'comments_count', 'get_html_image')
    list_display_links = ('title', 'short_text', 'get_html_image')
    readonly_fields = ('slug', 'created', 'updated',)

    @staticmethod
    def get_html_image(obj):
        if obj.image:
            return format_html(f'<img src="/static/media/{obj.image}" height="60">')
        return format_html(f'<img src="/static/images/no_img.png" height="60">')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('created', 'post', 'username', 'short_text')
    list_display_links = ('post', 'username', 'short_text')
    readonly_fields = ('created', )

