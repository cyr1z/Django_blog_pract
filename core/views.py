from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from  django.urls import reverse
from .models import Post, Comment
# Create your views here.


def article(request, article_slug):
    ctx = {}
    try:
        post = Post.objects.filter(slug=article_slug).first()
        ctx['post'] = post
    except:
        raise Http404("Публікацію не знайдено")
    comments = Comment.objects.filter(post=post)
    ctx['comments'] = comments
    return render(request, 'core/blog-single.html', ctx)


def index(request):
    ctx = {}
    try:
        posts = Post.objects.all().order_by('-created')
        ctx['posts'] = posts
    except:
        raise Http404("Публікацію не знайдено")
    posts_count = Post.get_posts_count()
    ctx['posts_count'] = posts_count
    return render(request, 'core/category.html', ctx)


def leave_comment(request, article_slug):
    post = Post.objects.filter(slug=article_slug).first()
    post.comment_set.create(
        username=request.POST['username'],
        text=request.POST['text'])
    return HttpResponseRedirect(reverse('core:post', args=(post.slug,)))
