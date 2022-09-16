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
  
def delete_menu(request,menu_id):
  if request.method == 'POST':
    print(menu_id)
    menu = Menus.objects.get(id=menu_id)
    menu.delete()
    return redirect('/menus/')
  
def edit_menu(request,menu_id):
  menu = Menus.objects.get(id=menu_id)
  if request.method == 'POST':
    main = request.POST['main']
    starter = request.POST['starter']
    dessert = request.POST['dessert']
    price = request.POST['price']
    menu.main = main
    menu.starter =starter
    menu.dessert = dessert
    menu.price = price
    menu.save()
    return redirect('/menus/')
  else:
    return render(request,'menus/menus-form.html',{"edit":True,"menu":menu})

def search_menu(request):
  if request.method=='POST':
    value=request.POST['value']
    if request.POST['type_menu'] == 'starter':
      menus = Menus.objects.filter(starter__icontains=value)
    if request.POST['type_menu'] == 'main':
      menus = Menus.objects.filter(main__icontains=value)
    if request.POST['type_menu'] == 'dessert':
      menus = Menus.objects.filter(dessert__icontains=value)
  return render(request,'menus/menus.html',{"menus":menus})