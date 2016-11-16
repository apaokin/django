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
		team=Team.objects.all().first()
		l=Match.objects.filter(first_team=team)
		ex_post=Post.objects.filter(id=18).first()
		form = PostForm(instance=ex_post)
		form2 = PostForm(instance=Post("dd","dd"))
		z=form2.save(commit=False)
		print()
		tournam=Tournament.objects.all()
		#print(dir(Player))
		#print(dir(User))
		counter=0
		t=Tag.objects.all()
		for item in tournam:
			counter=counter+1
		
		print(counter)
		
		

		#t.delete()#print(Tag.objects.all())
		#l.delete()
		#l2.delete()
		#l3.delete()


    
	
