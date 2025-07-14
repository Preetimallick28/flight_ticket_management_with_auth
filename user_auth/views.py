from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login , logout
from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# we are learning django session base authentication system
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username_data = request.POST['username']
        password_data = request.POST['password']
        # print(username_data,password_data)
        u=authenticate(username=username_data , password = password_data) #return boolean value
        print(u)
        # if credential is matching it will return user_out(true) and if not matching return None
        if u is not None:
            login(request,u)
            return redirect('home')
        else:
            return render(request,'login.html',{'wrong_':True})
        
    return render(request,'login.html') 

def register_view(request):
    context = {}
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        print(firstname,lastname,email,username)
        if User.objects.filter(username=username).exists():
            context['error'] = 'Username already exists.please choose another one'
            return render(request,'register.html',context)

        u=User.objects.create(
            first_name = firstname,
            last_name = lastname,
            email = email,
            username = username,
        )
        # set_password() used to store password in encrypted format
        u.set_password(password)
        u.save()
        return redirect('login')
    #IntegrityError - unique constraint failed:auth_username -  when same username is used
        
    return render(request,'register.html')

def logout_(request):
    logout(request)
    return redirect('login')

#for what purpose we are storing credential in session storage
# to design navbar like profile
#how to store?
# first we have to import login
# from django.contrib.auth import authenticate ,login

@login_required
def profile(request):
    return render(request,'profile.html')

@login_required
def reset_pass(request):
    context={}
    user_record = User.objects.get(username=request.user)
    print(user_record.password)
    if request.method=='POST':
        old_pass = request.POST['old_pass']
        new_pass = request.POST['new_pass']
        
        u= authenticate(username=user_record.username , password=old_pass)
        # print(old_pass,new_pass)
        if u is not None:
            user_record.set_password(new_pass)
            user_record.save()
            logout(request)
            return redirect('login')
        else:
            context['error']='you have entered wrong old password'
            return render(request,'reset_pass.html',context)
        
    return render(request,'reset_pass.html')

@login_required
def update_profile(request,pk):
    u=User.objects.get(username=pk)
    if request.method=='POST':
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        email = request.POST['email']
        username = request.POST['username']

        u.first_name = first_name
        u.last_name = last_name
        u.email = email
        u.username = username
        u.save()
        return redirect('profile')
    return render(request,'update_profile.html',{'u':u})