from django.core.management.base import BaseCommand, CommandError
from django.db import migrations,transaction
from django.contrib.auth.models import User
from first.models import *
import MySQLdb
import time
import random
import datetime
from django.db import connection

class Command(BaseCommand):
	help = 'Closes the specified poll for voting'
	output_transaction= True
   
	def handle(self, *args, **options):
		
		l=Match.objects.all()
		l2=TTD_player.objects.all()[:50000000]
		l3=Event.objects.all()
		#print(dir(Player))
		print(dir(User))
		
		ob=l.get(id=5681)
		print(ob.check_goals())
		#l.delete()
		#l2.delete()
		#l3.delete()


    
	
