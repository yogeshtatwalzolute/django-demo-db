"""
Run with: python manage.py shell < seed_data.py
"""
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from django.utils import timezone
from blog.models import Category, Post, Comment

# Superuser
if not User.objects.filter(username='admin').exists():
    admin = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Created superuser: admin / admin123')
else:
    admin = User.objects.get(username='admin')

# Categories
tech, _ = Category.objects.get_or_create(name='Technology', defaults={'description': 'Tech articles'})
life, _ = Category.objects.get_or_create(name='Lifestyle', defaults={'description': 'Life tips'})
django_cat, _ = Category.objects.get_or_create(name='Django', defaults={'description': 'Django framework posts'})

# Posts
posts_data = [
    {
        'title': 'Getting Started with Django and PostgreSQL',
        'body': (
            'Django is a high-level Python web framework that encourages rapid development. '
            'When paired with PostgreSQL, you get a powerful, production-ready stack.\n\n'
            'PostgreSQL offers advanced features like JSONB fields, full-text search, '
            'and excellent performance for complex queries — all accessible directly through Django ORM.'
        ),
        'category': django_cat,
        'status': Post.STATUS_PUBLISHED,
        'published_at': timezone.now(),
    },
    {
        'title': 'Django ORM: Queries You Should Know',
        'body': (
            'The Django ORM provides a rich API for database interaction. '
            'Key methods include filter(), exclude(), annotate(), aggregate(), and select_related().\n\n'
            'Understanding these unlocks efficient database access without raw SQL in most cases.'
        ),
        'category': django_cat,
        'status': Post.STATUS_PUBLISHED,
        'published_at': timezone.now(),
    },
    {
        'title': 'Why PostgreSQL for Production?',
        'body': (
            'PostgreSQL is the world\'s most advanced open-source relational database. '
            'It supports ACID transactions, complex joins, window functions, and JSON natively.\n\n'
            'For Django projects, it is the recommended database for production workloads.'
        ),
        'category': tech,
        'status': Post.STATUS_PUBLISHED,
        'published_at': timezone.now(),
    },
    {
        'title': 'Draft Post: Upcoming Features',
        'body': 'This post is still a draft and won\'t appear on the public listing.',
        'category': life,
        'status': Post.STATUS_DRAFT,
        'published_at': None,
    },
]

for data in posts_data:
    if not Post.objects.filter(title=data['title']).exists():
        post = Post.objects.create(author=admin, **data)
        print(f'Created post: {post.title}')

# Comments on first post
first_post = Post.objects.filter(status=Post.STATUS_PUBLISHED).first()
if first_post and not first_post.comments.exists():
    Comment.objects.create(
        post=first_post,
        author_name='Alice',
        author_email='alice@example.com',
        body='Great introduction! Really helped me set up my first Django + Postgres project.',
    )
    Comment.objects.create(
        post=first_post,
        author_name='Bob',
        author_email='bob@example.com',
        body='Would love to see a follow-up on using Docker with this stack.',
    )
    print(f'Added comments to: {first_post.title}')

print('\nSeed complete.')
print('Admin login: http://127.0.0.1:8000/admin/  (admin / admin123)')
