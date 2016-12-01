from django.core.management.base import BaseCommand, CommandError
from django.db import migrations,transaction
from django.contrib.auth.models import User
from first.models import *
from first.forms import *
import MySQLdb
import time
import random
import datetime
from django.db import connection

class Command(BaseCommand):
	help = 'Closes the specified poll for voting'
	output_transaction= True
   
	def handle(self, *args, **options):
		team=Team.objects.first()
		p=Post.objects.all()
		user=User.objects.first()
		for post in p:
			t=Like(content_object=post,bel=user)
			t.save()

		#print(dir(Player))
		#print(dir(User))
		
		
		
		

		#t.delete()#print(Tag.objects.all())
		#l.delete()
		#l2.delete()
		#l3.delete()


    
	
