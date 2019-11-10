from . views import index, article
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('', index, name='index', ),
    path('posts/', index, name='posts', ),
    path('posts/<slug:article_slug>', article, name='post'),
]
