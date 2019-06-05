from django.conf.urls import url
from .views import (post_model_list_view,
                    post_model_detail_view,
                    post_create,
                    post_update,
                    post_delete,
                    searchform,
                    DashboardTemplateView,
                    PostDetail,PostList,PostCreate,PostUpdate,PostDelete)

urlpatterns = [
    #url(r'^create$', post_create, name='create'),
    url('form1',searchform,name='searchform'),
    url(r'^$', PostList.as_view(), name='list'),
    url(r'edit/(?P<slug>[-\w]+)/$',PostUpdate.as_view(),name='edit'),
    url(r'^postcreate$', PostCreate.as_view(), name='create'),
    url(r'postdetail/(?P<slug>[-\w]+)/$', PostDetail.as_view(), name = 'detail'),
    url(r'^about$', DashboardTemplateView.as_view(), name='create'),
    #url(r'^contact$', TemplateView.as_view(template_name='blog/contact.html'), name='create'),
    #url(r'^(?P<id>\d+)/$',post_model_detail_view,name='detail'),
    #url(r'^(?P<id>\d+)/edit/$',post_update,name='edit'),
    #url(r'^(?P<id>\d+)/delete/$',post_delete,name='delete'),
    url(r'delete/(?P<slug>[-\w]+)/$', PostDelete.as_view(), name='delete'),
]
