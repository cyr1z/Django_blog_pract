from django.shortcuts import render
from .models import Post, Comment
# Create your views here.


def article(request, article_slug):
    post = Post.objects.filter(slug=article_slug).first()
    comments = Comment.objects.filter(post=post)
    ctx = {'post': post, 'comments': comments}
    return render(request, 'core/blog-single.html', ctx)


def index(request):
    posts = Post.objects.all().order_by('-created')
    posts_count = Post.get_posts_count()
    ctx = {'posts': posts, 'posts_count': posts_count}
    return render(request, 'core/category.html', ctx)
