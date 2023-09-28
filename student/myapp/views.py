from django.shortcuts import render
from django.http import JsonResponse
from .models import Department, Course
from .forms import OrderForm
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def order_form(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Handle form submission, e.g., save data to a database
            # You can access form.cleaned_data for each field
            # Return a success message
            return JsonResponse({'message': 'Order Confirmed'})
    else:
        form = OrderForm()

    return render(request, 'order_form.html', {'form': form})

def load_courses(request):
    department_id = request.GET.get('department')
    courses = Course.objects.filter(department_id=department_id).values('id', 'name')
    return JsonResponse(list(courses), safe=False)

def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('myapp:order_form')
        else:
            messages.info(request,'invalid credentials')
            return redirect('myapp:login')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('myapp:register')
            elif User.objects.filter(email=email).exists():
                 messages.info(request, "email Taken")
                 return redirect('myapp:register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
                return redirect('myapp:login')

        else:
            messages.info(request,"password not matching")
            return redirect('myapp:register')
        return redirect('/')
    return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')