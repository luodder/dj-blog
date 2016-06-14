from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.dates import DateDetailView
from djblog.models import Article, Category

import markdown2

class IndexView(ListView):
    template_name = "index.html"
    context_object_name = "article_list"

    def get_queryset(self):
        article_list = Article.objects.filter(status='p')
        for article in article_list:
            article.body = markdown2.markdown(article.body,)
        return article_list
    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(IndexView,self).get_context_data(**kwargs)



class ArticleDetailView(DateDetailView):
    model = Article

    template_name = 'index.html'

    context_object_name = 'article'

    pk_url_kwarg = 'article_id'

    def get_object(self, queryset=None):
        obj = super(ArticleDetailView,self).get_object()
        obj.body = markdown2.markdown(obj.body)
        return obj

class CategoryView(ListView):

    template_name = 'index.html'
    context_object_name = 'article_list'

    def get_queryset(self):

        article_list = Article.objects.filter(category = self.kwargs['cate_id'], status = 'p')

        for article in article_list:
            article.body = markdown2.markdown(article.body,)
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(CategoryView, self).get_context_data(**kwargs)
