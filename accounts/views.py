from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterUserForm, UserSigninForm
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.crypto import get_random_string
from django.http import Http404
from django.contrib.auth.forms import PasswordResetForm


class UserSignupView(View):
    form_class = RegisterUserForm
    template_name = 'accounts/register.html'
    
    def get(self, request):
        register = self.form_class()
        return render(request, self.template_name, {'register': register})
        
    def post(self, request):
        register = self.form_class(request.POST)
        if register.is_valid():
            cd = register.cleaned_data
            User.objects.create_user(
                email = cd['email'],
                username = cd['username'],
                password = cd['password'],
                mobile = cd['mobile'],
                is_active = False,
                email_active_code = get_random_string(72)
            )
            messages.success(request, 'success create account', 'success')
            messages.success(request, 'please verify email address', 'success')
            return redirect('accounts:login')
        return render(request, self.template_name, {"register": register})


class ActiveAccountView(View):
    def get(self, request, email_active_code):
        try:
            user = User.objects.get(email_active_code__iexact=email_active_code)
            if user:
                if not user.is_active:
                    user.is_active = True
                    user.save()
                    messages.success(request, 'Your account has been activated successfully.', 'success')
                    return redirect('accounts:login')
                else:
                    messages.error(request, 'your accounts was activate', 'warning')
                    raise Http404
            else:
                raise Http404
        except User.DoesNotExist:
            raise Http404

        
class UserSigninView(View):
    form_class = UserSigninForm
    template_name = 'accounts/login.html'
    
    def get(self, request):
        signin_form = self.form_class()
        return render(request, self.template_name, {"signin_form": signin_form})
    
    def post(self, request):
        signin_form = self.form_class(request.POST)
        if signin_form.is_valid():
            cd = signin_form.cleaned_data
            user = authenticate(
                username = cd['usernme'],
                password = cd['password']
            )
            if user is not None:
                login(user)
                # success
                # redirect
                if self.next:
                    return redirect(self.next)
                # redirect
            # error
        return render(request, self.template_name, {"signin_form": signin_form})
    

class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        # message success
        


class ForgetPasswordView(View):
    ...