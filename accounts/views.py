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

 #######################################
# THE CRUD OPERATIONS ON A CLASS MODULE #
 #######################################
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
        form =  EditclassinformationForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewclassinformation')
    else:
        form =  EditclassinformationForm(instance=item)
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

#######################################
# THE CRUD OPERATIONS ON SECTION MODULE #
#######################################
def createsectioninformation(request):
    if request.method=="POST":
        form=SectioninformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createsectioninformation')
    else:
        form = SectioninformationForm()
        context = {'form': form}
        return render(request, 'accounts/createsectioninformation.html', context)
def editsectioninformation(request, pk):
    item = get_object_or_404(Sectioninformation, id=pk)
    if request.method == "POST":
        form =  EditsectioninformationForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewsectioninformation')
    else:
        form =  EditsectioninformationForm(instance=item)
        return render(request, 'accounts/editsectioninformation.html', {'form': form})

def deletesectioninformation(request, pk):
    Sectioninformation.objects.filter(id=pk).delete()
    all_info=Sectioninformation.objects.all()
    context={'all_info' :all_info}
    return render(request, 'accounts/viewsectioninformation.html', context)

def viewsectioninformation(request):
    all_info = Sectioninformation.objects.all()
    context={'all_info':all_info}
    return render(request, 'accounts/viewsectioninformation.html', context)

#######################################
# CRUD FOR THE TEACHER MODULE         #
#######################################

def createteacher(request):
    if request.method=="POST":
        form=CreateTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createteacher')
    else:
        form = CreateTeacherForm()
        context = {'form': form}
        return render(request, 'accounts/createteacher.html', context)
def editteacher(request, pk):
    item = get_object_or_404(Teacher, id=pk)
    if request.method == "POST":
        form =  CreateTeacherForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewteachers')
    else:
        form =  CreateTeacherForm(instance=item)
        return render(request, 'accounts/editteacher.html', {'form': form})

def deleteteacher(request, pk):
    Teacher.objects.filter(id=pk).delete()
    all_info=Sectioninformation.objects.all()
    context={'all_info' :all_info}
    return render(request, 'accounts/viewteacher.html', context)

def viewteachers(request):
    all_info = Teacher.objects.all()
    context={'all_info':all_info}
    return render(request, 'accounts/viewteacher.html', context)
