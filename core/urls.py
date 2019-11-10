from . views import index, article
from django.urls import path

urlpatterns = [
    path('', index, name='index', ),
    path('posts/', index, name='index', ),
    path('posts/<slug:article_slug>', article, name='article'),
]
