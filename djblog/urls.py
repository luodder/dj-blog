from django.conf.urls import url
from djblog import views

urlpatterns = [
    url(r'^djblog/$', views.IndexView.as_view(), name='index'),
    url(r'^djblog/article/(?P<article_id>\d+)$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^djblog/category/(?P<article_id>\d+)$', views.CategoryView.as_view(), name='category'),

]