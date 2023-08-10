from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class SignupForm(UserCreationForm):
   email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
   first_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
   last_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))



class Meta:
   model = User
   fields = ('user_name','first_name','last_name','email','password1','password2')


   def __init(self,*args,**kwargs):
      super(SignupForm,self).__init__(*args, **kwargs)

      self.fields['username'].widget.attrs['class'] = 'form-control'
      self.fields['username'].widget.attrs['placeholder'] = 'User Name'
      self.fields['username'].label = ''
      self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required.150 characters or fewer.Letters,digits and @/./+/-/_ only.</small></span>'

      self.fields['username'].widget.attrs['class'] = 'form-control'
      self.fields['username'].widget.attrs['placeholder'] = 'Password'
      self.fields['username'].label = ''
      self.fields['username'].help_text = '<ul class="form-text text-muted small"><li>Your password cannot be too simmilar to your personal information</li><li>Your password cannot be entirely numbers</li></ul>'

      self.fields['username'].widget.attrs['class'] = 'form-control'
      self.fields['username'].widget.attrs['placeholder'] = ' confirm Password'
      self.fields['username'].label = ''
      self.fields['username'].help_text = '<span class="form-text text-muted "><small>Enter the same password as before</small></span>'