from django.shortcuts import render,redirect

# Create your views here.

def menus(request):
  return render(request, 'menus/menus.html')

def create_menu(request):
  if request.method == 'POST':
    main = request.POST['main']
    dessert = request.POST['dessert']
    price = request.POST['price']
    print(f'{main} {dessert} {price}')
    return redirect('/menus/')
  else:
    return render(request,'menus/menus-form.html')