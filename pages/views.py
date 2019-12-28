from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from .models import Post


class NewsListView(ListView):
    model = Post
    template_name = 'news_list.html'


class NewsAddView(CreateView):
    model = Post
    template_name = 'news_add.html'
    fields = ['title', 'text', 'author', 'tags']


class NewsDetailView(DetailView):
    model = Post
    template_name = 'news_detail.html'


def get(request, pk):
    post = Post.objects.get(pk=pk)
    post.views += 1
    post.save()
    return render(request, "news_detail.html", {'post': post})


class NewsStatisticsView(ListView):
    template_name = 'news_statistics.html'
    model = Post
    queryset = Post.objects.all().order_by('-views')



