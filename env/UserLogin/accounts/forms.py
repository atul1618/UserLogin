from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']
        widgets={
            'first_name':forms.TextInput(attrs={'placeholder':'First Name '}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name '}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address '}),
            'username':forms.TextInput(attrs={'placeholder':'Username'})
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Enter Your Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})

    def clean(self):
        print("Inside clean method ")
        cleaned_data=super().clean()
        userid=cleaned_data.get('username')
        mailid=cleaned_data.get('email')
        qs1=User.objects.filter(username=userid)
        if qs1:
            msg='Username exists'
            self.add_error('username',msg)
        else:
            print("Username created")
        qs2=User.objects.filter(email=mailid)
        if qs2:
            msg='Email address already registered'
            self.add_error('email',msg)



