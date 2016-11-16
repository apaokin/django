from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.urls import *
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
import json


def user_index(request,from1):
	fr=int(from1)
	from2=fr+50;
	users=User.objects.all()[fr:from2]
	
	template = loader.get_template('first/user_index.html')
	context = {
		'prev' : fr-50,
        'users': users,
        'from': from2,
         
    }

	return HttpResponse(template.render(context, request))
def player_index(request,team_num="",from1="0"):
	fr=0
	from2=0
	
		#players=Player.objects.filter(team_id=team_num)
		
	
	fr=int(from1)
	from2=fr+50;
	players=Player.objects.all()[fr:from2]
	
	
	context = {
		'prev' : fr-50,
        'players': players,
        'from': from2,
         
    }

	return render(request,'first/player_index.html',context)
def teams_index(request,from1):
	fr=int(from1)
	from2=fr+50;
	teams=Team.objects.all()[fr:from2]
	
	
	context = {
		'prev' : fr-50,
        'teams': teams,
        'from': from2,
         
    }


	return render(request,'first/teams_index.html',context)

def tourn_index(request,from1):
	fr=int(from1)
	from2=fr+50;
	items=Tournament.objects.all()[fr:from2]
	
	
	context = {
		'prev' : fr-50,
        'items': items,
        'from': from2,
         
    }


	return render(request,'first/tourn_index.html',context)

def tourn_index_json(request,from1):
	fr=int(from1)
	from2=fr+10;
	items=Tournament.objects.all()[fr:from2]
	it=[]
	for item in items:
		it.append((item.id,item.name,item.platform))
	
	return HttpResponse(json.dumps(it), content_type='text/json')

def tourn_json(request):

	return render(request,'first/tourn_json.html')

def my_login(request):
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = NameForm(request.POST)
        # check whether it's valid:
		if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
			return HttpResponseRedirect('/list_users0')

    # if a GET (or any other method) we'll create a blank form
	else:
		form = NameForm()

	return render(request, 'my_login.html', {'form': form})
def player_detail(request,player_id):
	player = Player.objects.get(id=player_id)
	
	template = loader.get_template('first/player.html')
	context = {
        'player': player,
        
    }

	return HttpResponse(template.render(context, request))


def goal(item):
	return item[2]

def tourn_ttd(request,num):
	item = Tournament.objects.get(id=num)
	

	teams= item.team_set.all()
	players_ttd=[]

	for team in teams:

		players=team.player_set.filter(team_id=num)[:20]
		for player in players:
			goals=0
			matches=item.match_set.all()
			for match in matches:
				ttd=TTD_player.objects.get(player_id=player.id,match_id=match.id)
				goals=goals+ttd.goals
			players_ttd.append([player.login,player.team,goals])

	#players_ttd.sort(key=goal)
	i=1
	for ttd_item in players_ttd:
		ttd_item.insert(0,i) 
		i=i+1
	context = {
        'players_ttd': players_ttd,
        
        
    }
	
	return render(request,'first/tourn_top.html',context)
def post_change(request,*args):
	if args: 
		post=Post.objects.filter(id=args[0]).first()
		if not( post.author == request.user or request.user.is_staff):
			return render(request,'auth_error.html')
		to=reverse(post_change,args=[post.id])
	else: 
		post=Post()
		to=reverse(post_change)

	if request.method=='POST':
		
		form = PostForm(request.POST,instance=post)
		if form.is_valid():

			
			post_tags = form.cleaned_data['post_tags']
			tags_set=post_tags.split(';')
			post.author=request.user
			post.save()
			for item in tags_set:
				if item:
					tag=Tag.objects.filter(name=item).first()
					if not tag:
						tag=Tag(name=item)
						tag.save()
					post.tag.add(tag)
			
			post.save()
			return HttpResponseRedirect('')
	else:

		form = PostForm(instance=post)
		
	context = {
        'form': form,
        'to':to
        
    }
	
	return render(request,'first/post_form.html',context)
def func_for_sort(i):
	l=(i[1],i[2],i[3])
	return l	
def tourn_detail(request,num):
	
	item = Tournament.objects.get(id=num)
	teams= item.team_set.all()
	d=[]
	team_list=[]
	for team in teams:
		d.append([team.name,0,0,0])
		team_list.append(team.id)

	
	matches=Match.objects.filter(tourn=item)
	
	for match in matches:
		points=0

		points= (match.first_goals - match.second_goals >0)*3 + (match.first_goals - match.second_goals ==0) 
		k=team_list.index(match.first_team_id)
		d[k][1]=d[k][1]+ points
		d[k][2]=d[k][2]+ match.first_goals
		d[k][3]=d[k][3]+ match.second_goals
		points= (match.second_goals - match.first_goals >0)*3 + (match.second_goals - match.first_goals ==0) 
		k=team_list.index(match.second_team_id)
		d[k][1]=d[k][1]+ points
		d[k][2]=d[k][2]+ match.second_goals
		d[k][3]=d[k][3]+ match.first_goals
		
			
	d.sort(key=func_for_sort,reverse=True)
	
	template = loader.get_template('first/tourn.html')
	context = {
        'table': d,
        'item': item,
        
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
def team_detail(request,t_id):
	team = Team.objects.get(id=t_id)
	players = team.player_set.all()
	
	
	template = loader.get_template('first/team.html')
	context = {
         'players':players,
        'team': team,
        
    }
	return HttpResponse(template.render(context, request))
def m_profile(request):
	
	
	
	#template = loader.get_template('first/success.html')

	return render(request,'first/success.html')
def start(request,num=None):
	
	if num is not None:
		tag=Tag.objects.get(name=num)
		posts=tag.post_set.all().prefetch_related('tag')
	else:
		posts=Post.objects.all().prefetch_related('tag')
	
		
	
	#template = loader.get_template('first/success.html')
	context = {
         
        'posts': posts,
        
    }
	return render(request,'first/start.html',context)