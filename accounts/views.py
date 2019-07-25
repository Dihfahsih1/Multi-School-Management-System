from django.shortcuts import *
from django.views.generic import CreateView
from .models import *
from .forms import *
def home(request):
    return render(request, 'accounts/home.html')
def login(request):
 form = LoginForm()
 context = {'form': form}
 return render(request, 'accounts/login.html', context)

def logout(request):
 return render(request, 'accounts/login.html')

def createclassinformation(request):
    if request.method=="POST":
        form=Createclassinformation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createclassinformation')
    else:
        form = Createclassinformation()
        context = {'form': form}
        return render(request, 'accounts/createclassinformation.html', context)

def editclassinformation(request):
 return render(request, 'accounts/editclassinformation.html')

def deleteclassinformation(request):
 return render(request, 'accounts/deleteclassinformation.html')

def viewclassinformation(request):
 return render(request, 'accounts/viewclassinformation.html')
# Create your views here.
