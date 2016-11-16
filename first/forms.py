from django import forms
from django.forms import ModelForm
from first.models import *
class NameForm(forms.Form):
    your_name = forms.CharField(label='Bv:', max_length=100)
    your_pass = forms.CharField(label='Пароль:', max_length=100)

class PostForm(ModelForm):
	post_tags=forms.CharField(label='теги(через ;)',max_length=100,required=False)
	class Meta:
		model = Post 
		fields = ['title', 'content']
	def __init__(self,*args,**kwargs):
		instance = kwargs.get('instance',None)#kwargs.pop('instance', None)
		
		if not instance._state.adding:
			tags=instance.tag.all()
			post_tags=""
			for tag in tags:
				post_tags=post_tags +";"+str(tag)
			self.post_tags=post_tags
			
	
		super(PostForm, self).__init__(*args,**kwargs)
	
