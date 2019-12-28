from django.urls import path
from .views import NewsListView, NewsAddView, NewsStatisticsView, get

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('news_add/', NewsAddView.as_view(), name='news_add'),
    path('news_detail/<int:pk>/', get, name='news_detail'),
    path('news_statistics/', NewsStatisticsView.as_view(), name='news_statistics')

]