from . views import index, article, leave_comment
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('', index, name='index', ),
    path('posts/', index, name='posts', ),
    path('posts/<slug:article_slug>', article, name='post'),
    path('posts/<slug:article_slug>/leave_comment', leave_comment, name='leave_comment'),
]
