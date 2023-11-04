from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer

#registration
class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        labels = {'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}

#loginForm
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control' }))

    password = forms.CharField(label=_('password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current_password', 'class':'form-control' }))


#password change

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_('old password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current_password', 'autofocus':True , 'class':'form-control'}))

    new_password1 = forms.CharField(label=_('new password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())

    new_password2 = forms.CharField(label=('confirm new password'),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new password','class':'form-control'}))

#password_reset_Form

class MyPasswordResetForm(PasswordResetForm):
    email = forms.CharField(label=_("Email"),max_length=254, widget=forms.EmailInput(attrs={'autocomplete':'email', 'class':'form-control'}))


#set password form
class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_('New password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
    
    new_password2 = forms.CharField(label=_('Confirm new password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}))


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','division','district','thana','villorroad','zipcode']
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}), 'division':forms.Select(attrs={'class':'form-control'}), 'district':forms.TextInput(attrs={'class':'form-control'}), 'thana':forms.TextInput(attrs={'class':'form-control'}), 'villorroad':forms.TextInput(attrs={'class':'form-control'}), 'zipcode':forms.NumberInput(attrs={'class':'form-control'})} 
