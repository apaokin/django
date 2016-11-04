from django.core.management.base import BaseCommand, CommandError
from django.db import migrations,transaction
from django.contrib.auth.models import User
from django.db import connection
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
		
		my_file = open("/home/andrey/test/words.txt")
		my_string = my_file.read()
		words=my_string.split()
		for word in words:
			for letter in word:
				if letter < 'A' or letter >'z' or letter >'Z' and letter<'a':
					words.remove(word)
					break
		x=[]
		l_team=[]
		real_id=[]
		pl_list=Player.objects.all()
		N=len(pl_list)
		
		for i in range(N//400+1):
			x.append(Tournament(name=random.choice(words)+str(i),platform='Real'
			))
			
		Tournament.objects.bulk_create(x)
		
		real_id=pl_list.filter(platform='Real').values_list('id', flat=True).order_by('id')
		
		for i in range(N//20+1):
			
			l_team.append(Team(name=random.choice(words)+str(i)))
			
		Team.objects.bulk_create(l_team)

		
		real_up=[]
		counter=0;
		
		t_list=Team.objects.all()
		tour_list=Tournament.objects.all()
		
		for i in t_list:
			i.tournam.add(tour_list.get(name=x[counter//20].name))
			counter=counter+1

		t=t_list.values_list('id', flat=True).order_by('id')
		print (time.time() - t1)
		counter=0
		
		for i in real_id:
			
			if counter % 20==0:
				
				real_up.append((t[counter//20],1,i))
			else:	
				real_up.append((t[counter//20],0,i))
			counter=counter+1	
		print("ZZZZZZ")
		with connection.cursor() as cursor:
		
			cursor.executemany("""UPDATE first_player
SET team_id=%s, t_adm=%s
WHERE id=%s AND platform='Real'; """,real_up)



	

		print (time.time() - t1)
	
