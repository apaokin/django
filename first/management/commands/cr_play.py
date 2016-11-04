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
		x=User.objects.all()
		for i in x:
			
			
			
			l_players.append(Player(login='player'+str(i.id),
			platform='Real',
			user_id=i.id))
		print("Before bulk\n")
		Player.objects.bulk_create(l_players)

		print (time.time() - t1)
	
