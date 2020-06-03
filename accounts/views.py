from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import get_user_model,authenticate,login,logout
from django_email_verification import sendConfirm
from .forms import *
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.views.generic import View
from django.contrib import messages
from django.http import JsonResponse


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        login(request,user)
        return redirect('home')

    context = {
        'form' : form
    }
    return render(request,'login.html',context)





def register_view(request):
    User = get_user_model()
    if request.method == 'POST':
        form = CustomUserRegistration(request.POST or None)
        if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string('confirm_email.html', {
                            'user': user,
                            'domain': current_site.domain,
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                            'token': account_activation_token.make_token(user),
                        })
                to_email = form.cleaned_data.get('email')
                send_mail(mail_subject, message, 'devbryan254@gmail.com', [to_email])
                return render(request,'email_redirect.html',{})
                return redirect('home')
    else:
        form = CustomUserRegistration()
    return render(request, 'register.html', {'form': form})




def validate_username(request):
    username = request.get.GET('username')
    email_qs = User.objects.filter(username__icontains=username).exists


    
    return JsonResponse


class ActivateAccount(View):
    
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            # login(request, user)
            return render(request,'confirm_sucess.html',{})
            return redirect('home')
        else:
            return render(request,'confirm_error.html',{})
            return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('/')

