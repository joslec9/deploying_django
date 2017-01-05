from django.conf.urls import url
from . import views

urlpatterns = {
    url(r'^$', views.index, name='index'),
    url(r'^sign-up$', views.sign_up),
    url(r'^login$', views.login),
    url(r'^account$', views.account, name='account'),
    url(r'^remove/(?P<id>\d+$)', views.remove),
    url(r'^logout$', views.logout),
    # url(r'^courses/add$', views.add),
    # url(r'courses/confirm_destroy/(?P<id>\d+$)', views.confirm_destroy),
    # url(r'courses/destroy/(?P<id>\d+$)', views.destroy)
}
