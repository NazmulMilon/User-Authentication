from django.shortcuts import redirect, render,HttpResponse
from .Mainuserform import Salim,loginf
from django.contrib import messages
from django.db.models import Q
# Create your views here.
from .models import Mainuser

def home(request):
    milon=Salim()
    if request.method == "POST":
        milon=Salim(request.POST,request.FILES)
        if milon.is_valid():
            milon.save()
            messages.success(request,"Hey u Saved")


    con = {
        'f': milon
    }
    return render(request,'index.html',con)

def userlog(request):
    
    king=loginf()
         # if request.method =='POST':
        #
        #     name=request.POST['name']
        #     email = request.POST['email']
        #     s=Mainuser.objects.filter(name=name,email=email)
        #     if s:
        #         return  HttpResponse("your login")

    # if request.method=='POST':
    #     king = loginf(request.POST)
    #     if king.is_valid():
    #         name=king.cleaned_data['name']
    #         email=king.cleaned_data['email']
    #         s = Mainuser.objects.filter(name=name, email=email)
    #         if s:
    #             return HttpResponse("your login")
    if request.method == 'POST':
        king = loginf(request.POST)
        if king.is_valid():
            name = king.cleaned_data['name']
            email = king.cleaned_data['email']
            s = Mainuser.objects.filter(name=name, email=email).count()
            if s>=1:
                return HttpResponse(f'u r login {name}')

    con={
        'f':king
    }
    return  render(request,'log.html',con)


def show(request):
    milu=Mainuser.objects.all()
    
    con={
        'm':milu
    }
    return render(request, 'display.html',con)

def search(request):
    
    if request.method=="POST":
        naz=request.POST['sa']
        
        mul=Mainuser.objects.filter(Q(name__icontains=naz)|Q(email__icontains=naz)).distinct()
        if mul:
            con={
                'm':mul
            }
            return render(request, 's.html',con)
    return render(request, 's.html')

def edit(request,id):
    
    d=Mainuser.objects.get(id=id)
    d.save()
    con={
        'f':d
    }
    return render(request,'edit.html',con)


def update(request,id):
    d=Mainuser.objects.get(id=id)
    
    d.name=request.POST['name']
    d.email=request.POST['email']

    d.address=request.POST['address']

    d.phone=request.POST['phone']

    d.images=request.POST['images']
    s=Mainuser(name=name,email=email,address=address,phone=phone,images=images)

    s.save()
    return render(request,'edit.html')

def delete(request,id):
    d=Mainuser.objects.get(id=id)  
    d.delete()
    messages.success(request,"Hey u delete")
    return redirect('show')

    return render(request,'display.html') 
   
    
