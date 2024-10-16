from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout
from .models import ItemModel


def homeView(request):
    items = ItemModel.objects.all().order_by('-created_at')
    paginator = Paginator(items, 6)
    page_number = request.GET.get('page')
    page_items = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_items': page_items})


def adminLoginView(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.filter(username=username).first()

            if not user:
                messages.error(request, "Admin Account Not Found")
                return redirect('admin_login')
            
            if not user.check_password(password):
                messages.error(request, "Incorrect Password")
                return redirect('admin_login')
            
            login(request, user=user)
            return redirect('home')
        
        except Exception as ex:
            print(ex)
            messages.error(request, "Something Went Wrong")
            return redirect('admin_login')
        
    return render(request, 'login.html')


def addItemVIew(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            description = request.POST['description']
            price = request.POST['price']

            item = ItemModel.objects.create(
                name=name,
                description=description,
                price=price
            )
            if 'image' in request.FILES:
                image = request.FILES.get('image', None)
                item.image = image

            item.save()
            return redirect('home')
        
        except Exception as ex:
            print(ex)
            messages.error("Something Went Wrong")
            return redirect('add_items')
        
    return render(request, 'add_items.html')


def logoutView(request):
    logout(request)
    return redirect('home')