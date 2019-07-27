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
        form=ClassinformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createclassinformation')
    else:
        form = ClassinformationForm()
        context = {'form': form}
        return render(request, 'accounts/createclassinformation.html', context)

def editclassinformation(request, pk):
    item = get_object_or_404(Classinformation, id=pk)
    if request.method == "POST":
        form =  EditinformationForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewclassinformation')
    else:
        form =  EditinformationForm(instance=item)
        return render(request, 'accounts/editclassinformation.html', {'form': form})

def deleteclassinformation(request, pk):
    Classinformation.objects.filter(id=pk).delete()
    all_info=Classinformation.objects.all()
    context={'all_info' :all_info}

    return render(request, 'accounts/viewclassinformation.html', context)

def viewclassinformation(request):
    all_info = Classinformation.objects.all()
    context={'all_info':all_info}
    return render(request, 'accounts/viewclassinformation.html', context)
# Create your views here.
