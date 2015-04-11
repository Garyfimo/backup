from django import forms

from .models import SignUp

class SignUpForm(forms.ModelForm):
	"""docstring for SignUpForm"""
	class Meta:
		model = SignUp