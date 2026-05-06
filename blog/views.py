from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category, Comment


def post_list(request):
    posts = Post.objects.filter(
        status=Post.STATUS_PUBLISHED,
        published_at__lte=timezone.now()
    ).select_related('author', 'category')
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'categories': categories,
    })


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(
        Post,
        slug=slug,
        status=Post.STATUS_PUBLISHED,
        published_at__year=year,
        published_at__month=month,
        published_at__day=day,
    )
    comments = post.comments.filter(active=True)
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
    })


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(
        status=Post.STATUS_PUBLISHED,
        published_at__lte=timezone.now()
    ).select_related('author')
    return render(request, 'blog/category_posts.html', {
        'category': category,
        'posts': posts,
    })
