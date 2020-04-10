from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import feedback

class RegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=(
            'username',
            'first_name',
            'email',
            'password1',
            'password2'
        )
    def save(self,commit=True):
        user=super(RegistrationForm,self).save(commit=False)
        user.first_name=self.cleaned_data['first_name']
        user.email=self.cleaned_data['email']

        if commit:
            user.save()

        return user
    
class EditProfile(UserChangeForm):
    class Meta:
        model=User
        fields=(
            'first_name',
            'username',
            'email',
            'password'
        )

class Feedback(forms.ModelForm):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    content=forms.CharField()

    class Meta:
        model=feedback
        fields=('name','email','content')