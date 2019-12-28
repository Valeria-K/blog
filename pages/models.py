from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)
    author = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def  get_absolute_url(self):
        return reverse('news_list')

