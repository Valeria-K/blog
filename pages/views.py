from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from .models import Post


class NewsListView(ListView):
    model = Post
    template_name = 'news_list.html'


class NewsAddView(CreateView):
    model = Post
    template_name = 'news_add.html'
    fields = '__all__'


class NewsDetailView(DetailView):
    model = Post
    template_name = 'news_detail.html'


class NewsStatisticsView(TemplateView):
    template_name = 'news_statistics.html'

