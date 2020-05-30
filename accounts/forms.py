from django import forms
from django.contrib.auth import authenticate,get_user_model
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError('The user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Password does not exist')
            if not user.is_active:
                raise forms.ValidationError('user is not active')




        return super(LoginForm,self).clean()

class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label='email')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget= forms.PasswordInput,max_length=200)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
        ]

    def clean(self,*args,**kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError('Emails must mathc')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('User already exists')
        return super(RegisterForm,self).clean(*args,**kwargs)
    
