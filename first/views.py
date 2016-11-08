from django.http import HttpResponse
from django.template import loader
from .models import *

def index(request,from1):
	fr=int(from1)
	from2=fr+50;
	users=User.objects.all()[fr:from2]
	
	template = loader.get_template('first/index.html')
	context = {
		'prev' : fr-50,
        'users': users,
        'from': from2,
         
    }
	return HttpResponse(template.render(context, request))
def player_detail(request,player_id):
	player = Player.objects.get(id=player_id)
	
	template = loader.get_template('first/player.html')
	context = {
        'player': player,
        
    }
	return HttpResponse(template.render(context, request))
def user_detail(request,u_name):
	user = User.objects.get(username=u_name)
	players= user.player_set.all()
	#am=request.user.is_authenticated
	template = loader.get_template('first/user.html')
	context = {
        'user': user,
        'players': players,
        
    }
	return HttpResponse(template.render(context, request))
	