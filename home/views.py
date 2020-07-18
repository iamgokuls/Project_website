from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm,EditProfile,Feedback
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import history
# Create your views here.

def homeview(request):
    return render(request,'index.html')

@login_required(login_url='login')
def profilepage(request):
    return render(request,'profile.html')

def register(request):
    if request.method == 'POST':
        form=RegistrationForm(request.POST)
        text='Registration failed'
        flag=False
        if form.is_valid():
            form.save()
            name=form.cleaned_data['first_name']
            text="Successfully Registered"
            flag=True

        return render(request,'signup.html',{'form':form,'text':text,'flag':flag})
    else:
        form=RegistrationForm()
        return render(request,'signup.html')

def logoutuser(request):
    auth.logout(request)
    return redirect('index')




class LoginPage(TemplateView):
    def get(self,request):
        messages=''
        return render(request,'login.html',{'messages':messages})

    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=auth.authenticate(request,username=username,password=password)

        if user is not None:
            messages="Valid"
            auth.login(request,user)
            return redirect('profile')
        else:
            messages="Invalid User Credentials"
            return render(request,'login.html',{'messages':messages})
            #redirect('login')
@csrf_exempt
def getmail(request):
    username=request.POST.get('username')
    password=request.POST.get('password')

    user=auth.authenticate(request,username=username,password=password)

    if user is not None:
        message=user.email
        return HttpResponse(message)
    else:
        message="invalid"
        return HttpResponse(message)


@login_required(login_url='login')
def changepass(request):
    if request.method== 'POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)
        text='Updation failed'
        flag=False
        if form.is_valid():
            form.save()
            text="Successfully Updated"
            flag=True
            update_session_auth_hash(request,form.user)
        return render(request,'changepass.html',{'form':form,'text':text,'flag':flag})

        
    else:
        form=PasswordChangeForm(user=request.user)
        return render(request,'changepass.html')

@login_required(login_url='login')
def changeinfo(request):
    if request.method== 'POST':
        form=EditProfile(request.POST,instance=request.user)
        text='Updation failed'
        flag=False
        if form.is_valid():
            form.save()
            text="Successfully Updated"
            flag=True
        return render(request,'changeinfo.html',{'form':form,'text':text,'flag':flag})

        
    else:
        form=EditProfile(instance=request.user)
        return render(request,'changeinfo.html')

def feedback(request):
    if request.method=="POST":
        form=Feedback(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request,'index.html',{'form':form})
    else:
        return redirect('index')

@csrf_exempt
def sethistory(request):
    if request.method=="POST":
        email=request.POST.get('email')
        message=request.POST.get('message')
        obj=history(email=email,message=message)
        obj.save()
        return HttpResponse("success")

@login_required(login_url='login')
def gethistory(request):
   
    if request.method=="GET":
        mailid=request.user.email
        results=enumerate(history.objects.filter(email=mailid).order_by('-datetime'),1)
        length=len(history.objects.filter(email=mailid))
        flag=0
        if(length==0):
            flag=1
        return render(request,'history.html',{'results':results,'flag':flag})

def error_404_view(request,exception=None):
    data={}
    return render(request,'error.html',status=404)

'''def error(request):
    return render(request,'error.html')'''