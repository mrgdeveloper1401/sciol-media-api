from django.shortcuts import render
from django.views import View
from .forms import RegisterUserForm
from .models import User


class RegisterUserView(View):
    form_class = RegisterUserForm
    template_name = 'accounts/register.html'
    
    def get(self, request):
        register = self.form_class()
        return render(request, self.template_name, {'register': register})
        
    def post(self, request):
        register = self.form_class(request.POST)
        if register.is_valid():
            cd = register.cleaned_data
            email = cd.get('email')
            username = cd.get('username')
            password = cd.get('password')
            User.objects.create_user(
                email=email,
                password = password,
                username = username
            )
        return render(request, self.template_name, {"register": register})
            
