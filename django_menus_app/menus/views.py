from django.shortcuts import render

# Create your views here.

def menus(request):
  return render(request, 'menus/menus.html')

def create_menu(request):
  return render(request,'menus/menus-form.html')