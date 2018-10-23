from django import forms
from .models import User,Event



class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['name',
					'gender',
					'branch',
					'paasout_year',
					'dob',
					'address',
					'contact_number',
					'is_admin',]



class EventForm(forms.ModelForm):

	class Meta:
		model = Event
		fields = '__all__'