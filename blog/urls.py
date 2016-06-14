"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from rest_framework import routers

from blogpost.serializers import BlogpostSet
from blogpost.sitemaps.sitemaps import PageSitemap,FlatPagesSitemap,BlogSitemap
from blogpost.views import index,view_post
from djblog.views import IndexView as djIndexView

"""
urlpatterns = ['',
    url(r'^$', index,name='main'),
    url(r'^blog/(?p<slug>[^\.]+).html', view_post),
    url(r'^admin/', include(admin.site.urls)),
]
"""

apiRouter = routers.DefaultRouter()
apiRouter.register(r'blogpost', BlogpostSet)

sitemaps = {
    "page":PageSitemap,
    "flatpages":FlatPagesSitemap,
    "blog":BlogSitemap
}

urlpatterns = [
    url(r'^$', index, name='main'),
    url(r'^blog/(?P<slug>[^\.]+).html', view_post, name='view_blog_post'),
    url(r'^admin/',admin.site.urls),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(apiRouter.urls)),
    url(r'^djblog/', include('djblog.urls',namespace = 'djblog', app_name = 'djblog')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

