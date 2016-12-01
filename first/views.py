from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.urls import *
from django.http import HttpResponseRedirect,JsonResponse
from .models import *
from .forms import *
import json
from django.views.decorators.http import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import *
from django.contrib.auth import logout
from cent import Client



def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

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
	form=TourFormIndex()
	cat=request.POST.get('z')

	fr=int(from1)
	from2=fr+50;
	if not cat:
		items=Tournament.objects.all()[fr:from2]
	else:
		items=Tournament.objects.filter(platform=cat)[fr:from2]
	
	
	context = {
		'prev' : fr-50,
        'items': items,
        'from': from2,
        'form': form,
         
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


def t(request,from1):
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


class TourCreate(CreateView):
    model = Tournament
    template_name_suffix='_create'
    fields = ['platform', 'name', 'first_place_rew', 'second_place_rew', 'third_place_rew']

class TourEdit(UpdateView):
    model = Tournament
    template_name_suffix='_edit'

    fields = ['platform', 'name', 'first_place_rew', 'second_place_rew', 'third_place_rew']
    def get_object(self, queryset=None):
    	self.my_id=self.kwargs['id']
    	obj = Tournament.objects.get(id=int(self.kwargs['id']))
    	return obj
    
def handle_ajax_tour(request):
	if request.method == 'POST':
		
		errors=[]
		my_id=request.POST.get('my_id')
		if my_id:
			form=TourForm(request.POST,instance=Tournament.objects.get(id=int(my_id)))
		else:
			form= TourForm(request.POST);

		if form.is_valid():
			form.save()
			if my_id:
				errors="Турнир успешно отредактирован"
			else:
				errors="Турнир успешно создан"

		else:
			#post_text = json.dumps([(k, [e for e in v]) for k, v in form.errors.items()])
		
			
			l=[]
			for k,v in form.errors.items():
				l=[]
				l.append(k);
				for e in v:
					l.append(e);
				errors.append(l);

			#print(errors)

			
		return HttpResponse(
            json.dumps(errors),
            content_type="application/json")
        
	



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
		print(request.POST)
		
		form = PostForm(request.POST,instance=post)
		if form.is_valid():

			
			post_tags = form.cleaned_data['post_tags']
			tags_set=post_tags.split(';')
			post.author=request.user
			if args:
				post.tag.clear()
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
@require_POST
def post_delete(request,*args):
	post=Post.objects.get(id=args[0])
	if not( post.author== request.user or request.user.is_staff):
		return render(request,'auth_error.html')
	#post.delete()
	return render(request,'success.html')


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
		posts=tag.post_set.prefetch_related('tag')
	else:
		posts=Post.objects.prefetch_related('tag')
	posts=posts.select_related('author')	
		
	
	#template = loader.get_template('first/success.html')
	context = {
         
        'posts': posts,
        
    }
	return render(request,'first/start.html',context)

def handle_ajax_like(request,num=None):
	if request.method=="GET":

		likes=[]
		for item in Like.objects.filter(bel=request.user.id):
				likes.append(item.object_id)
		return HttpResponse(
    json.dumps(likes),
            content_type="application/json")	
	else:
		

		url = "http://localhost:7000/"
		secret_key = "secret"

# initialize client instance.
		client = Client(url, secret_key, timeout=1)

# publish data into channel
		channel = "like-updates"
		data = {"input": "test"}
		client.publish(channel, data)
		post_id=request.POST.get('post_id');
		like=Like.objects.filter(object_id=post_id,bel=request.user.id).first()
		if like:
			like.delete()
			return HttpResponse(
    json.dumps("delete"),
            content_type="application/json")
		else:
			like=Like(content_object=Post.objects.get(id=post_id),bel=request.user)
			like.save()
			return HttpResponse(
    json.dumps("create"),
            content_type="application/json")


def start_pag(request,num=None):
		


	if num is not None:
		tag=Tag.objects.get(name=num)
		posts=tag.post_set.prefetch_related('tag')
	else:
		posts=Post.objects.prefetch_related('tag')
	posts=posts.prefetch_related('likes')
	posts=posts.select_related('author')	
	
	
	if request.is_ajax():
		likes=[]
		for post in posts:
			likes.append((post.id,post.likes.count()))
		return HttpResponse(
            json.dumps(likes),
            content_type="application/json")	
	
	#template = loader.get_template('first/success.html')
	
	paginator = Paginator(posts, 5) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		items = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		items = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		items = paginator.page(paginator.num_pages)

	context = {
         
        'items': items,
        
    }
	
	return render(request,'first/start_tag.html',context)