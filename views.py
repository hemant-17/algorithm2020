from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import *

# Create your views here.
def lockhome(request):
    return render(request,'lockhome.html')

def sign(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name','')
        last_name=request.POST.get('last_name','')
        username=request.POST.get('username','')
        email=request.POST.get('email','')
        password1= request.POST.get('password1','')
        password2= request.POST.get('password2','')


        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'USERNAME already registered ')
                return redirect('/sign')

            else:
                user = User.objects.create_user( first_name=first_name,last_name=last_name, username=username, email=email, password=password1 )
                user.save()
                return redirect('/lock')

        else:
            messages.info(request, 'Confirm password did not match ')
            return redirect('/sign')

    return render(request,'sign1.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        User=auth.authenticate(username=username,password=password)

        if User is not None:
            auth.login(request,User)
            username=request.user.username
            return redirect("/lock")
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/login')
    return render(request,'login1.html')

def logout(request):
    auth.logout(request)

    return redirect("/lock")

def post_a_job(request):
    if request.method=='POST':
        title = request.POST.get('title','')
        in1 = request.POST.get('input1','')
        in2 = request.POST.get('input2','')
        in3 = request.POST.get('input3','')
        in4 = request.POST.get('input4','')
        in5 = request.POST.get('input5','')
        in6 = request.POST.get('input6','')
        desc = request.POST.get('desc','')
        vacancy = request.POST.get('vacancy','')
        print(title)
        print(in1)
        print(in2)
        print(in3)
        print(in4)

    # for item in skills:
    #     print(item[0])
    job = {'job':skills}
    edu = {'edu':ed}
    # print(skills[0][0])
    #print(request.POST)
    # skill = skills_required()
    # print(skill)




    return render(request,'job_offers.html' ,job,edu)

def profile(request):
    return render(request,'profile.html')
