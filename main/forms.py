from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class LoginForm(ModelForm):
	class Meta:
		model=User
		fields=('username','password')
class WithdrawForm(forms.ModelForm):
    class Meta:
        model=Withdraw
        fields=['wallet','address','amount',]
    amount= forms.CharField(label='Minimum Withdraw Is $10',required=True)
    address= forms.CharField(label='Account Address(Phone no, or Wallet address)',required=True)
class RegistrationForm(UserCreationForm):
	email=forms.EmailField()

	class Meta:
		model=User
		fields=["username","email","password1","password2"]


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for bound_field in self:
            if hasattr(bound_field, "field") and bound_field.field.required:
                bound_field.field.widget.attrs["required"] = "required"

class KYCForm(forms.ModelForm):
    class Meta:
        model=KYC
        fields=['nin','front','back',]
    nin= forms.CharField(label='Enter Unique NIN number',required=True)