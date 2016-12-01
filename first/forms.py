from django import forms
from django.forms import ModelForm
from first.models import *
from django.http import *
import json
from django.views.generic import FormView



class AjaxFormMixin(FormView):

   
    def form_valid(self, form):
        form.save()
        return HttpResponse('OK')

    def form_invalid(self, form):
        errors_dict = json.dumps(dict([(k, [e for e in v]) for k, v in form.errors.items()]))
        return HttpResponseBadRequest(json.dumps(errors_dict))


class TourFormIndex(forms.Form):
   

    z=forms.ChoiceField(label='Выберите категорию',widget=forms.Select, choices=Tournament.PL_CHOICE)


class TourForm(ModelForm):
	def clean(self):
		cleaned_data=super(TourForm,self).clean()
		return cleaned_data
	class Meta:
		model = Tournament 
		fields = ['platform', 'name', 'first_place_rew', 'second_place_rew', 'third_place_rew']

class PostForm(ModelForm):
	post_tags=forms.CharField(label='теги(через ;)',max_length=100,required=False)
	class Meta:
		model = Post 
		fields = ['title', 'content']
	def __init__(self,*args,**kwargs):
		instance = kwargs.get('instance',None)
		post_tags=""
		if not instance._state.adding:
			tags=instance.tag.all()
			
			for tag in tags:
				post_tags=post_tags +str(tag) +";"	
		
		super(PostForm, self).__init__(*args,**kwargs)
		self.fields['post_tags'].initial=post_tags	
	
