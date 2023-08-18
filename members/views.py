from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from members.models import Member1
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def mem(request):
    ml=Member1.objects.all().values()
    context={
        'mymemb':ml,
    }
    return render(request,'memberlist.html',context)

def add(request):
    mek=Member1.objects.all()
    context={
        'mhj':mek
    }
    return render(request,'addmem.html',context)


def addrec(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        mk=Member1(firstname=fname,lastname=lname)
        mk.save()
        return redirect("home")
    
def delete(request,id):
    md=Member1.objects.get(id=id)
    md.delete()
    return redirect("home")

def up(request,id):
    mj=Member1.objects.get(id=id)
    context={
        'mh':mj
    }
    return render(request,'update.html',context)

def update(request,id):   
    first=request.POST['fname']
    second=request.POST['lname']
    me=Member1.objects.get(id=id)
    me.firstname=first
    me.lastname=second
    me.save()
    return redirect("home")

def logout(request):
    template=loader.get_template('logout.html')
    return HttpResponse(template.render())

def login_user(request):
    if request.method=='POST':
        username = request.POST["username"]
        pasword = request.POST["pasword"]
        user = authenticate(request, username=username, password=pasword)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
           messages.success(request,('Incorrect User Name or Password. Please Enter Correct Username and Password'))
           return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    return render(request,'register.html')
def register_user(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'Registeration is Sucusseful')
            return redirect("home")
        else:
            form=UserCreationForm()

    return render(request,'register.html',{
        'form':form,
    })


