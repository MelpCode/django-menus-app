from django.shortcuts import render,redirect
from menus.models import Menus

# Create your views here.

def menus(request):
  return render(request, 'menus/menus.html')

def create_menu(request):
  if request.method == 'POST':
    starter=request.POST['starter']
    main = request.POST['main']
    dessert = request.POST['dessert']
    price = request.POST['price']
    new_menu = Menus(starter=starter,main=main,dessert=dessert,price=price)
    new_menu.save()
    print('Menu Saved Succesfully')
    return redirect('/menus/')
  else:
    return render(request,'menus/menus-form.html')