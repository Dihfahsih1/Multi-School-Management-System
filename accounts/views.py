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


#######################################
#   CRUD FOR THE EXAM TERM MODULE    #
#######################################
def addexamterm(request):
    if request.method=="POST":
        form=AddExamTermForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addexamterm')
    else:
        form = AddExamTermForm()
        context = {'form': form}
        return render(request, 'accounts/addexamterm.html', context)
def editexamterm(request, pk):
    item = get_object_or_404(ExamTerm, id=pk)
    if request.method == "POST":
        form =  EditExamTermForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewexamterm')
    else:
        form =  EditExamTermeForm(instance=item)
        return render(request, 'accounts/editexamterm.html', {'form': form})

def deleteexamterm(request, pk):
    ExamTerm.objects.filter(id=pk).delete()
    all_info=ExamTerm.objects.all()
    context={'all_info' :all_info}
    return render(request, 'accounts/viewexamterm.html', context)
def viewexamterm(request):
    all_info = ExamTerm.objects.all()
    context={'all_info':all_info}
    return render(request, 'accounts/viewexamterm.html', context)

  #######################################
#   CRUD FOR THE EXAM SCHEDULE MODULE    #
  #######################################
def addexamschedule(request):
    if request.method=="POST":
        form=AddExamScheduleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addexamschedule')
    else:
        form = AddExamScheduleForm()
        context = {'form': form}
        return render(request, 'accounts/addexamschedule.html', context)
def editexamschedule(request, pk):
    item = get_object_or_404(ExamSchedule, id=pk)
    if request.method == "POST":
        form =  EditExamScheduleForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewexamschedule')
    else:
        form =  EditExamScheduleForm(instance=item)
        return render(request, 'accounts/editexamschedule.html', {'form': form})

def deleteexamschedule(request, pk):
    ExamSchedule.objects.filter(id=pk).delete()
    all_info=ExamSchedule.objects.all()
    context={'all_info' :all_info}
    return render(request, 'accounts/viewexamschedule.html', context)
def viewexamschedule(request):
    all_info = ExamSchedule.objects.all()
    context={'all_info':all_info}
    return render(request, 'accounts/viewexamschedule.html', context)



  #######################################
#   CRUD FOR THE EXAM SUGGESTION MODULE    #
  #######################################
def addexamsuggestion(request):
    if request.method=="POST":
        form=AddExamSuggestionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addexamsuggestion')
    else:
        form = AddExamSuggestionForm()
        context = {'form': form}
        return render(request, 'accounts/addexamsuggestion.html', context)
def editexamsuggestion(request, pk):
    item = get_object_or_404(ExamSuggestion, id=pk)
    if request.method == "POST":
        form =  EditExamSuggestionForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewexamsuggestion')
    else:
        form =  EditExamSuggestionForm(instance=item)
        return render(request, 'accounts/editexamsuggestion.html', {'form': form})

def deleteexamsuggestion(request, pk):
    ExamSuggestion.objects.filter(id=pk).delete()
    all_info=ExamSuggestion.objects.all()
    context={'all_info' :all_info}
    return render(request, 'accounts/viewexamsuggestion.html', context)
def viewexamsuggestion(request):
    all_info = ExamSuggestion.objects.all()
    context={'all_info':all_info}
    return render(request, 'accounts/viewexamsuggestion.html', context)

  #######################################
#   CRUD FOR THE LIBRARY MODULE         #
  #######################################
def addlibrarybook(request):
    if request.method=="POST":
        form=AddLibraryBookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addlibrarybook')
    else:
        form = AddLibraryBookForm()
        context = {'form': form}
        return render(request, 'accounts/addlibrarybook.html', context)
def editlibrarybook(request, pk):
    item = get_object_or_404(Library, id=pk)
    if request.method == "POST":
        form =  EditLibraryBookForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewlibrarybook')
    else:
        form =  EditLibraryBookForm(instance=item)
        return render(request, 'accounts/editlibrarybook.html', {'form': form})

def deletelibrarybook(request, pk):
    Library.objects.filter(id=pk).delete()
    all_info=Library.objects.all()
    context={'all_info' :all_info}
    return render(request, 'accounts/viewlibrarybook.html', context)
def viewlibrarybook(request):
    all_info = Library.objects.all()
    context={'all_info':all_info}
    return render(request, 'accounts/viewlibrarybook.html', context)


  #######################################
#   CRUD FOR THE VEHICLE MODULE         #
  #######################################
def addvehicle(request):
    if request.method=="POST":
        form=AddVehicleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addvehicle')
    else:
        form = AddVehicleForm()
        context = {'form': form}
        return render(request, 'accounts/addvehicle.html', context)
def editvehicle(request, pk):
    item = get_object_or_404(Transport, id=pk)
    if request.method == "POST":
        form =  EditVehicleForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewvehicle')
    else:
        form =  EditVehicleForm(instance=item)
        return render(request, 'accounts/editvehicle.html', {'form': form})

def deletevehicle(request, pk):
    Transport.objects.filter(id=pk).delete()
    all_info=Transport.objects.all()
    context={'all_info' :all_info}
    return render(request, 'accounts/viewvehicle.html', context)
def viewvehicle(request):
    all_info = Transport.objects.all()
    context={'all_info':all_info}
    return render(request, 'accounts/viewvehicle.html', context)



  #############################################
#   CRUD FOR THE TRANSPORT ROUTE MODULE         #
  #############################################
def addroute(request):
    if request.method=="POST":
        form=AddRouteForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addroute')
    else:
        form = AddRouteForm()
        context = {'form': form}
        return render(request, 'accounts/addroute.html', context)
def editroute(request, pk):
    item = get_object_or_404(Transport, id=pk)
    if request.method == "POST":
        form =  EditRouteForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewroute')
    else:
        form =  EditRouteForm(instance=item)
        return render(request, 'accounts/editroute.html', {'form': form})

def deleteroute(request, pk):
    Route.objects.filter(id=pk).delete()
    all_info=Route.objects.all()
    context={'all_info' :all_info}
    return render(request, 'accounts/viewroute.html', context)
def viewroute(request):
    all_info = Route.objects.all()
    context={'all_info':all_info}
    return render(request, 'accounts/viewroute.html', context)



  ################################################
#   CRUD FOR THE HOSTEL INFORMATION MODULE         #
  ################################################
def addhostel(request):
    if request.method=="POST":
        form=AddHostelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addhostel')
    else:
        form = AddHostelForm()
        context = {'form': form}
        return render(request, 'accounts/addhostel.html', context)

def edithostel(request, pk):
    item = get_object_or_404(Hostel, id=pk)
    if request.method == "POST":
        form =  EditHostelForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewhostel')
    else:
        form =  EditHostelForm(instance=item)
        return render(request, 'accounts/edithostel.html', {'form': form})

def deletehostel(request, pk):
    Hostel.objects.filter(id=pk).delete()
    all_info=Hostel.objects.all()
    context={'all_info' :all_info}
    return render(request, 'accounts/viewhostel.html', context)

def viewhostel(request):
    all_info = Hostel.objects.all()
    context={'all_info':all_info}
    return render(request, 'accounts/viewhostel.html', context)

 ################################################
#   CRUD FOR THE HOSTEL ROOM MODULE              #
 ################################################
def addroom(request):
   if request.method=="POST":
       form=AddHostelRoomForm(request.POST,request.FILES)
       if form.is_valid():
           form.save()
           return redirect('addroom')
   else:
       form = AddHostelRoomForm()
       context = {'form': form}
       return render(request, 'accounts/addhostelroom.html', context)

def editroom(request, pk):
   item = get_object_or_404(HostelRooms, id=pk)
   if request.method == "POST":
       form =  EditHostelRoomForm(request.POST,request.FILES, instance=item)
       if form.is_valid():
           form.save()
           return redirect('viewroom')
   else:
       form =  EditHostelRoomForm(instance=item)
       return render(request, 'accounts/edithostelroom.html', {'form': form})

def deleteroom(request, pk):
   HostelRooms.objects.filter(id=pk).delete()
   all_info=HostelRooms.objects.all()
   context={'all_info' :all_info}
   return render(request, 'accounts/viewhostelroom.html', context)

def viewroom(request):
   all_info = HostelRooms.objects.all()
   context={'all_info':all_info}
   return render(request, 'accounts/viewhostelroom.html', context)

 ################################################
#   CRUD FOR THE VISITOR INFO MODULE              #
 ################################################
def addvisitor(request):
   if request.method=="POST":
       form=AddVistorInfoForm(request.POST,request.FILES)
       if form.is_valid():
           form.save()
           return redirect('addvisitor')
   else:
       form = AddVistorInfoForm()
       context = {'form': form}
       return render(request, 'accounts/addvisitor.html', context)

def editvisitor(request, pk):
   item = get_object_or_404(VisitorInfor, id=pk)
   if request.method == "POST":
       form =  EditVistorInfoForm(request.POST,request.FILES, instance=item)
       if form.is_valid():
           form.save()
           return redirect('viewvisitor')
   else:
       form =  EditVistorInfoForm(instance=item)
       return render(request, 'accounts/editvisitor.html', {'form': form})

def deletevisitor(request, pk):
   VisitorInfor.objects.filter(id=pk).delete()
   all_info=VisitorInfor.objects.all()
   context={'all_info' :all_info}
   return render(request, 'accounts/viewvisitor.html', context)

def viewvisitor(request):
   all_info = VisitorInfor.objects.all()
   context={'all_info':all_info}
   return render(request, 'accounts/viewvisitor.html', context)

 ################################################
#   CRUD FOR THE SALARY GRADE INFO MODULE        #
 ################################################
def addsalarygrade(request):
   if request.method=="POST":
       form=AddSalaryGradeForm(request.POST,request.FILES)
       if form.is_valid():
           form.save()
           return redirect('addsalarygrade')
   else:
       form = AddSalaryGradeForm()
       context = {'form': form}
       return render(request, 'accounts/addsalarygrade.html', context)

def editsalarygrade(request, pk):
   item = get_object_or_404(SalaryGrade, id=pk)
   if request.method == "POST":
       form =  EditSalaryGradeForm(request.POST,request.FILES, instance=item)
       if form.is_valid():
           form.save()
           return redirect('viewsalarygrade')
   else:
       form =  EditSalaryGradeForm(instance=item)
       return render(request, 'accounts/editsalarygrade.html', {'form': form})

def deletesalarygrade(request, pk):
   SalaryGrade.objects.filter(id=pk).delete()
   all_info=SalaryGrade.objects.all()
   context={'all_info' :all_info}
   return render(request, 'accounts/viewsalarygrade.html', context)

def viewsalarygrade(request):
   all_info = SalaryGrade.objects.all()
   context={'all_info':all_info}
   return render(request, 'accounts/viewsalarygrade.html', context)
