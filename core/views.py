from django.shortcuts import render
from django.http import  Http404, HttpResponseRedirect
from  django.urls import  reverse
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


def leavecomment(request, article_slug):
    post = Post.objects.filter(slug=article_slug).first()
    post.comment_set.create(
        username=request.POST['name'],
        text=request.POST['text'])
    return article(request, article_slug)
