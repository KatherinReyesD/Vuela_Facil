from django import views
from django.views import View
from django.shortcuts import render


class LandingPage (View):
    template = "main.html"
    def get (self,request):
        return render (request, self.template,{})

class checkout(View):
    template = "Carrito.html"
    def get (self,request):
        return render(request, self.template,{})