from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status = 'pulished')

class Post(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255)
    author = models.ForeignKey( User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='darft')

    class Meta:
        ordering = ('-publish',)


    def __str__(self):
        return self.title
    
    objects = models.Manager()
    published = PublishedManager()


posts = Post.objects.filter(status = 'published')
post = Post.published.all()