from django.core.management.base import BaseCommand, CommandError
from django.db import migrations,transaction
from django.contrib.auth.models import User
from first.models import *
import MySQLdb
import time
import random
import datetime

class Command(BaseCommand):
	help = 'Closes the specified poll for voting'
	output_transaction= True
    
	def handle(self, *args, **options):
		t1 = time.time()
		N=100000
		my_file = open("/home/andrey/test/words.txt")
		my_string = my_file.read()
		words=my_string.split()
		for word in words:
			for letter in word:
				if letter < 'A' or letter >'z' or letter >'Z' and letter<'a':
					words.remove(word)
					break
		x=[]
		l_players=[]
		
		for i in range(N):
			x.append(User(username=random.choice(words)+str(i),
			email=random.choice(words) + "@mail.ru",
			password=random.choice(words)))
		User.objects.bulk_create(x)
		l_users=User.objects.all()


		x=[]
		l_team=[]
		
		
		N=len(l_users)
		
		for i in range(N//400+1):
			x.append(Tournament(name=random.choice(words)+str(i),platform='PC'
			))		
		Tournament.objects.bulk_create(x)		
		for i in range(N//20+1):
			
			l_team.append(Team(name=random.choice(words)+str(i)))	
		Team.objects.bulk_create(l_team)
		
		
		
		t_list=Team.objects.all()
		l_team=t_list.values_list('id', flat=True).order_by('id')
		tour_list=Tournament.objects.all()
		counter=0
		for i in t_list:
			i.tournam.add(tour_list.get(name=x[counter//20].name))
			counter=counter+1
		counter=0
		print (time.time() - t1)

		for i in l_users:
			if counter%20==0:

				l_players.append(Player(login='player'+str(i.id),
				platform='PC',
				user_id=i.id,team_id=l_team[counter//20],t_adm=1))
			else:
				l_players.append(Player(login='player'+str(i.id),
				platform='PC',
				user_id=i.id,team_id=l_team[counter//20]))
			counter=counter+1
		print("Before bulk\n")
		print (time.time() - t1)

		Player.objects.bulk_create(l_players)

		print (time.time() - t1)

		
		

		
	
