
from django.shortcuts import render,redirect
from django.http import HttpResponse
from SignUp.forms import SignUpForm,AdminlogForm 
from SignUp.models import Adminlog, SignUp  

# Create your views here.

def signup(request):
    return render(request,'SignUp.html')

def adminlogout(request):
    return render(request,'adminlogin.html')

def aboutus(request):
    return render(request,'aboutus.html')

def login(request):
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def sup(request):  
   
    if request.method == "POST": 
        
        form = SignUpForm(request.POST or None) 
        # form.save() 
        # return HttpResponse(form.is_valid())  
        
        if form.is_valid():
            
            try:  
                print("Hello")
                form.save()  
                return render(request,'login.html')  
            except:  
                pass  
    else:  
        form = SignUpForm()  
    return render(request,'SignUp.html',{'form':form})

def loginHandle(request):
    
    if request.method == "POST":    
        form = SignUpForm(request.POST)
        un = request.POST.get("username")
        ps = request.POST.get("password")
        uname = SignUp.objects.all().filter(username=un)
        
       
        if uname[0].username == un and uname[0].password == ps:
            return render(request,'home.html', {"username" : un})  
            # return HttpResponse('successful')
       
    else:
        form = SignUpForm()
        return render(request, template_name = "login.html"  , context = {"form":form})
  
def adminlogin(request):
    return render(request,'adminlogin.html')


def adminloginHandle(request):
    
    if request.method == "POST":    
        form = AdminlogForm(request.POST)
        un = request.POST.get("username")
        ps = request.POST.get("password")
        uname = Adminlog.objects.all().filter(username=un)
        
       
        if uname[0].username == un and uname[0].password == ps:
            return render(request,'admin.html')  
            # return HttpResponse('successful')
       
    else:
        form = AdminlogForm()
        return render(request, template_name = "login.html"  , context = {"form":form})