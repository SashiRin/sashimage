from django.db import models
from django.urls import reverse
from markdownx.models import MarkdownxField


class Post(models.Model):
    title = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=200, default="")
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    thumb = models.ImageField(upload_to='thumb/')
    image = models.ImageField(upload_to='image/')
    body = MarkdownxField()
    create_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
