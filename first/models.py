from django.db import models

class Player(models.Model):
	login = models.CharField("Логин",max_length=40,unique=True)
	first_name = models.CharField("Имя",max_length=40,blank=True)
	last_name = models.CharField("Фамилия",max_length=40,blank=True)
	Date_of_reg = models.DateField("Дата регистрации",editable=False,auto_now_add=True)

class Team(models.Model):
	name = models.CharField("Имя",max_length=40)
	Date_of_creation = models.DateField("Дата создания",auto_now_add=True)
	cap = models.ForeignKey(Player,default=None)

Player.team = models.ForeignKey(Team)
class Match(models.Model):
	first_team = models.ForeignKey(Team)
	second_team = models.ForeignKey(Team,related_name='+')
