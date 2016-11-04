from django.db import models
from django.contrib.auth.models import User 

class Player(models.Model):
	login = models.CharField(db_index=True,max_length=40)
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
	position = models.IntegerField(choices=POS_CHOICE,blank=True,null=True)
	platform = models.CharField(max_length=4,choices=PL_CHOICE)
	user = models.ForeignKey(User)
	image=models.ImageField(blank=True,null=True)
	team = models.ForeignKey('Team',on_delete=models.SET_NULL,null=True,blank=True)
	t_adm=models.BooleanField(default=0)
	def __str__(self):
		return self.login 
	
	class Meta:
		unique_together=("login","platform")
			







class Tournament(models.Model):
	PL_CHOICE = (
    ('PS3', 'PlayStation 3'),
    ('PS4', 'PlayStation 4'),
    ('XB', 'Xbox 360'),
	('PC', 'PC'),
	('Real', 'Real'),
	)
	platform = models.CharField(max_length=4,choices=PL_CHOICE)
	name = models.CharField(unique=True,max_length=40)
	first_place_rew=models.PositiveIntegerField(default=0)
	second_place_rew=models.PositiveIntegerField(default=0)
	straight_up=models.PositiveIntegerField(default=0)
	straight_down=models.PositiveIntegerField(default=0)
	third_place_rew=models.PositiveIntegerField(default=0)
	stik_up=models.PositiveIntegerField(default=0)
	stik_down=models.PositiveIntegerField(default=0)
	done=models.BooleanField(default=False)
	

class Team(models.Model):
	name = models.CharField(db_index=True,max_length=40)
	Date_of_creation = models.DateField(auto_now=True)
	tournam = models.ManyToManyField(Tournament)
	group=models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.name


	#	

	


	
		




class Match(models.Model):
	first_team = models.ForeignKey(Team)
	second_team = models.ForeignKey(Team,related_name='sec')
	tourn = models.ForeignKey(Tournament)
	date = models.DateTimeField(auto_now=True)
	first_goals=models.PositiveIntegerField(default=0)
	second_goals=models.PositiveIntegerField(default=0)
	tour=models.PositiveIntegerField(default=0)
	done=models.BooleanField(default=False)
	play_off=models.PositiveIntegerField(default=0)


	def check_goals(self):
		sum1=0
		sum2=0
		l=TTD_player.objects.filter(match_id=self.id)
		for i in l:
			if i.player.team_id==self.first_team_id:
				sum1=sum1+i.goals
			else:
				sum2=sum2+i.goals

		return( sum1==self.first_goals and sum2==self.second_goals)
		
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
	
	rating_1=models.IntegerField(default=5)
	rating_2=models.IntegerField(default=5)
