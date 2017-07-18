
from django.conf.urls import url
from . import  views


# 视图函数命名空间
app_name = 'blogpj'
urlpatterns = [
    # name参数的值可作为处理函数index的别名，这里正则可改写为r'^$'
    url(r'^$', views.index, name='index'),
    # 搜索功能
    url(r'^search/$', views.search, name='search'),
    # (?P<pk>[0-9]+)表示命名捕获组，作用是从用户访问的URL里把括号内匹配的字符串捕获并作为关键字参数传给其对应的视图函数detail
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category')
]