from django.shortcuts import render
from django.views import View


class RegisterUserView(View):
    form_class = ''
    template_name = ''
    
    def get(self, request):
        ...
        
    def post(self, request):
        ...
