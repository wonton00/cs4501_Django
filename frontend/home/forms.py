from django import forms
import datetime
from django.utils import timezone
class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput)
	
class RegisterForm(forms.Form):
	username = forms.CharField(required=False)
	password = forms.CharField(required=True, widget=forms.PasswordInput)
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	date_of_birth = forms.DateField(required=True, initial=timezone.now())

class JobForm(forms.Form):
	name = forms.CharField(required=True)
	description = forms.CharField(widget=forms.Textarea)
	price = forms.DecimalField(required=True)
	location = forms.CharField(required=True)

class SearchForm(forms.Form):
	search = forms.CharField(required=True, label='What are you searching for?', max_length=50)
