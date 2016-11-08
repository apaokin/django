from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list_users(?P<from1>[0-9]+)/$', views.index, name='index'),
    url(r'^player(?P<player_id>[0-9]+)/$', views.player_detail, name='player_detail'),
    url(r'^user(?P<u_name>.+)/$', views.user_detail, name='user_detail'),
] 
