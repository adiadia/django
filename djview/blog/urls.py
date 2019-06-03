from django.conf.urls import url
from .views import (post_model_list_view,post_model_detail_view,post_create,post_update,post_delete,DashboardTemplateView,PostDetail,PostList)
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^create$', post_create, name='create'),
    url(r'^$', PostList.as_view(), name='list'),
    url(r'postdetail/(?P<slug>[-\w]+)/$', PostDetail.as_view(), name = 'detail'),
    url(r'^about$', DashboardTemplateView.as_view(), name='create'),
    url(r'^contact$', TemplateView.as_view(template_name='blog/contact.html'), name='create'),
    url(r'^(?P<id>\d+)/$',post_model_detail_view,name='detail'),
    url(r'^(?P<id>\d+)/edit/$',post_update,name='edit'),
    url(r'^(?P<id>\d+)/delete/$',post_delete,name='delete'),
]
