from django.conf.urls import url

from . import views
from article.views import RSSFeed
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    # url(r'^test/$',views.test),
    url(r'^archives/$',views.archives,name='archives'),
    url(r'^aboutme/$',views.about_me,name='aboutme'),
    url(r'^tag(?P<tag>\w+)/$',views.search_tag,name='search_tag'),
    url(r'^search/$',views.blog_search,name='search'),
    url(r'^feed/$',RSSFeed(),name='RSS')
]
