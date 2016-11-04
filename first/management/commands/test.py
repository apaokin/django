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
		ob=l.get(id=2641)
		print(ob.check_goals())
		#l.delete()


    
	
