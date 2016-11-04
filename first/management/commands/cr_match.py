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

		tourn=Tournament.objects.first()
		z=tourn.team_set.all()
		l_goals=[]
		
		l_match=[]
		l_first=[]
		l_second=[]
		l_ttd=[]
		for i in range(19*20*22):
			l_goals.append(random.randint(0,2))
		print("before match")
		for i in range(20):
			for j in range(20):
				sum1=0
				sum2=0
				if i!=j:
					for k in range(11):
						sum1=l_goals[i*20*19 +j*22+k ] + sum1
						sum2=l_goals[i*20*19 +j*22+k+11 ] + sum2
				
					l_match.append(Match(first_team_id=z[i].id,second_team_id=z[j].id,tourn_id=tourn.id,first_goals=sum1,second_goals=sum2))
		print("before bulk")
		Match.objects.bulk_create(l_match)
		l_match=Match.objects.filter(tourn_id=tourn.id).order_by('id')
		for i in range(20):
			#print("i= "+str(i))
			for j in range(19):
			#	print(j)
				l_first=l_match[i*19+j].first_team.player_set.all()
				l_second=l_match[i*19+j].second_team.player_set.all()
				for k in range(11):
					
					l_ttd.append(TTD_player(player_id=l_first[k].id,match_id=l_match[i*19+j].id,goals=l_goals[i*20*19 +j*22+k ],position=k))
					l_ttd.append(TTD_player(player_id=l_second[k].id,match_id=l_match[i*19+j].id,goals=l_goals[i*20*19 +j*22+k+11 ],position=k))
		print("before bulk")
		TTD_player.objects.bulk_create(l_ttd)


		
		print (time.time() - t1)

		
		

		
	
 
