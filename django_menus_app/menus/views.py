from django.shortcuts import render,redirect
from django.contrib import messages
from menus.models import Menus

# Create your views here.

def menus(request):
  menus = Menus.objects.all()
  return render(request, 'menus/menus.html',{"menus":menus})

def create_menu(request):
  if request.method == 'POST':
    starter=request.POST['starter']
    main = request.POST['main']
    dessert = request.POST['dessert']
    price = request.POST['price']
    new_menu = Menus(starter=starter,main=main,dessert=dessert,price=price)
    new_menu.save()
    messages.add_message(request,messages.SUCCESS,'Menu added successfully')
    return redirect('/menus/')
  else:
    return render(request,'menus/menus-form.html')