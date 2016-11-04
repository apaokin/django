from django.core.management.base import BaseCommand, CommandError
from django.db import migrations,transaction
from django.contrib.auth.models import User
import MySQLdb
import time
import random
import datetime
from first.models import *

class Command(BaseCommand):
	help = 'Closes the specified poll for voting'

    
	def handle(self, *args, **options):
		user = User.objects.exclude(username="root")
		player=Player.objects.all()
		te=Tournament.objects.all()
		t=Team.objects.all()
		matches=Match.objects.all()
		ttd=TTD_player.objects.all()
		
		user.delete()
		player.delete()
		te.delete()
		t.delete()
		ttd.delete()
		matches.delete()
	
 
