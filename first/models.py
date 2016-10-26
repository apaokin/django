from django.db import models
from django.contrib.auth.models import User 

class Player(models.Model):
	login = models.CharField(db_index=True,max_length=40)
	first_name = models.CharField(max_length=40,blank=True)
	last_name = models.CharField(max_length=40,blank=True)
	date_of_reg = models.DateField(editable=False,auto_now=True)
	PL_CHOICE = (
    	('PS3', 'PlayStation 3'),
    	('PS4', 'PlayStation 4'),
    	('XB', 'Xbox 360'),
	('PC', 'PC'),
	('Real', 'Real'),
	)
	POS_CHOICE = (
    	(0, 'Goalkeeper'),
    	(1, 'Central base'),
    	(2, 'Left base'),
	(3, 'Right base'),
	(4, 'Defending midfielder'),
	(5, 'Central midfielder'),
	(6, 'Left midfielder'),
	(7, 'Right midfielder'),
	(8, 'Atacking midfielder'),
	(9, 'Striker'),
	(10, 'Left forward'),
	(11, 'Right forward'),
	)
	position = models.IntegerField(choices=POS_CHOICE)
	platform = models.CharField(max_length=4,choices=PL_CHOICE)
	user = models.ForeignKey(User)
	image=models.ImageField(blank=True)
	
	class Meta:
		unique_together=("login","platform")
			
		






class Tournament(models.Model):
	name = models.CharField(db_index=True,max_length=40)
	first_place_rew=models.PositiveIntegerField(default=0)
	second_place_rew=models.PositiveIntegerField(default=0)
	straight_up=models.PositiveIntegerField(default=0)
	straight_down=models.PositiveIntegerField(default=0)
	third_place_rew=models.PositiveIntegerField(default=0)
	stik_up=models.PositiveIntegerField(default=0)
	stik_down=models.PositiveIntegerField(default=0)
	max_match=models.PositiveIntegerField()
	done=models.BooleanField(default=False)
	

class Team(models.Model):
	name = models.CharField(db_index=True,max_length=40)
	Date_of_creation = models.DateField(auto_now=True)
	cap = models.OneToOneField(Player,on_delete=models.PROTECT)
	tournam = models.ManyToManyField(Tournament, through='Table_item')
		

Player.team = models.ForeignKey(Team,on_delete=models.SET_NULL,null=True)	
class Table_item(models.Model):
	team = models.ForeignKey(Team)
	tournament = models.ForeignKey(Tournament)
	points=models.PositiveIntegerField(default=0)
	goal_scored=models.PositiveIntegerField(default=0)
	goal_missed=models.PositiveIntegerField(default=0)
	place=models.PositiveIntegerField(default=0)


	
		




class Match(models.Model):
	first_team = models.ForeignKey(Team)
	second_team = models.ForeignKey(Team,related_name='sec')
	tourn = models.ForeignKey(Tournament)
	date = models.DateTimeField(auto_now=True)
	first_goals=models.PositiveIntegerField(default=0)
	second_goals=models.PositiveIntegerField(default=0)
	tour=models.PositiveIntegerField(default=0)
	done=models.BooleanField(default=False)

class Event(models.Model):
	
	minute=models.PositiveIntegerField(default=0)
	name=models.CharField(max_length=40)
	match = models.ForeignKey(Match)
	
class Img(models.Model):
	image=models.ImageField()
	date = models.DateTimeField(editable=False,auto_now=True)
	match = models.ForeignKey(Match)
	
class TTD_player(models.Model):
	match = models.ForeignKey(Match)
	player = models.ForeignKey(Player)
	
	goals=models.PositiveIntegerField(default=0)
	assists=models.PositiveIntegerField(default=0)
	shots=models.PositiveIntegerField(default=0)
	shots_on_target=models.PositiveIntegerField(default=0)
	passes_try=models.PositiveIntegerField(default=0)
	passes=models.PositiveIntegerField(default=0)
	tackles=models.PositiveIntegerField(default=0)
	tackles_won=models.PositiveIntegerField(default=0)
	interceptions=models.PositiveIntegerField(default=0)
	saves=models.PositiveIntegerField(default=0)
	drib_try=models.PositiveIntegerField(default=0)
	drib=models.PositiveIntegerField(default=0)
	bend_try=models.PositiveIntegerField(default=0)
	bend=models.PositiveIntegerField(default=0)
	TTD=models.PositiveIntegerField(default=0)
	TTD_suc=models.PositiveIntegerField(default=0)
	POS_CHOICE = (
    	(0, 'Goalkeeper'),
    	(1, 'Central base'),
    	(2, 'Left base'),
	(3, 'Right base'),
	(4, 'Defending midfielder'),
	(5, 'Central midfielder'),
	(6, 'Left midfielder'),
	(7, 'Right midfielder'),
	(8, 'Atacking midfielder'),
	(9, 'Striker'),
	(10, 'Left forward'),
	(11, 'Right forward'),
	)
	position = models.IntegerField(choices=POS_CHOICE)
	own_goal=models.PositiveIntegerField(default=0)
	yellow=models.PositiveIntegerField(default=0)
	red=models.PositiveIntegerField(default=0)	
	
	rating_1=models.IntegerField()
	rating_2=models.IntegerField()
