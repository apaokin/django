from django.conf.urls import url

from . import views
from first.views import *
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    url(r'^users\+from(?P<from1>[0-9]+)/$', views.user_index, name='user_index'),
    url(r'^players\+from(?P<from1>[0-9]+)/$', views.player_index, name='player_index'),
    url(r'^players/$', views.player_index, name='player_index'),
	url(r'^players\+team(?P<team_num>.+)/$', views.player_index, name='player_index'),   
    url(r'^player\+id=(?P<player_id>[0-9]+)/$', views.player_detail, name='player_detail'),
    url(r'^user\+username(?P<u_name>.+)/$', views.user_detail, name='user_detail'),
    url(r'^teams\+from(?P<from1>[0-9]+)/$', views.teams_index, name='teams_index'),
    url(r'^team\+id=(?P<t_id>.+)/$', views.team_detail, name='team_detail'),
    url(r'^my_login/$', views.my_login, name='my_login'),
    url(r'^accounts/profile/$', views.m_profile, name='my_login'),
    url(r'^tournaments\+from(?P<from1>[0-9]+)$', views.tourn_index, name='tourn_index'),
    url(r'^tournaments_j/$', views.tourn_json, name='tourn_json'),
    url(r'^tournaments_json\+from(?P<from1>[0-9]+)/$', views.tourn_index_json, name='tourn_index_json'),
    url(r'^tournament\+id(?P<num>[0-9]+)/$', views.tourn_detail, name='tourn_detail'),
    url(r'^tourn_top\+id(?P<num>[0-9]+)/$', views.tourn_ttd, name='tourn_ttd'),
    url(r'^create_post/$', views.post_change, name='post_create'),
    url(r'^create_tour/$', (staff_member_required) (TourCreate.as_view()), name='tour_create'),
    url(r'^edit_tour/(?P<id>[0-9]+)/$', (staff_member_required) (TourEdit.as_view()), name='tour_edit'),
    url(r'^handle_ajax_tour/$',  handle_ajax_tour, name='handle_ajax_tour'),
     url(r'^handle_ajax_like/$',  handle_ajax_like, name='handle_ajax_like'),
    # url(r'^create_ajax/$', (staff_member_required) (TournCreateAjax.as_view()), name='tour_create_ajax'),
    url(r'^create_post/(\d+)$', views.post_change, name='post_create'),
     url(r'^post_delete/(\d+)$', views.post_delete, name='post_delete'),
      url(r'^my_logout$', views.logout_view, name='my_logout'),
                
    
    

    url(r'^posts\+tag=(?P<num>.+)/$', views.start_pag, name='start_tag'),
    # url(r'^posts/$', views.start, name='start'),
     url(r'^$', views.start_pag, name='start_pag'),

] 
