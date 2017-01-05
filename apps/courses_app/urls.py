from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^add$', views.add),
    url(r'^confirm_destroy/(?P<id>\d+$)', views.confirm_destroy),
    url(r'^destroy/(?P<id>\d+$)', views.destroy),
    url(r'^assign_user$', views.assign_user )
]
