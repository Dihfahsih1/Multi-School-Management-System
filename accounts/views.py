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
    all_info=Teacher.objects.all()
    context={'all_info' :all_info}
    return render(request, 'accounts/viewteacher.html', context)

def viewteachers(request):
    all_info = Teacher.objects.all()
    context={'all_info':all_info}
    return render(request, 'accounts/viewteacher.html', context)

#######################################
#   CRUD FOR THE subject MODULE        #
#######################################
def addsubject(request):
    if request.method=="POST":
        form=AddSubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addsubject')
    else:
        form = AddSubjectForm()
        context = {'form': form}
        return render(request, 'accounts/addsubject.html', context)
def editsubject(request, pk):
    item = get_object_or_404(Subjects, id=pk)
    if request.method == "POST":
        form =  EditSubjectForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewsubjects')
    else:
        form =  EditSubjectForm(instance=item)
        return render(request, 'accounts/editsubject.html', {'form': form})

def deletesubject(request, pk):
    Subjects.objects.filter(id=pk).delete()
    all_info=Subjects.objects.all()
    context={'all_info' :all_info}
    return render(request, 'accounts/viewsubjects.html', context)

def viewsubjects(request):
    all_info = Subjects.objects.all()
    context={'all_info':all_info}
    return render(request, 'accounts/viewsubjects.html', context)


#######################################
#   CRUD FOR THE Syllabus MODULE        #
#######################################
def addsyllabus(request):
    if request.method=="POST":
        form=AddSyllabusForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addsyllabus')
    else:
        form = AddSyllabusForm()
        context = {'form': form}
        return render(request, 'accounts/addsyllabus.html', context)
def editsyllabus(request, pk):
    item = get_object_or_404(Syllabus, id=pk)
    if request.method == "POST":
        form =  EditSyllabusForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewsyllabus')
    else:
        form =  EditSyllabusForm(instance=item)
        return render(request, 'accounts/editsyllabus.html', {'form': form})

def deletesyllabus(request, pk):
    Syllabus.objects.filter(id=pk).delete()
    all_info=Syllabus.objects.all()
    context={'all_info' :all_info}
    return render(request, 'accounts/viewsyllabus.html', context)

def viewsyllabus(request):
    all_info = Syllabus.objects.all()
    context={'all_info':all_info}
    return render(request, 'accounts/viewsyllabus.html', context)

 ###############################################
#   CRUD FOR THE HUMAN RESOURCES MANAGER MODULE #
 ###############################################
def addhumanresource(request):
    if request.method=="POST":
        form=AddHumanResourceForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addhumanresource')
    else:
        form = AddHumanResourceForm()
        context = {'form': form}
        return render(request, 'accounts/addhumanresource.html', context)
def edithumanresource(request, pk):
    item = get_object_or_404(HumanResource, id=pk)
    if request.method == "POST":
        form =  EditHumanResourceForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewhumanresource')
    else:
        form =  EditHumanResourceForm(instance=item)
        return render(request, 'accounts/edithumanresource.html', {'form': form})

def deletehumanresource(request, pk):
    HumanResource.objects.filter(id=pk).delete()
    all_info=HumanResource.objects.all()
    context={'all_info' :all_info}
    return render(request, 'accounts/viewhumanresource.html', context)

def viewhumanresource(request):
    all_info = HumanResource.objects.all()
    context={'all_info':all_info}
    return render(request, 'accounts/viewhumanresource.html', context)

 ###############################################
############  CRUD FOR THE ROUTINE #############
 ###############################################
def addroutine(request):
    if request.method=="POST":
        form=AddRoutineForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addroutine')
    else:
        form = AddRoutineForm()
        context = {'form': form}
        return render(request, 'accounts/addroutine.html', context)
def editroutine(request, pk):
    item = get_object_or_404(Routine, id=pk)
    if request.method == "POST":
        form =  EditRoutineForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewroutine')
    else:
        form =  EditRoutineForm(instance=item)
        return render(request, 'accounts/editroutine.html', {'form': form})

def deleteroutine(request, pk):
    Routine.objects.filter(id=pk).delete()
    all_info=Routine.objects.all()
    context={'all_info' :all_info}
    return render(request, 'accounts/viewroutine.html', context)

def viewroutine(request):
    all_info = Routine.objects.all()
    context={'all_info':all_info}
    return render(request, 'accounts/viewroutine.html', context)

#######################################
#   CRUD FOR THE ASSIGNMENT MODULE    #
#######################################
def addassignment(request):
    if request.method=="POST":
        form=AddAssignmentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addassignment')
    else:
        form = AddAssignmentForm()
        context = {'form': form}
        return render(request, 'accounts/addassignment.html', context)
def editassignment(request, pk):
    item = get_object_or_404(Assignment, id=pk)
    if request.method == "POST":
        form =  EditAssignmentForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewassignment')
    else:
        form =  EditAssignmentForm(instance=item)
        return render(request, 'accounts/editassignment.html', {'form': form})

def deleteassignment(request, pk):
    Assignment.objects.filter(id=pk).delete()
    all_info=Assignment.objects.all()
    context={'all_info' :all_info}
    return render(request, 'accounts/viewassignment.html', context)

def viewassignment(request):
    all_info = Assignment.objects.all()
    context={'all_info':all_info}
    return render(request, 'accounts/viewassignment.html', context)

#######################################
#   CRUD FOR THE EXAM GRADE MODULE    #
#######################################
def addexamgrade(request):
    if request.method=="POST":
        form=AddExamGradeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addexamgrade')
    else:
        form = AddExamGradeForm()
        context = {'form': form}
        return render(request, 'accounts/addexamgrade.html', context)
def editexamgrade(request, pk):
    item = get_object_or_404(ExamGrade, id=pk)
    if request.method == "POST":
        form =  EditExamGradeForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewexamgrade')
    else:
        form =  EditExamGradeForm(instance=item)
        return render(request, 'accounts/editexamgrade.html', {'form': form})

def deleteexamgrade(request, pk):
    ExamGrade.objects.filter(id=pk).delete()
    all_info=ExamGrade.objects.all()
    context={'all_info' :all_info}
    return render(request, 'accounts/viewexamgrade.html', context)

def viewexamgrade(request):
    all_info = ExamGrade.objects.all()
    context={'all_info':all_info}
    return render(request, 'accounts/viewexamgrade.html', context)
