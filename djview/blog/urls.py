from django.conf.urls import url
from .views import (post_model_list_view,post_model_detail_view,post_create,post_update,post_delete)
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^create$', post_create, name='create'),
    url(r'^$', post_model_list_view, name='list'),
    url(r'^about$', TemplateView.as_view(template_name='blog/about.html'), name='create'),
    url(r'^contact$', TemplateView.as_view(template_name='blog/contact.html'), name='create'),
    url(r'^(?P<id>\d+)/$',post_model_detail_view,name='detail'),
    url(r'^(?P<id>\d+)/edit/$',post_update,name='edit'),
    url(r'^(?P<id>\d+)/delete/$',post_delete,name='delete'),
]
