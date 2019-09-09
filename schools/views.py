from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.views import generic
from django.contrib import messages

from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.template.loader import render_to_string
from .forms import *

IMAGE_FILE_TYPES = ['png', 'jpg', 'pjeg']


def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password, backend='django.contrib.auth.backends.ModelBackend')
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'home/home.html')
            else:
                return render(request, 'home/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'home/login.html', {'error_message': 'Invalid login'})
    return render(request, 'home/login.html')


def logout_user(request):
    logout(request)
    return render(request, 'home/login.html')


def index(request):
    school_count = School.objects.all().count()
    student_count = Student.objects.all().count()
    context = {'school_count': school_count,
               'student_count': student_count
               }
    return render(request, 'home/home.html', context)


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'home/profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('view_profile'))
        else:
            return redirect(reverse('change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'home/change_password.html', args)


def school_create(request):
    form = SchoolForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        school = form.save(commit=False)
        school.logo = request.FILES['logo']
        file_type = school.logo.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in IMAGE_FILE_TYPES:
            context = {
                'school': school,
                'form': form,
                'error_message': 'Logo must be PNG, JPG, or JPEG',
            }
            return render(request, 'schools/create_school.html', context)
        school.save()
        return render(request, 'schools/school_list.html')
    context = {
        "form": form,
    }
    return render(request, 'schools/create_school.html', context)


def delete_school(request, school_id):
    school = School.objects.get(pk=school_id)
    school.delete()
    schools = School.objects.all()
    return render(request, 'schools/school_list.html', {'schools': schools})


def view_school(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    return render(request, 'schools/school_list.html', {'school': school})


def school_list(request):
    schools = School.objects.all()
    return render(request, 'schools/school_list.html', {'schools': schools})


def save_school_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            schools = School.objects.all()
            data['html_school_list'] = render_to_string('schools/includes/partial_school_list.html', {
                'schools': schools
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


#
#
# def school_create(request):
#     if request.method == 'POST':
#         form = SchoolForm(request.POST, request.FILES)
#     else:
#         form = SchoolForm()
#     return save_school_form(request, form, 'schools/includes/partial_school_create.html')
#
#


def school_view(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    if request.method == 'POST':
        form = SchoolForm(request.POST, instance=school)
    else:
        form = SchoolForm(instance=school)
    return save_school_form(request, form, 'schools/includes/partial_school_view.html')


def school_update(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    if request.method == 'POST':
        form = SchoolForm(request.POST, instance=school)
    else:
        form = SchoolForm(instance=school)
    return save_school_form(request, form, 'schools/includes/partial_school_update.html')


def school_delete(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    data = dict()
    if request.method == 'POST':
        school.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        schools = School.objects.all()
        data['html_school_list'] = render_to_string('schools/includes/partial_school_list.html', {
            'schools': schools
        })
    else:
        context = {'school': school}
        data['html_form'] = render_to_string('schools/includes/partial_school_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def classroom_list(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    classrooms = school.classroom_set.all()
    return render(request, 'classrooms/classroom_list.html', {
        'school': school,
        'classrooms': classrooms,
    })


def save_classroom_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            classrooms = Classroom.objects.all()
            data['html_classroom_list'] = render_to_string('classrooms/includes/partial_classroom_list.html', {
                'classrooms': classrooms
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def classroom_create(request, school_id):
    form = ClassroomForm(request.POST or None, request.FILES or None)
    school = get_object_or_404(School, pk=school_id)
    if form.is_valid():
        school_classrooms = school.classroom_set.all()
        for cr in school_classrooms:
            if cr.classroom == form.cleaned_data.get("classroom"):
                context = {
                    'school': school,
                    'form': form,
                    'error_message': 'You already added that classroom',
                }
                return render(request, 'classrooms/classroom_create.html', context)
        classroom = form.save(commit=False)
        classroom.school = school
        classroom.save()

        school_url = reverse('classroom_list', kwargs={'school_id': school_id})
        return redirect(school_url)
    context = {
        'school': school,
        'form': form,
    }
    return render(request, 'classrooms/classroom_create.html', context)


def classroom_view(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    return render(request, 'classrooms/includes/partial_classroom_view.html', {'school': school})


def classroom_update(request, pk):
    classroom = get_object_or_404(Classroom, pk=pk)
    if request.method == 'POST':
        form = ClassroomForm(request.POST, instance=classroom)
    else:
        form = ClassroomForm(instance=classroom)
    return save_classroom_form(request, form, 'classrooms/includes/partial_classroom_update.html')


def classroom_delete(request, pk):
    classroom = get_object_or_404(Classroom, pk=pk)
    data = dict()
    if request.method == 'POST':
        classroom.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        classrooms = Classroom.objects.all()
        data['html_classroom_list'] = render_to_string('classrooms/includes/partial_classroom_list.html', {
            'classrooms': classrooms
        })
    else:
        context = {'classroom': classroom}
        data['html_form'] = render_to_string('classrooms/includes/partial_classroom_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def section_list(request, school_id, classroom_id):
    classroom = get_object_or_404(Classroom, school_id=school_id, pk=classroom_id)
    sections = classroom.section_set.all()
    return render(request, 'sections/section_list.html', {
        'classroom': classroom,
        'sections': sections,
    })


def save_section_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            sections = Section.objects.all()
            data['html_section_list'] = render_to_string('sections/includes/partial_section_list.html', {
                'sections': sections
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def section_create(request, school_id, classroom_id):
    classroom = get_object_or_404(Classroom, school_id=school_id, pk=classroom_id)
    if request.method == 'POST':
        form = SectionForm(request.POST, request.FILES)
        if form.is_valid():
            section = form.save(commit=False)
            section.classroom = classroom
            section.save()
            classroom.save()

            classroom_url = reverse('section_list', kwargs={'school_id': school_id, 'classroom_id': classroom_id})

            return redirect(classroom_url)
    else:
        form = SectionForm()
    return render(request, 'sections/section_create.html', {'classroom': classroom, 'form': form})


def section_view(request, pk):
    section = get_object_or_404(Section, pk=pk)
    if request.method == 'POST':
        form = SectionForm(request.POST, instance=section)
    else:
        form = SectionForm(instance=section)
    return save_section_form(request, form, 'sections/includes/partial_section_view.html')


def section_update(request, pk):
    section = get_object_or_404(Section, pk=pk)
    if request.method == 'POST':
        form = SectionForm(request.POST, instance=section)
    else:
        form = SectionForm(instance=section)
    return save_section_form(request, form, 'sections/includes/partial_section_update.html')


def section_delete(request, pk):
    section = get_object_or_404(Section, pk=pk)
    data = dict()
    if request.method == 'POST':
        section.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        sections = Section.objects.all()
        data['html_section_list'] = render_to_string('sections/includes/partial_section_list.html', {
            'sections': sections
        })
    else:
        context = {'section': section}
        data['html_form'] = render_to_string('sections/includes/partial_section_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def superuser_list(request):
    superusers = Superuser.objects.all()
    return render(request, 'superusers/superuser_list.html', {'superusers': superusers})


def save_superuser_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            superusers = Superuser.objects.all()
            data['html_superuser_list'] = render_to_string('superusers/includes/partial_superuser_list.html', {
                'superusers': superusers
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def superuser_create(request):
    if request.method == 'POST':
        form = SuperuserForm(request.POST, request.FILES)
    else:
        form = SuperuserForm()
    return save_superuser_form(request, form, 'superusers/includes/partial_superuser_create.html')


def superuser_view(request, pk):
    superuser = get_object_or_404(Superuser, pk=pk)
    if request.method == 'POST':
        form = SuperuserForm(request.POST, instance=superuser)
    else:
        form = SuperuserForm(instance=superuser)
    return save_superuser_form(request, form, 'superusers/includes/partial_superuser_view.html')


def superuser_update(request, pk):
    superuser = get_object_or_404(Superuser, pk=pk)
    if request.method == 'POST':
        form = SuperuserForm(request.POST, instance=superuser)
    else:
        form = SuperuserForm(instance=superuser)
    return save_superuser_form(request, form, 'superusers/includes/partial_superuser_update.html')


def superuser_delete(request, pk):
    superuser = get_object_or_404(Superuser, pk=pk)
    data = dict()
    if request.method == 'POST':
        superuser.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        superusers = Superuser.objects.all()
        data['html_superuser_list'] = render_to_string('superusers/includes/partial_superuser_list.html', {
            'superusers': superusers
        })
    else:
        context = {'superuser': superuser}
        data['html_form'] = render_to_string('superusers/includes/partial_superuser_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def admin_list(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    return render(request, 'admins/admin_list.html', {
        'school': school,
    })


def save_admin_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            admins = Admin.objects.all()
            data['html_admin_list'] = render_to_string('admins/includes/partial_admin_list.html', {
                'admins': admins
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def admin_create(request, school_id):
    form = AdminForm(request.POST or None, request.FILES or None)
    school = get_object_or_404(School, pk=school_id)
    if form.is_valid():
        school_admins = school.admin_set.all()
        for cr in school_admins:
            if cr.admin.user.full_name == form.cleaned_data.get("full_name"):
                context = {
                    'school': school,
                    'form': form,
                    'error_message': 'You already added that admin',
                }
                return render(request, 'admins/admin_create.html', context)
        admin = form.save(commit=False)
        admin.school = school
        admin.save()
        return render(request, 'admins/admin_list.html', {'school': school})
    context = {
        'school': school,
        'form': form,
    }
    return render(request, 'admins/admin_create.html', context)


def admin_view(request, pk):
    admin = get_object_or_404(Admin, pk=pk)
    if request.method == 'POST':
        form = AdminForm(request.POST, instance=admin)
    else:
        form = AdminForm(instance=admin)
    return save_admin_form(request, form, 'admins/includes/partial_admin_view.html')


def admin_update(request, pk):
    admin = get_object_or_404(Admin, pk=pk)
    if request.method == 'POST':
        form = AdminForm(request.POST, instance=admin)
    else:
        form = AdminForm(instance=admin)
    return save_admin_form(request, form, 'admins/includes/partial_admin_update.html')


def admin_delete(request, pk):
    admin = get_object_or_404(Admin, pk=pk)
    data = dict()
    if request.method == 'POST':
        admin.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        admins = Admin.objects.all()
        data['html_admin_list'] = render_to_string('admins/includes/partial_admin_list.html', {
            'admins': admins
        })
    else:
        context = {'admin': admin}
        data['html_form'] = render_to_string('admins/includes/partial_admin_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def student_list(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    students = school.student_set.all()
    return render(request, 'students/student_list.html', {
        'school': school,
        'students': students,
    })


def save_student_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            students = Student.objects.all()
            data['html_student_list'] = render_to_string('students/includes/partial_student_list.html', {
                'students': students
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def student_create(request, school_id):
    form = StudentForm(request.POST or None, request.FILES or None)
    school = get_object_or_404(School, pk=school_id)
    if form.is_valid():
        school_students = school.student_set.all()
        for cr in school_students:
            if cr.student.user.full_name == form.cleaned_data.get("full_name"):
                context = {
                    'school': school,
                    'form': form,
                    'error_message': 'You already added that student',
                }
                return render(request, 'students/student_create.html', context)
        student = form
        student.school = school
        student.save()
        return redirect('student_list', pk=school_id, student_id=student.pk)
    context = {
        'school': school,
        'form': form,
    }
    return render(request, 'students/student_create.html', context)


def student_view(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student.user)
    else:
        form = StudentForm(instance=student.user)
    return save_student_form(request, form, 'students/includes/partial_student_view.html')


def student_update(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student.user)
    else:
        form = StudentForm(instance=student.user)
    return save_student_form(request, form, 'students/includes/partial_student_update.html')


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    data = dict()
    if request.method == 'POST':
        student.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        students = Student.objects.all()
        data['html_student_list'] = render_to_string('students/includes/partial_student_list.html', {
            'students': students
        })
    else:
        context = {'student': student}
        data['html_form'] = render_to_string('students/includes/partial_student_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def guardian_list(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    guardians = school.guardian_set.all()
    return render(request, 'guardians/guardian_list.html', {
        'school': school,
        'guardians': guardians,
    })


def save_guardian_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            guardians = Guardian.objects.all()
            data['html_guardian_list'] = render_to_string('guardians/includes/partial_guardian_list.html', {
                'guardians': guardians
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def guardian_create(request, school_id):
    form = GuardianForm(request.POST or None, request.FILES or None)
    school = get_object_or_404(School, pk=school_id)
    if form.is_valid():
        guardian = form
        guardian.school = school
        guardian.save()
        return render(request, 'guardians/guardian_list.html', {'school': school})
    context = {
        'school': school,
        'form': form,
    }
    return render(request, 'guardians/guardian_create.html', context)


def guardian_view(request, pk):
    guardian = get_object_or_404(Guardian, pk=pk)
    if request.method == 'POST':
        form = GuardianForm(request.POST, instance=guardian.user)
    else:
        form = GuardianForm(instance=guardian.user)
    return save_guardian_form(request, form, 'guardians/includes/partial_guardian_view.html')


def guardian_update(request, pk):
    guardian = get_object_or_404(Guardian, pk=pk)
    if request.method == 'POST':
        form = GuardianForm(request.POST, instance=guardian.user)
    else:
        form = GuardianForm(instance=guardian.user)
    return save_guardian_form(request, form, 'guardians/includes/partial_guardian_update.html')


def guardian_delete(request, pk):
    guardian = get_object_or_404(Guardian, pk=pk)
    data = dict()
    if request.method == 'POST':
        guardian.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        guardians = Guardian.objects.all()
        data['html_guardian_list'] = render_to_string('guardians/includes/partial_guardian_list.html', {
            'guardians': guardians
        })
    else:
        context = {'guardian': guardian}
        data['html_form'] = render_to_string('guardians/includes/partial_guardian_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def designation_list(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    designations = school.designation_set.all()
    return render(request, 'designations/designation_list.html', {
        'school': school,
        'designations': designations,
    })


def save_designation_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            designations = Designation.objects.all()
            data['html_designation_list'] = render_to_string('designations/includes/partial_designation_list.html', {
                'designations': designations
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def designation_create(request, school_id):
    form = DesignationForm(request.POST or None, request.FILES or None)
    school = get_object_or_404(School, pk=school_id)
    if form.is_valid():
        designations = school.designation_set.all()
        for cr in designations:
            if cr.designation == form.cleaned_data.get("designation"):
                context = {
                    'school': school,
                    'form': form,
                    'error_message': 'You already added that designation',
                }
                return render(request, 'designations/designation_create.html', context)
        designation = form
        designation.school = school
        designation.save()
        return render(request, 'designations/designation_list.html', {'school': school})
    context = {
        'school': school,
        'form': form,
    }
    return render(request, 'designations/designation_create.html', context)


def designation_view(request, pk):
    designation = get_object_or_404(Designation, pk=pk)
    if request.method == 'POST':
        form = DesignationForm(request.POST, instance=designation)
    else:
        form = DesignationForm(instance=designation)
    return save_designation_form(request, form, 'designations/includes/partial_designation_view.html')


def designation_update(request, pk):
    designation = get_object_or_404(Designation, pk=pk)
    if request.method == 'POST':
        form = DesignationForm(request.POST, instance=designation)
    else:
        form = DesignationForm(instance=designation)
    return save_designation_form(request, form, 'designations/includes/partial_designation_update.html')


def designation_delete(request, pk):
    designation = get_object_or_404(Designation, pk=pk)
    data = dict()
    if request.method == 'POST':
        designation.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        designations = Designation.objects.all()
        data['html_designation_list'] = render_to_string('designations/includes/partial_designation_list.html', {
            'designations': designations
        })
    else:
        context = {'designation': designation}
        data['html_form'] = render_to_string('designations/includes/partial_designation_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def employee_list(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    employees = school.employee_set.all()
    return render(request, 'employees/employee_list.html', {
        'school': school,
        'employees': employees,
    })


def save_employee_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            employees = Employee.objects.all()
            data['html_employee_list'] = render_to_string('employees/includes/partial_employee_list.html', {
                'employees': employees
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def employee_create(request, school_id):
    form = EmployeeForm(request.POST or None, request.FILES or None)
    school = get_object_or_404(School, pk=school_id)
    if form.is_valid():
        school_employees = school.employee_set.all()
        for cr in school_employees:
            if cr.employee.user.full_name == form.cleaned_data.get("full_name"):
                context = {
                    'school': school,
                    'form': form,
                    'error_message': 'You already added that employee',
                }
                return render(request, 'employees/employee_create.html', context)
        employee = form.save(commit=False)
        employee.school = school
        employee.save()
        return render(request, 'employees/employee_list.html', {'school': school})
    context = {
        'school': school,
        'form': form,
    }
    return render(request, 'employees/employee_create.html', context)


def employee_view(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
    else:
        form = EmployeeForm(instance=employee)
    return save_employee_form(request, form, 'employees/includes/partial_employee_view.html')


def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
    else:
        form = EmployeeForm(instance=employee)
    return save_employee_form(request, form, 'employees/includes/partial_employee_update.html')


def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    data = dict()
    if request.method == 'POST':
        employee.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        employees = Employee.objects.all()
        data['html_employee_list'] = render_to_string('employees/includes/partial_employee_list.html', {
            'employees': employees
        })
    else:
        context = {'employee': employee}
        data['html_form'] = render_to_string('employees/includes/partial_employee_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def year_list(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    years = school.year_set.all()
    return render(request, 'years/year_list.html', {
        'school': school,
        'years': years,
    })


def save_year_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            years = Year.objects.all()
            data['html_year_list'] = render_to_string('years/includes/partial_year_list.html', {
                'years': years
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def year_create(request):
    if request.method == 'POST':
        form = YearForm(request.POST)
    else:
        form = YearForm()
    return save_year_form(request, form, 'years/includes/partial_year_create.html')


def year_update(request, pk):
    year = get_object_or_404(Year, pk=pk)
    if request.method == 'POST':
        form = YearForm(request.POST, instance=year)
    else:
        form = YearForm(instance=year)
    return save_year_form(request, form, 'years/includes/partial_year_update.html')


def year_view(request, pk):
    year = get_object_or_404(Year, pk=pk)
    if request.method == 'POST':
        form = YearForm(request.POST, instance=year)
    else:
        form = YearForm(instance=year)
    return save_year_form(request, form, 'years/includes/partial_year_view.html')


def year_delete(request, pk):
    year = get_object_or_404(Year, pk=pk)
    data = dict()
    if request.method == 'POST':
        year.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        years = Year.objects.all()
        data['html_year_list'] = render_to_string('years/includes/partial_year_list.html', {
            'years': years
        })
    else:
        context = {'year': year}
        data['html_form'] = render_to_string('years/includes/partial_year_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def teacher_list(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    school_teachers = school.teacher_set.all()
    return render(request, 'teachers/teacher_list.html', {
        'school': school,
        'school_teachers': school_teachers,
    })


def save_teacher_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            teachers = Teacher.objects.all()
            data['html_teacher_list'] = render_to_string('teachers/includes/partial_teacher_list.html', {
                'teachers': teachers
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def teacher_create(request, school_id):
    form = TeacherForm(request.POST or None, request.FILES or None)
    school = get_object_or_404(School, pk=school_id)
    if form.is_valid():
        school_teachers = school.teacher_set.all()
        for cr in school_teachers:
            if cr.teacher.user.full_name == form.cleaned_data.get("full_name"):
                context = {
                    'school': school,
                    'form': form,
                    'error_message': 'You already added that teacher',
                }
                return render(request, 'teachers/teacher_create.html', context)
        teacher = form.save(commit=False)
        teacher.school = school
        teacher.save()

        school_url = reverse('classroom_list', kwargs={'school_id': school_id})
        return redirect(school_url)

    context = {
        'school': school,
        'form': form,
    }
    return render(request, 'teachers/teacher_create.html', context)


def teacher_view(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher.user)
    else:
        form = TeacherForm(instance=teacher.user)
    return save_teacher_form(request, form, 'teachers/includes/partial_teacher_view.html')


def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher.user)
    else:
        form = TeacherForm(instance=teacher.user)
    return save_teacher_form(request, form, 'teachers/includes/partial_teacher_update.html')


def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    data = dict()
    if request.method == 'POST':
        teacher.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        teachers = Teacher.objects.all()
        data['html_teacher_list'] = render_to_string('teachers/includes/partial_teacher_list.html', {
            'teachers': teachers
        })
    else:
        context = {'teacher': teacher}
        data['html_form'] = render_to_string('teachers/includes/partial_teacher_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def syllabus_list(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    syllabuss = school.syllabus_set.all()
    return render(request, 'syllabus/syllabus_list.html', {
        'school': school,
        'syllabuss': syllabuss,
    })


def save_syllabus_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            syllabuss = Syllabus.objects.all()
            data['html_syllabus_list'] = render_to_string('syllabus/includes/partial_syllabus_list.html', {
                'syllabuss': syllabuss
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def syllabus_create(request, school_id):
    form = SyllabusForm(request.POST or None, request.FILES or None)
    school = get_object_or_404(School, pk=school_id)
    if form.is_valid():
        syllabuss = school.syllabus_set.all()
        for cr in syllabuss:
            if cr.syllabus == form.cleaned_data.get("syllabus"):
                context = {
                    'school': school,
                    'form': form,
                    'error_message': 'You already added that syllabus',
                }
                return render(request, 'syllabus/syllabus_create.html', context)
        syllabus = form.save(commit=False)
        syllabus.school = school
        syllabus.save()
        return render(request, 'syllabus/syllabus_list.html', {'school': school})
    context = {
        'school': school,
        'form': form,
    }
    return render(request, 'syllabus/syllabus_create.html', context)


def syllabus_update(request, pk):
    syllabus = get_object_or_404(Syllabus, pk=pk)
    if request.method == 'POST':
        form = SyllabusForm(request.POST, instance=syllabus)
    else:
        form = SyllabusForm(instance=syllabus)
    return save_syllabus_form(request, form, 'syllabus/includes/partial_syllabus_update.html')


def syllabus_delete(request, pk):
    syllabus = get_object_or_404(Syllabus, pk=pk)
    data = dict()
    if request.method == 'POST':
        syllabus.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        syllabuss = Syllabus.objects.all()
        data['html_syllabus_list'] = render_to_string('syllabus/includes/partial_syllabus_list.html', {
            'syllabuss': syllabuss
        })
    else:
        context = {'syllabus': syllabus}
        data['html_form'] = render_to_string('syllabus/includes/partial_syllabus_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def subject_list(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    subjects = school.subject_set.all()
    return render(request, 'subjects/subject_list.html', {
        'school': school,
        'subjects': subjects,
    })


def save_subject_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            subjects = Subject.objects.all()
            data['html_subject_list'] = render_to_string('subjects/includes/partial_subject_list.html', {
                'subjects': subjects
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def subject_create(request, school_id):
    form = SubjectForm(request.POST or None, request.FILES or None)
    school = get_object_or_404(School, pk=school_id)
    if form.is_valid():
        subjects = school.subject_set.all()
        for cr in subjects:
            if cr.subject == form.cleaned_data.get("subject"):
                context = {
                    'school': school,
                    'form': form,
                    'error_message': 'You already added that subject',
                }
                return render(request, 'subjects/subject_create.html', context)
        subject = form.save(commit=False)
        subject.school = school
        subject.save()
        return render(request, 'subjects/subject_list.html', {'school': school})
    context = {
        'school': school,
        'form': form,
    }
    return render(request, 'subjects/subject_create.html', context)


def subject_update(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
    else:
        form = SubjectForm(instance=subject)
    return save_subject_form(request, form, 'subjects/includes/partial_subject_update.html')


def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    data = dict()
    if request.method == 'POST':
        subject.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        subjects = Subject.objects.all()
        data['html_subject_list'] = render_to_string('subjects/includes/partial_subject_list.html', {
            'subjects': subjects
        })
    else:
        context = {'subject': subject}
        data['html_form'] = render_to_string('subjects/includes/partial_subject_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def routine_list(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    routines = school.routine_set.all()
    return render(request, 'routines/routine_list.html', {
        'school': school,
        'routines': routines,
    })


def save_routine_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            routines = Routine.objects.all()
            data['html_routine_list'] = render_to_string('routines/includes/partial_routine_list.html', {
                'routines': routines
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def routine_create(request, school_id):
    form = RoutineForm(request.POST or None, request.FILES or None)
    school = get_object_or_404(School, pk=school_id)
    if form.is_valid():
        routines = school.routine_set.all()
        for cr in routines:
            if cr.routine == form.cleaned_data.get("routine"):
                context = {
                    'school': school,
                    'form': form,
                    'error_message': 'You already added that routine',
                }
                return render(request, 'routines/routine_create.html', context)
        routine = form.save(commit=False)
        routine.school = school
        routine.save()
        return render(request, 'routines/routine_list.html', {'school': school})
    context = {
        'school': school,
        'form': form,
    }
    return render(request, 'routines/routine_create.html', context)


def routine_update(request, pk):
    routine = get_object_or_404(Routine, pk=pk)
    if request.method == 'POST':
        form = RoutineForm(request.POST, instance=routine)
    else:
        form = RoutineForm(instance=routine)
    return save_routine_form(request, form, 'routines/includes/partial_routine_update.html')


def routine_delete(request, pk):
    routine = get_object_or_404(Routine, pk=pk)
    data = dict()
    if request.method == 'POST':
        routine.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        routines = Routine.objects.all()
        data['html_routine_list'] = render_to_string('routines/includes/partial_routine_list.html', {
            'routines': routines
        })
    else:
        context = {'routine': routine}
        data['html_form'] = render_to_string('routines/includes/partial_routine_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def save_bulk_student_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            bulk_students = BulkStudent.objects.all()
            data['html_bulk_student_list'] = render_to_string('bulk_students/includes/partial_bulk_student_list.html', {
                'bulk_students': bulk_students
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def bulk_student_list(request):
    bulk_students = BulkStudent.objects.all()
    return render(request, 'bulk_students/bulk_student_list.html', {'bulk_students': bulk_students})


def bulk_student_create(request):
    if request.method == 'POST':
        form = BulkStudentForm(request.POST)
    else:
        form = BulkStudentForm()
    return save_bulk_student_form(request, form, 'bulk_students/includes/partial_bulk_student_create.html')


def student_attendance_list(request):
    student_attendance = StudentAttendance.objects.all()
    return render(request, 'attendance/student_attendance_list.html', {'student_attendance': student_attendance})


def teacher_attendance_list(request):
    teacher_attendance = TeacherAttendance.objects.all()
    return render(request, 'attendance/teacher_attendance_list.html', {'teacher_attendance': teacher_attendance})


def employee_attendance_list(request):
    employee_attendance = EmployeeAttendance.objects.all()
    return render(request, 'attendance/employee_attendance_list.html', {'employee_attendance': employee_attendance})


def assignment_list(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    assignments = school.assignment_set.all()
    return render(request, 'assignments/assignment_list.html', {
        'school': school,
        'assignments': assignments,
    })


def save_assignment_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            assignments = Assignment.objects.all()
            data['html_assignment_list'] = render_to_string('assignments/includes/partial_assignment_list.html', {
                'assignments': assignments
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def assignment_create(request, school_id):
    form = AssignmentForm(request.POST or None, request.FILES or None)
    school = get_object_or_404(School, pk=school_id)
    if form.is_valid():
        assignments = school.assignment_set.all()
        for cr in assignments:
            if cr.assignment_title == form.cleaned_data.get("assignment_title"):
                context = {
                    'school': school,
                    'form': form,
                    'error_message': 'You already added that assignment',
                }
                return render(request, 'assignments/assignment_create.html', context)
        assignment = form.save(commit=False)
        assignment.school = school
        assignment.save()
        return render(request, 'assignments/assignment_list.html', {'school': school})
    context = {
        'school': school,
        'form': form,
    }
    return render(request, 'assignments/assignment_create.html', context)


def assignment_update(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment)
    else:
        form = AssignmentForm(instance=assignment)
    return save_assignment_form(request, form, 'assignments/includes/partial_assignment_update.html')


def assignment_delete(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    data = dict()
    if request.method == 'POST':
        assignment.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        assignments = Assignment.objects.all()
        data['html_assignment_list'] = render_to_string('assignments/includes/partial_assignment_list.html', {
            'assignments': assignments
        })
    else:
        context = {'assignment': assignment}
        data['html_form'] = render_to_string('assignments/includes/partial_assignment_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def exam_grade_list(request):
    exam_grades = ExamGrade.objects.all()
    return render(request, 'exam_grades/exam_grade_list.html', {'exam_grades': exam_grades})


def save_exam_grade_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            exam_grades = ExamGrade.objects.all()
            data['html_exam_grade_list'] = render_to_string('exam_grades/includes/partial_exam_grade_list.html', {
                'exam_grades': exam_grades
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def exam_grade_create(request):
    if request.method == 'POST':
        form = ExamGradeForm(request.POST)
    else:
        form = ExamGradeForm()
    return save_exam_grade_form(request, form, 'exam_grades/includes/partial_exam_grade_create.html')


def exam_grade_update(request, pk):
    exam_grade = get_object_or_404(ExamGrade, pk=pk)
    if request.method == 'POST':
        form = ExamGradeForm(request.POST, instance=exam_grade)
    else:
        form = ExamGradeForm(instance=exam_grade)
    return save_exam_grade_form(request, form, 'exam_grades/includes/partial_exam_grade_update.html')


def exam_grade_delete(request, pk):
    exam_grade = get_object_or_404(ExamGrade, pk=pk)
    data = dict()
    if request.method == 'POST':
        exam_grade.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        exam_grades = ExamGrade.objects.all()
        data['html_exam_grade_list'] = render_to_string('exam_grades/includes/partial_exam_grade_list.html', {
            'exam_grades': exam_grades
        })
    else:
        context = {'exam_grade': exam_grade}
        data['html_form'] = render_to_string('exam_grades/includes/partial_exam_grade_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'exams/exam_list.html', {'exams': exams})


def save_exam_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            exams = Exam.objects.all()
            data['html_exam_list'] = render_to_string('exams/includes/partial_exam_list.html', {
                'exams': exams
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def exam_create(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
    else:
        form = ExamForm()
    return save_exam_form(request, form, 'exams/includes/partial_exam_create.html')


def exam_update(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    if request.method == 'POST':
        form = ExamForm(request.POST, instance=exam)
    else:
        form = ExamForm(instance=exam)
    return save_exam_form(request, form, 'exams/includes/partial_exam_update.html')


def exam_delete(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    data = dict()
    if request.method == 'POST':
        exam.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        exams = Exam.objects.all()
        data['html_exam_list'] = render_to_string('exams/includes/partial_exam_list.html', {
            'exams': exams
        })
    else:
        context = {'exam': exam}
        data['html_form'] = render_to_string('exams/includes/partial_exam_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def exam_schedule_list(request):
    exam_schedules = ExamSchedule.objects.all()
    return render(request, 'exam_schedules/exam_schedule_list.html', {'exam_schedules': exam_schedules})


def save_exam_schedule_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            exam_schedules = ExamSchedule.objects.all()
            data['html_exam_schedule_list'] = render_to_string(
                'exam_schedules/includes/partial_exam_schedule_list.html', {
                    'exam_schedules': exam_schedules
                })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def exam_schedule_create(request):
    if request.method == 'POST':
        form = ExamScheduleForm(request.POST)
    else:
        form = ExamScheduleForm()
    return save_exam_schedule_form(request, form, 'exam_schedules/includes/partial_exam_schedule_create.html')


def exam_schedule_update(request, pk):
    exam_schedule = get_object_or_404(ExamSchedule, pk=pk)
    if request.method == 'POST':
        form = ExamScheduleForm(request.POST, instance=exam_schedule)
    else:
        form = ExamScheduleForm(instance=exam_schedule)
    return save_exam_schedule_form(request, form, 'exam_schedules/includes/partial_exam_schedule_update.html')


def exam_schedule_delete(request, pk):
    exam_schedule = get_object_or_404(ExamSchedule, pk=pk)
    data = dict()
    if request.method == 'POST':
        exam_schedule.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        exam_schedules = ExamSchedule.objects.all()
        data['html_exam_schedule_list'] = render_to_string('exam_schedules/includes/partial_exam_schedule_list.html', {
            'exam_schedules': exam_schedules
        })
    else:
        context = {'exam_schedule': exam_schedule}
        data['html_form'] = render_to_string('exam_schedules/includes/partial_exam_schedule_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def exam_suggestion_list(request):
    exam_suggestions = ExamSuggestion.objects.all()
    return render(request, 'exam_suggestions/exam_suggestion_list.html', {'exam_suggestions': exam_suggestions})


def save_exam_suggestion_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            exam_suggestions = ExamSuggestion.objects.all()
            data['html_exam_suggestion_list'] = render_to_string(
                'exam_suggestions/includes/partial_exam_suggestion_list.html', {
                    'exam_suggestions': exam_suggestions
                })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def exam_suggestion_create(request):
    if request.method == 'POST':
        form = ExamSuggestionForm(request.POST)
    else:
        form = ExamSuggestionForm()
    return save_exam_suggestion_form(request, form, 'exam_suggestions/includes/partial_exam_suggestion_create.html')


def exam_suggestion_update(request, pk):
    exam_suggestion = get_object_or_404(ExamSuggestion, pk=pk)
    if request.method == 'POST':
        form = ExamSuggestionForm(request.POST, instance=exam_suggestion)
    else:
        form = ExamSuggestionForm(instance=exam_suggestion)
    return save_exam_suggestion_form(request, form, 'exam_suggestions/includes/partial_exam_suggestion_update.html')


def exam_suggestion_delete(request, pk):
    exam_suggestion = get_object_or_404(ExamSuggestion, pk=pk)
    data = dict()
    if request.method == 'POST':
        exam_suggestion.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        exam_suggestions = ExamSuggestion.objects.all()
        data['html_exam_suggestion_list'] = render_to_string(
            'exam_suggestions/includes/partial_exam_suggestion_list.html', {
                'exam_suggestions': exam_suggestions
            })
    else:
        context = {'exam_suggestion': exam_suggestion}
        data['html_form'] = render_to_string('exam_suggestions/includes/partial_exam_suggestion_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def certificate_list(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    certificates = school.certificatetype_set.all()
    return render(request, 'certificates/certificate_list.html', {
        'school': school,
        'certificates': certificates,
    })


def save_certificate_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            certificates = CertificateType.objects.all()
            data['html_certificate_list'] = render_to_string('certificates/includes/partial_certificate_list.html', {
                'certificates': certificates
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def certificate_create(request, school_id):
    form = CertificateForm(request.POST or None, request.FILES or None)
    school = get_object_or_404(School, pk=school_id)
    if form.is_valid():
        certificates = school.certificatetype_set.all()
        for cr in certificates:
            if cr.certificate_name == form.cleaned_data.get("certificate_name"):
                context = {
                    'school': school,
                    'form': form,
                    'error_message': 'You already added that certificate',
                }
                return render(request, 'certificates/certificate_create.html', context)
        certificate = form.save(commit=False)
        certificate.school = school
        certificate.save()
        return render(request, 'certificates/certificate_list.html', {'school': school})
    context = {
        'school': school,
        'form': form,
    }
    return render(request, 'certificates/certificate_create.html', context)


def certificate_update(request, pk):
    certificate = get_object_or_404(CertificateType, pk=pk)
    if request.method == 'POST':
        form = CertificateForm(request.POST, instance=certificate)
    else:
        form = CertificateForm(instance=certificate)
    return save_certificate_form(request, form, 'certificates/includes/partial_certificate_update.html')


def certificate_delete(request, pk):
    certificate = get_object_or_404(CertificateType, pk=pk)
    data = dict()
    if request.method == 'POST':
        certificate.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        certificates = CertificateType.objects.all()
        data['html_certificate_list'] = render_to_string('certificates/includes/partial_certificate_list.html', {
            'certificates': certificates
        })
    else:
        context = {'certificate': certificate}
        data['html_form'] = render_to_string('certificates/includes/partial_certificate_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def book_list(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    books = school.book_set.all()
    return render(request, 'books/book_list.html', {
        'school': school,
        'books': books,
    })


def save_book_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            books = Book.objects.all()
            data['html_book_list'] = render_to_string('books/includes/partial_book_list.html', {
                'books': books
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def book_create(request, school_id):
    form = BookForm(request.POST or None, request.FILES or None)
    school = get_object_or_404(School, pk=school_id)
    if form.is_valid():
        books = school.book_set.all()
        for cr in books:
            if cr.book_title == form.cleaned_data.get("book_title"):
                context = {
                    'school': school,
                    'form': form,
                    'error_message': 'You already added that book',
                }
                return render(request, 'books/book_create.html', context)
        book = form.save(commit=False)
        book.school = school
        book.save()
        return render(request, 'books/book_list.html', {'school': school})
    context = {
        'school': school,
        'form': form,
    }
    return render(request, 'books/book_create.html', context)


def book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
    else:
        form = BookForm(instance=book)
    return save_book_form(request, form, 'books/includes/partial_book_view.html')


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
    else:
        form = BookForm(instance=book)
    return save_book_form(request, form, 'books/includes/partial_book_update.html')


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    data = dict()
    if request.method == 'POST':
        book.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        books = Book.objects.all()
        data['html_book_list'] = render_to_string('books/includes/partial_book_list.html', {
            'books': books
        })
    else:
        context = {'book': book}
        data['html_form'] = render_to_string('books/includes/partial_book_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def library_member_list(request):
    library_members = LibraryMember.objects.all()
    return render(request, 'library_members/library_member_list.html', {'library_members': library_members})


def save_library_member_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            library_members = LibraryMember.objects.all()
            data['html_library_member_list'] = render_to_string(
                'library_members/includes/partial_library_member_list.html', {
                    'library_members': library_members
                })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def library_member_create(request):
    if request.method == 'POST':
        form = LibraryMemberForm(request.POST)
    else:
        form = LibraryMemberForm()
    return save_library_member_form(request, form, 'library_members/includes/partial_library_member_create.html')


def library_member_update(request, pk):
    library_member = get_object_or_404(LibraryMember, pk=pk)
    if request.method == 'POST':
        form = LibraryMemberForm(request.POST, instance=library_member)
    else:
        form = LibraryMemberForm(instance=library_member)
    return save_library_member_form(request, form, 'library_members/includes/partial_library_member_update.html')


def library_member_delete(request, pk):
    library_member = get_object_or_404(LibraryMember, pk=pk)
    data = dict()
    if request.method == 'POST':
        library_member.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        library_members = LibraryMember.objects.all()
        data['html_library_member_list'] = render_to_string('library_members/includes/partial_library_member_list.html',
                                                            {
                                                                'library_members': library_members
                                                            })
    else:
        context = {'library_member': library_member}
        data['html_form'] = render_to_string('library_members/includes/partial_library_member_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def issue_list(request):
    issues = Issue.objects.all()
    return render(request, 'issues/issue_list.html', {'issues': issues})


def save_issue_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            issues = Issue.objects.all()
            data['html_issue_list'] = render_to_string('issues/includes/partial_issue_list.html', {
                'issues': issues
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def issue_create(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
    else:
        form = IssueForm()
    return save_issue_form(request, form, 'issues/includes/partial_issue_create.html')


def issue_update(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == 'POST':
        form = IssueForm(request.POST, instance=issue)
    else:
        form = IssueForm(instance=issue)
    return save_issue_form(request, form, 'issues/includes/partial_issue_update.html')


def issue_delete(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    data = dict()
    if request.method == 'POST':
        issue.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        issues = Issue.objects.all()
        data['html_issue_list'] = render_to_string('issues/includes/partial_issue_list.html', {
            'issues': issues
        })
    else:
        context = {'issue': issue}
        data['html_form'] = render_to_string('issues/includes/partial_issue_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles/vehicle_list.html', {'vehicles': vehicles})


def save_vehicle_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            vehicles = Vehicle.objects.all()
            data['html_vehicle_list'] = render_to_string('vehicles/includes/partial_vehicle_list.html', {
                'vehicles': vehicles
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def vehicle_create(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
    else:
        form = VehicleForm()
    return save_vehicle_form(request, form, 'vehicles/includes/partial_vehicle_create.html')


def vehicle_update(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
    else:
        form = VehicleForm(instance=vehicle)
    return save_vehicle_form(request, form, 'vehicles/includes/partial_vehicle_update.html')


def vehicle_delete(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    data = dict()
    if request.method == 'POST':
        vehicle.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        vehicles = Vehicle.objects.all()
        data['html_vehicle_list'] = render_to_string('vehicles/includes/partial_vehicle_list.html', {
            'vehicles': vehicles
        })
    else:
        context = {'vehicle': vehicle}
        data['html_form'] = render_to_string('vehicles/includes/partial_vehicle_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def route_list(request):
    routes = Route.objects.all()
    return render(request, 'routes/route_list.html', {'routes': routes})


def save_route_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            routes = Route.objects.all()
            data['html_route_list'] = render_to_string('routes/includes/partial_route_list.html', {
                'routes': routes
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def route_create(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
    else:
        form = RouteForm()
    return save_route_form(request, form, 'routes/includes/partial_route_create.html')


def route_update(request, pk):
    route = get_object_or_404(Route, pk=pk)
    if request.method == 'POST':
        form = RouteForm(request.POST, instance=route)
    else:
        form = RouteForm(instance=route)
    return save_route_form(request, form, 'routes/includes/partial_route_update.html')


def route_delete(request, pk):
    route = get_object_or_404(Route, pk=pk)
    data = dict()
    if request.method == 'POST':
        route.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        routes = Route.objects.all()
        data['html_route_list'] = render_to_string('routes/includes/partial_route_list.html', {
            'routes': routes
        })
    else:
        context = {'route': route}
        data['html_form'] = render_to_string('routes/includes/partial_route_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def transport_member_list(request):
    transport_members = TransportMember.objects.all()
    return render(request, 'transport_members/transport_member_list.html', {'transport_members': transport_members})


def save_transport_member_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            transport_members = TransportMember.objects.all()
            data['html_transport_member_list'] = render_to_string(
                'transport_members/includes/partial_transport_member_list.html', {
                    'transport_members': transport_members
                })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def transport_member_create(request):
    if request.method == 'POST':
        form = TransportMemberForm(request.POST)
    else:
        form = TransportMemberForm()
    return save_transport_member_form(request, form, 'transport_members/includes/partial_transport_member_create.html')


def transport_member_update(request, pk):
    transport_member = get_object_or_404(TransportMember, pk=pk)
    if request.method == 'POST':
        form = TransportMemberForm(request.POST, instance=transport_member)
    else:
        form = TransportMemberForm(instance=transport_member)
    return save_transport_member_form(request, form, 'transport_members/includes/partial_transport_member_update.html')


def transport_member_delete(request, pk):
    transport_member = get_object_or_404(TransportMember, pk=pk)
    data = dict()
    if request.method == 'POST':
        transport_member.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        transport_members = TransportMember.objects.all()
        data['html_transport_member_list'] = render_to_string(
            'transport_members/includes/partial_transport_member_list.html', {
                'transport_members': transport_members
            })
    else:
        context = {'transport_member': transport_member}
        data['html_form'] = render_to_string('transport_members/includes/partial_transport_member_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def hostel_list(request):
    hostels = Hostel.objects.all()
    return render(request, 'hostels/hostel_list.html', {'hostels': hostels})


def save_hostel_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            hostels = Hostel.objects.all()
            data['html_hostel_list'] = render_to_string('hostels/includes/partial_hostel_list.html', {
                'hostels': hostels
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def hostel_create(request):
    if request.method == 'POST':
        form = HostelForm(request.POST)
    else:
        form = HostelForm()
    return save_hostel_form(request, form, 'hostels/includes/partial_hostel_create.html')


def hostel_update(request, pk):
    hostel = get_object_or_404(Hostel, pk=pk)
    if request.method == 'POST':
        form = HostelForm(request.POST, instance=hostel)
    else:
        form = HostelForm(instance=hostel)
    return save_hostel_form(request, form, 'hostels/includes/partial_hostel_update.html')


def hostel_delete(request, pk):
    hostel = get_object_or_404(Hostel, pk=pk)
    data = dict()
    if request.method == 'POST':
        hostel.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        hostels = Hostel.objects.all()
        data['html_hostel_list'] = render_to_string('hostels/includes/partial_hostel_list.html', {
            'hostels': hostels
        })
    else:
        context = {'hostel': hostel}
        data['html_form'] = render_to_string('hostels/includes/partial_hostel_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/room_list.html', {'rooms': rooms})


def save_room_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            rooms = Room.objects.all()
            data['html_room_list'] = render_to_string('rooms/includes/partial_room_list.html', {
                'rooms': rooms
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def room_create(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
    else:
        form = RoomForm()
    return save_room_form(request, form, 'rooms/includes/partial_room_create.html')


def room_update(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
    else:
        form = RoomForm(instance=room)
    return save_room_form(request, form, 'rooms/includes/partial_room_update.html')


def room_delete(request, pk):
    room = get_object_or_404(Room, pk=pk)
    data = dict()
    if request.method == 'POST':
        room.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        rooms = Room.objects.all()
        data['html_room_list'] = render_to_string('rooms/includes/partial_room_list.html', {
            'rooms': rooms
        })
    else:
        context = {'room': room}
        data['html_form'] = render_to_string('rooms/includes/partial_room_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def hostel_member_list(request):
    hostel_members = HostelMember.objects.all()
    return render(request, 'hostel_members/hostel_member_list.html', {'hostel_members': hostel_members})


def save_hostel_member_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            hostel_members = HostelMember.objects.all()
            data['html_hostel_member_list'] = render_to_string(
                'hostel_members/includes/partial_hostel_member_list.html', {
                    'hostel_members': hostel_members
                })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def hostel_member_create(request):
    if request.method == 'POST':
        form = HostelMemberForm(request.POST)
    else:
        form = HostelMemberForm()
    return save_hostel_member_form(request, form, 'hostel_members/includes/partial_hostel_member_create.html')


def hostel_member_update(request, pk):
    hostel_member = get_object_or_404(HostelMember, pk=pk)
    if request.method == 'POST':
        form = HostelMemberForm(request.POST, instance=hostel_member)
    else:
        form = HostelMemberForm(instance=hostel_member)
    return save_hostel_member_form(request, form, 'hostel_members/includes/partial_hostel_member_update.html')


def hostel_member_delete(request, pk):
    hostel_member = get_object_or_404(HostelMember, pk=pk)
    data = dict()
    if request.method == 'POST':
        hostel_member.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        hostel_members = HostelMember.objects.all()
        data['html_hostel_member_list'] = render_to_string('hostel_members/includes/partial_hostel_member_list.html', {
            'hostel_members': hostel_members
        })
    else:
        context = {'hostel_member': hostel_member}
        data['html_form'] = render_to_string('hostel_members/includes/partial_hostel_member_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def email_list(request):
    emails = Email.objects.all()
    return render(request, 'emails/email_list.html', {'emails': emails})


def save_email_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            emails = Email.objects.all()
            data['html_email_list'] = render_to_string('emails/includes/partial_email_list.html', {
                'emails': emails
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def email_create(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
    else:
        form = EmailForm()
    return save_email_form(request, form, 'emails/includes/partial_email_create.html')


def email_update(request, pk):
    email = get_object_or_404(Email, pk=pk)
    if request.method == 'POST':
        form = EmailForm(request.POST, instance=email)
    else:
        form = EmailForm(instance=email)
    return save_email_form(request, form, 'emails/includes/partial_email_update.html')


def email_delete(request, pk):
    email = get_object_or_404(Email, pk=pk)
    data = dict()
    if request.method == 'POST':
        email.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        emails = Email.objects.all()
        data['html_email_list'] = render_to_string('emails/includes/partial_email_list.html', {
            'emails': emails
        })
    else:
        context = {'email': email}
        data['html_form'] = render_to_string('emails/includes/partial_email_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def sms_list(request):
    smss = SMS.objects.all()
    return render(request, 'smss/sms_list.html', {'smss': smss})


def save_sms_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            smss = SMS.objects.all()
            data['html_sms_list'] = render_to_string('smss/includes/partial_sms_list.html', {
                'smss': smss
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def sms_create(request):
    if request.method == 'POST':
        form = SMSForm(request.POST)
    else:
        form = SMSForm()
    return save_sms_form(request, form, 'smss/includes/partial_sms_create.html')


def sms_update(request, pk):
    sms = get_object_or_404(SMS, pk=pk)
    if request.method == 'POST':
        form = SMSForm(request.POST, instance=sms)
    else:
        form = SMSForm(instance=sms)
    return save_sms_form(request, form, 'smss/includes/partial_sms_update.html')


def sms_delete(request, pk):
    sms = get_object_or_404(SMS, pk=pk)
    data = dict()
    if request.method == 'POST':
        sms.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        smss = SMS.objects.all()
        data['html_sms_list'] = render_to_string('smss/includes/partial_sms_list.html', {
            'smss': smss
        })
    else:
        context = {'sms': sms}
        data['html_form'] = render_to_string('smss/includes/partial_sms_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def notice_list(request):
    notices = Notice.objects.all()
    return render(request, 'notices/notice_list.html', {'notices': notices})


def save_notice_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            notices = Notice.objects.all()
            data['html_notice_list'] = render_to_string('notices/includes/partial_notice_list.html', {
                'notices': notices
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def notice_create(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
    else:
        form = NoticeForm()
    return save_notice_form(request, form, 'notices/includes/partial_notice_create.html')


def notice_update(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if request.method == 'POST':
        form = NoticeForm(request.POST, instance=notice)
    else:
        form = NoticeForm(instance=notice)
    return save_notice_form(request, form, 'notices/includes/partial_notice_update.html')


def notice_delete(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    data = dict()
    if request.method == 'POST':
        notice.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        notices = Notice.objects.all()
        data['html_notice_list'] = render_to_string('notices/includes/partial_notice_list.html', {
            'notices': notices
        })
    else:
        context = {'notice': notice}
        data['html_form'] = render_to_string('notices/includes/partial_notice_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def news_list(request):
    newss = News.objects.all()
    return render(request, 'newss/news_list.html', {'newss': newss})


def save_news_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            newss = News.objects.all()
            data['html_news_list'] = render_to_string('newss/includes/partial_news_list.html', {
                'newss': newss
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
    else:
        form = NewsForm()
    return save_news_form(request, form, 'newss/includes/partial_news_create.html')


def news_update(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
    else:
        form = NewsForm(instance=news)
    return save_news_form(request, form, 'newss/includes/partial_news_update.html')


def news_delete(request, pk):
    news = get_object_or_404(News, pk=pk)
    data = dict()
    if request.method == 'POST':
        news.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        newss = News.objects.all()
        data['html_news_list'] = render_to_string('newss/includes/partial_news_list.html', {
            'newss': newss
        })
    else:
        context = {'news': news}
        data['html_form'] = render_to_string('newss/includes/partial_news_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def holiday_list(request):
    holidays = Holiday.objects.all()
    return render(request, 'holidays/holiday_list.html', {'holidays': holidays})


def save_holiday_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            holidays = Holiday.objects.all()
            data['html_holiday_list'] = render_to_string('holidays/includes/partial_holiday_list.html', {
                'holidays': holidays
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def holiday_create(request):
    if request.method == 'POST':
        form = HolidayForm(request.POST)
    else:
        form = HolidayForm()
    return save_holiday_form(request, form, 'holidays/includes/partial_holiday_create.html')


def holiday_update(request, pk):
    holiday = get_object_or_404(Holiday, pk=pk)
    if request.method == 'POST':
        form = HolidayForm(request.POST, instance=holiday)
    else:
        form = HolidayForm(instance=holiday)
    return save_holiday_form(request, form, 'holidays/includes/partial_holiday_update.html')


def holiday_delete(request, pk):
    holiday = get_object_or_404(Holiday, pk=pk)
    data = dict()
    if request.method == 'POST':
        holiday.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        holidays = Holiday.objects.all()
        data['html_holiday_list'] = render_to_string('holidays/includes/partial_holiday_list.html', {
            'holidays': holidays
        })
    else:
        context = {'holiday': holiday}
        data['html_form'] = render_to_string('holidays/includes/partial_holiday_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


def save_event_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            events = Event.objects.all()
            data['html_event_list'] = render_to_string('events/includes/partial_event_list.html', {
                'events': events
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
    else:
        form = EventForm()
    return save_event_form(request, form, 'events/includes/partial_event_create.html')


def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
    else:
        form = EventForm(instance=event)
    return save_event_form(request, form, 'events/includes/partial_event_update.html')


def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    data = dict()
    if request.method == 'POST':
        event.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        events = Event.objects.all()
        data['html_event_list'] = render_to_string('events/includes/partial_event_list.html', {
            'events': events
        })
    else:
        context = {'event': event}
        data['html_form'] = render_to_string('events/includes/partial_event_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def visitor_list(request):
    visitors = Visitor.objects.all()
    return render(request, 'visitors/visitor_list.html', {'visitors': visitors})


def save_visitor_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            visitors = Visitor.objects.all()
            data['html_visitor_list'] = render_to_string('visitors/includes/partial_visitor_list.html', {
                'visitors': visitors
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def visitor_create(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
    else:
        form = VisitorForm()
    return save_visitor_form(request, form, 'visitors/includes/partial_visitor_create.html')


def visitor_update(request, pk):
    visitor = get_object_or_404(Visitor, pk=pk)
    if request.method == 'POST':
        form = VisitorForm(request.POST, instance=visitor)
    else:
        form = VisitorForm(instance=visitor)
    return save_visitor_form(request, form, 'visitors/includes/partial_visitor_update.html')


def visitor_delete(request, pk):
    visitor = get_object_or_404(Visitor, pk=pk)
    data = dict()
    if request.method == 'POST':
        visitor.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        visitors = Visitor.objects.all()
        data['html_visitor_list'] = render_to_string('visitors/includes/partial_visitor_list.html', {
            'visitors': visitors
        })
    else:
        context = {'visitor': visitor}
        data['html_form'] = render_to_string('visitors/includes/partial_visitor_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def salary_grade_list(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    salary_grades = school.salarygrade_set.all()
    return render(request, 'salary_grades/salary_grade_list.html', {
        'school': school,
        'salary_grades': salary_grades,
    })


def save_salary_grade_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            salary_grades = SalaryGrade.objects.all()
            data['html_salary_grade_list'] = render_to_string('salary_grades/includes/partial_salary_grade_list.html', {
                'salary_grades': salary_grades
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def salary_grade_create(request, school_id):
    form = SalaryGradeForm(request.POST or None, request.FILES or None)
    school = get_object_or_404(School, pk=school_id)
    if form.is_valid():
        school_salary_grades = school.salarygrade_set.all()
        for cr in school_salary_grades:
            if cr.grade_name == form.cleaned_data.get("grade_name"):
                context = {
                    'school': school,
                    'form': form,
                    'error_message': 'You already added that salary grade',
                }
                return render(request, 'salary_grades/salary_grade_create.html', context)
        salary_grade = form.save(commit=False)
        salary_grade.school = school
        salary_grade.save()
        return render(request, 'salary_grades/salary_grade_list.html', {'school': school})
    context = {
        'school': school,
        'form': form,
    }
    return render(request, 'salary_grades/salary_grade_create.html', context)


def salary_grade_update(request, school_id):
    salary_grade = get_object_or_404(SalaryGrade, pk=school_id)
    if request.method == 'POST':
        form = SalaryGradeForm(request.POST, instance=salary_grade)
    else:
        form = SalaryGradeForm(instance=salary_grade)
    return save_salary_grade_form(request, form, 'salary_grades/includes/partial_salary_grade_update.html')


def salary_grade_delete(request, school_id):
    salary_grade = get_object_or_404(SalaryGrade, pk=school_id)
    data = dict()
    if request.method == 'POST':
        salary_grade.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        salary_grades = SalaryGrade.objects.all()
        data['html_salary_grade_list'] = render_to_string('salary_grades/includes/partial_salary_grade_list.html', {
            'salary_grades': salary_grades
        })
    else:
        context = {'salary_grade': salary_grade}
        data['html_form'] = render_to_string('salary_grades/includes/partial_salary_grade_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def discount_list(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    discounts = school.discount_set.all()
    return render(request, 'discounts/discount_list.html', {
        'school': school,
        'discounts': discounts,
    })


def save_discount_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            discounts = Discount.objects.all()
            data['html_discount_list'] = render_to_string('discounts/includes/partial_discount_list.html', {
                'discounts': discounts
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def discount_create(request, school_id):
    form = DiscountForm(request.POST or None, request.FILES or None)
    school = get_object_or_404(School, pk=school_id)
    if form.is_valid():
        discounts = school.discount_set.all()
        for cr in discounts:
            if cr.title == form.cleaned_data.get("title"):
                context = {
                    'school': school,
                    'form': form,
                    'error_message': 'You already added that discount',
                }
                return render(request, 'discounts/discount_create.html', context)
        discount = form.save(commit=False)
        discount.school = school
        discount.save()
        return render(request, 'discounts/discount_list.html', {'school': school})
    context = {
        'school': school,
        'form': form,
    }
    return render(request, 'discounts/discount_create.html', context)


def discount_update(request, pk):
    discount = get_object_or_404(Discount, pk=pk)
    if request.method == 'POST':
        form = DiscountForm(request.POST, instance=discount)
    else:
        form = DiscountForm(instance=discount)
    return save_discount_form(request, form, 'discounts/includes/partial_discount_update.html')


def discount_delete(request, pk):
    discount = get_object_or_404(Discount, pk=pk)
    data = dict()
    if request.method == 'POST':
        discount.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        discounts = Discount.objects.all()
        data['html_discount_list'] = render_to_string('discounts/includes/partial_discount_list.html', {
            'discounts': discounts
        })
    else:
        context = {'discount': discount}
        data['html_form'] = render_to_string('discounts/includes/partial_discount_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def fee_type_list(request):
    fee_types = FeeType.objects.all()
    return render(request, 'fee_types/fee_type_list.html', {'fee_types': fee_types})


def save_fee_type_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            fee_types = FeeType.objects.all()
            data['html_fee_type_list'] = render_to_string('fee_types/includes/partial_fee_type_list.html', {
                'fee_types': fee_types
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def fee_type_create(request):
    if request.method == 'POST':
        form = FeeTypeForm(request.POST)
    else:
        form = FeeTypeForm()
    return save_fee_type_form(request, form, 'fee_types/includes/partial_fee_type_create.html')


def fee_type_update(request, pk):
    fee_type = get_object_or_404(FeeType, pk=pk)
    if request.method == 'POST':
        form = FeeTypeForm(request.POST, instance=fee_type)
    else:
        form = FeeTypeForm(instance=fee_type)
    return save_fee_type_form(request, form, 'fee_types/includes/partial_fee_type_update.html')


def fee_type_delete(request, pk):
    fee_type = get_object_or_404(FeeType, pk=pk)
    data = dict()
    if request.method == 'POST':
        fee_type.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        fee_types = FeeType.objects.all()
        data['html_fee_type_list'] = render_to_string('fee_types/includes/partial_fee_type_list.html', {
            'fee_types': fee_types
        })
    else:
        context = {'fee_type': fee_type}
        data['html_form'] = render_to_string('fee_types/includes/partial_fee_type_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoices/invoice_list.html', {'invoices': invoices})


def save_invoice_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            invoices = Invoice.objects.all()
            data['html_invoice_list'] = render_to_string('invoices/includes/partial_invoice_list.html', {
                'invoices': invoices
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def invoice_create(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
    else:
        form = InvoiceForm()
    return save_invoice_form(request, form, 'invoices/includes/partial_invoice_create.html')


def invoice_update(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
    else:
        form = InvoiceForm(instance=invoice)
    return save_invoice_form(request, form, 'invoices/includes/partial_invoice_update.html')


def invoice_delete(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    data = dict()
    if request.method == 'POST':
        invoice.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        invoices = Invoice.objects.all()
        data['html_invoice_list'] = render_to_string('invoices/includes/partial_invoice_list.html', {
            'invoices': invoices
        })
    else:
        context = {'invoice': invoice}
        data['html_form'] = render_to_string('invoices/includes/partial_invoice_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def bulk_invoice_list(request):
    bulk_invoices = BulkInvoice.objects.all()
    return render(request, 'bulk_invoices/bulk_invoice_list.html', {'bulk_invoices': bulk_invoices})


def save_bulk_invoice_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            bulk_invoices = BulkInvoice.objects.all()
            data['html_bulk_invoice_list'] = render_to_string('bulk_invoices/includes/partial_bulk_invoice_list.html', {
                'bulk_invoices': bulk_invoices
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def bulk_invoice_create(request):
    if request.method == 'POST':
        form = BulkInvoiceForm(request.POST)
    else:
        form = BulkInvoiceForm()
    return save_bulk_invoice_form(request, form, 'bulk_invoices/includes/partial_bulk_invoice_create.html')


def bulk_invoice_update(request, pk):
    bulk_invoice = get_object_or_404(BulkInvoice, pk=pk)
    if request.method == 'POST':
        form = BulkInvoiceForm(request.POST, instance=bulk_invoice)
    else:
        form = BulkInvoiceForm(instance=bulk_invoice)
    return save_bulk_invoice_form(request, form, 'bulk_invoices/includes/partial_bulk_invoice_update.html')


def bulk_invoice_delete(request, pk):
    bulk_invoice = get_object_or_404(BulkInvoice, pk=pk)
    data = dict()
    if request.method == 'POST':
        bulk_invoice.delete()
        data['form_is_valid'] = True
        bulk_invoices = BulkInvoice.objects.all()
        data['html_bulk_invoice_list'] = render_to_string('bulk_invoices/includes/partial_bulk_invoice_list.html', {
            'bulk_invoices': bulk_invoices
        })
    else:
        context = {'bulk_invoice': bulk_invoice}
        data['html_form'] = render_to_string('bulk_invoices/includes/partial_bulk_invoice_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def due_fee_email_list(request):
    due_fee_emails = DueFeeEmail.objects.all()
    return render(request, 'due_fee_emails/due_fee_email_list.html', {'due_fee_emails': due_fee_emails})


def save_due_fee_email_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            due_fee_emails = DueFeeEmail.objects.all()
            data['html_due_fee_email_list'] = render_to_string(
                'due_fee_emails/includes/partial_due_fee_email_list.html', {
                    'due_fee_emails': due_fee_emails
                })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def due_fee_email_create(request):
    if request.method == 'POST':
        form = DueFeeEmailForm(request.POST)
    else:
        form = DueFeeEmailForm()
    return save_due_fee_email_form(request, form, 'due_fee_emails/includes/partial_due_fee_email_create.html')


def due_fee_email_update(request, pk):
    due_fee_email = get_object_or_404(DueFeeEmail, pk=pk)
    if request.method == 'POST':
        form = DueFeeEmailForm(request.POST, instance=due_fee_email)
    else:
        form = DueFeeEmailForm(instance=due_fee_email)
    return save_due_fee_email_form(request, form, 'due_fee_emails/includes/partial_due_fee_email_update.html')


def due_fee_email_delete(request, pk):
    due_fee_email = get_object_or_404(DueFeeEmail, pk=pk)
    data = dict()
    if request.method == 'POST':
        due_fee_email.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        due_fee_emails = DueFeeEmail.objects.all()
        data['html_due_fee_email_list'] = render_to_string('due_fee_emails/includes/partial_due_fee_email_list.html', {
            'due_fee_emails': due_fee_emails
        })
    else:
        context = {'due_fee_email': due_fee_email}
        data['html_form'] = render_to_string('due_fee_emails/includes/partial_due_fee_email_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def due_fee_sms_list(request):
    due_fee_smss = DueFeeSMS.objects.all()
    return render(request, 'due_fee_smss/due_fee_sms_list.html', {'due_fee_smss': due_fee_smss})


def save_due_fee_sms_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            due_fee_smss = DueFeeSMS.objects.all()
            data['html_due_fee_sms_list'] = render_to_string('due_fee_smss/includes/partial_due_fee_sms_list.html', {
                'due_fee_smss': due_fee_smss
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def due_fee_sms_create(request):
    if request.method == 'POST':
        form = DueFeeSMSForm(request.POST)
    else:
        form = DueFeeSMSForm()
    return save_due_fee_sms_form(request, form, 'due_fee_smss/includes/partial_due_fee_sms_create.html')


def due_fee_sms_update(request, pk):
    due_fee_sms = get_object_or_404(DueFeeSMS, pk=pk)
    if request.method == 'POST':
        form = DueFeeSMSForm(request.POST, instance=due_fee_sms)
    else:
        form = DueFeeSMSForm(instance=due_fee_sms)
    return save_due_fee_sms_form(request, form, 'due_fee_smss/includes/partial_due_fee_sms_update.html')


def due_fee_sms_delete(request, pk):
    due_fee_sms = get_object_or_404(DueFeeSMS, pk=pk)
    data = dict()
    if request.method == 'POST':
        due_fee_sms.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        due_fee_smss = DueFeeSMS.objects.all()
        data['html_due_fee_sms_list'] = render_to_string('due_fee_smss/includes/partial_due_fee_sms_list.html', {
            'due_fee_smss': due_fee_smss
        })
    else:
        context = {'due_fee_sms': due_fee_sms}
        data['html_form'] = render_to_string('due_fee_smss/includes/partial_due_fee_sms_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def income_head_list(request):
    income_heads = IncomeHead.objects.all()
    return render(request, 'income_heads/income_head_list.html', {'income_heads': income_heads})


def save_income_head_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            income_heads = IncomeHead.objects.all()
            data['html_income_head_list'] = render_to_string('income_heads/includes/partial_income_head_list.html', {
                'income_heads': income_heads
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def income_head_create(request):
    if request.method == 'POST':
        form = IncomeHeadForm(request.POST)
    else:
        form = IncomeHeadForm()
    return save_income_head_form(request, form, 'income_heads/includes/partial_income_head_create.html')


def income_head_update(request, pk):
    income_head = get_object_or_404(IncomeHead, pk=pk)
    if request.method == 'POST':
        form = IncomeHeadForm(request.POST, instance=income_head)
    else:
        form = IncomeHeadForm(instance=income_head)
    return save_income_head_form(request, form, 'income_heads/includes/partial_income_head_update.html')


def income_head_delete(request, pk):
    income_head = get_object_or_404(IncomeHead, pk=pk)
    data = dict()
    if request.method == 'POST':
        income_head.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        income_heads = IncomeHead.objects.all()
        data['html_income_head_list'] = render_to_string('income_heads/includes/partial_income_head_list.html', {
            'income_heads': income_heads
        })
    else:
        context = {'income_head': income_head}
        data['html_form'] = render_to_string('income_heads/includes/partial_income_head_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def income_list(request):
    incomes = Income.objects.all()
    return render(request, 'incomes/income_list.html', {'incomes': incomes})


def save_income_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            incomes = Income.objects.all()
            data['html_income_list'] = render_to_string('incomes/includes/partial_income_list.html', {
                'incomes': incomes
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def income_create(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
    else:
        form = IncomeForm()
    return save_income_form(request, form, 'incomes/includes/partial_income_create.html')


def income_update(request, pk):
    income = get_object_or_404(Income, pk=pk)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
    else:
        form = IncomeForm(instance=income)
    return save_income_form(request, form, 'incomes/includes/partial_income_update.html')


def income_delete(request, pk):
    income = get_object_or_404(Income, pk=pk)
    data = dict()
    if request.method == 'POST':
        income.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        incomes = Income.objects.all()
        data['html_income_list'] = render_to_string('incomes/includes/partial_income_list.html', {
            'incomes': incomes
        })
    else:
        context = {'income': income}
        data['html_form'] = render_to_string('incomes/includes/partial_income_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def expenditure_head_list(request):
    expenditure_heads = ExpenditureHead.objects.all()
    return render(request, 'expenditure_heads/expenditure_head_list.html', {'expenditure_heads': expenditure_heads})


def save_expenditure_head_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            expenditure_heads = ExpenditureHead.objects.all()
            data['html_expenditure_head_list'] = render_to_string(
                'expenditure_heads/includes/partial_expenditure_head_list.html', {
                    'expenditure_heads': expenditure_heads
                })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def expenditure_head_create(request):
    if request.method == 'POST':
        form = ExpenditureHeadForm(request.POST)
    else:
        form = ExpenditureHeadForm()
    return save_expenditure_head_form(request, form, 'expenditure_heads/includes/partial_expenditure_head_create.html')


def expenditure_head_update(request, pk):
    expenditure_head = get_object_or_404(ExpenditureHead, pk=pk)
    if request.method == 'POST':
        form = ExpenditureHeadForm(request.POST, instance=expenditure_head)
    else:
        form = ExpenditureHeadForm(instance=expenditure_head)
    return save_expenditure_head_form(request, form, 'expenditure_heads/includes/partial_expenditure_head_update.html')


def expenditure_head_delete(request, pk):
    expenditure_head = get_object_or_404(ExpenditureHead, pk=pk)
    data = dict()
    if request.method == 'POST':
        expenditure_head.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        expenditure_heads = ExpenditureHead.objects.all()
        data['html_expenditure_head_list'] = render_to_string(
            'expenditure_heads/includes/partial_expenditure_head_list.html', {
                'expenditure_heads': expenditure_heads
            })
    else:
        context = {'expenditure_head': expenditure_head}
        data['html_form'] = render_to_string('expenditure_heads/includes/partial_expenditure_head_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def expenditure_list(request):
    expenditures = Expenditure.objects.all()
    return render(request, 'expenditures/expenditure_list.html', {'expenditures': expenditures})


def save_expenditure_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            expenditures = Expenditure.objects.all()
            data['html_expenditure_list'] = render_to_string('expenditures/includes/partial_expenditure_list.html', {
                'expenditures': expenditures
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def expenditure_create(request):
    if request.method == 'POST':
        form = ExpenditureForm(request.POST)
    else:
        form = ExpenditureForm()
    return save_expenditure_form(request, form, 'expenditures/includes/partial_expenditure_create.html')


def expenditure_update(request, pk):
    expenditure = get_object_or_404(Expenditure, pk=pk)
    if request.method == 'POST':
        form = ExpenditureForm(request.POST, instance=expenditure)
    else:
        form = ExpenditureForm(instance=expenditure)
    return save_expenditure_form(request, form, 'expenditures/includes/partial_expenditure_update.html')


def expenditure_delete(request, pk):
    expenditure = get_object_or_404(Expenditure, pk=pk)
    data = dict()
    if request.method == 'POST':
        expenditure.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        expenditures = Expenditure.objects.all()
        data['html_expenditure_list'] = render_to_string('expenditures/includes/partial_expenditure_list.html', {
            'expenditures': expenditures
        })
    else:
        context = {'expenditure': expenditure}
        data['html_form'] = render_to_string('expenditures/includes/partial_expenditure_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def gallery_list(request):
    gallerys = Gallery.objects.all()
    return render(request, 'gallerys/gallery_list.html', {'gallerys': gallerys})


def save_gallery_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            gallerys = Gallery.objects.all()
            data['html_gallery_list'] = render_to_string('gallerys/includes/partial_gallery_list.html', {
                'gallerys': gallerys
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def gallery_create(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST)
    else:
        form = GalleryForm()
    return save_gallery_form(request, form, 'gallerys/includes/partial_gallery_create.html')


def gallery_update(request, pk):
    gallery = get_object_or_404(Gallery, pk=pk)
    if request.method == 'POST':
        form = GalleryForm(request.POST, instance=gallery)
    else:
        form = GalleryForm(instance=gallery)
    return save_gallery_form(request, form, 'gallerys/includes/partial_gallery_update.html')


def gallery_delete(request, pk):
    gallery = get_object_or_404(Gallery, pk=pk)
    data = dict()
    if request.method == 'POST':
        gallery.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        gallerys = Gallery.objects.all()
        data['html_gallery_list'] = render_to_string('gallerys/includes/partial_gallery_list.html', {
            'gallerys': gallerys
        })
    else:
        context = {'gallery': gallery}
        data['html_form'] = render_to_string('gallerys/includes/partial_gallery_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def image_list(request):
    images = Image.objects.all()
    return render(request, 'images/image_list.html', {'images': images})


def save_image_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            images = Image.objects.all()
            data['html_image_list'] = render_to_string('images/includes/partial_image_list.html', {
                'images': images
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def image_create(request):
    if request.method == 'POST':
        form = ImageForm(request.POST)
    else:
        form = ImageForm()
    return save_image_form(request, form, 'images/includes/partial_image_create.html')


def image_update(request, pk):
    image = get_object_or_404(Image, pk=pk)
    if request.method == 'POST':
        form = ImageForm(request.POST, instance=image)
    else:
        form = ImageForm(instance=image)
    return save_image_form(request, form, 'images/includes/partial_image_update.html')


def image_delete(request, pk):
    image = get_object_or_404(Image, pk=pk)
    data = dict()
    if request.method == 'POST':
        image.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        images = Image.objects.all()
        data['html_image_list'] = render_to_string('images/includes/partial_image_list.html', {
            'images': images
        })
    else:
        context = {'image': image}
        data['html_form'] = render_to_string('images/includes/partial_image_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def page_list(request):
    pages = Page.objects.all()
    return render(request, 'pages/page_list.html', {'pages': pages})


def save_page_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            pages = Page.objects.all()
            data['html_page_list'] = render_to_string('pages/includes/partial_page_list.html', {
                'pages': pages
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def page_create(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
    else:
        form = PageForm()
    return save_page_form(request, form, 'pages/includes/partial_page_create.html')


def page_update(request, pk):
    page = get_object_or_404(Page, pk=pk)
    if request.method == 'POST':
        form = PageForm(request.POST, instance=page)
    else:
        form = PageForm(instance=page)
    return save_page_form(request, form, 'pages/includes/partial_page_update.html')


def page_delete(request, pk):
    page = get_object_or_404(Page, pk=pk)
    data = dict()
    if request.method == 'POST':
        page.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        pages = Page.objects.all()
        data['html_page_list'] = render_to_string('pages/includes/partial_page_list.html', {
            'pages': pages
        })
    else:
        context = {'page': page}
        data['html_form'] = render_to_string('pages/includes/partial_page_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def slider_list(request):
    sliders = Slider.objects.all()
    return render(request, 'sliders/slider_list.html', {'sliders': sliders})


def save_slider_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            sliders = Slider.objects.all()
            data['html_slider_list'] = render_to_string('sliders/includes/partial_slider_list.html', {
                'sliders': sliders
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def slider_create(request):
    if request.method == 'POST':
        form = SliderForm(request.POST)
    else:
        form = SliderForm()
    return save_slider_form(request, form, 'sliders/includes/partial_slider_create.html')


def slider_update(request, pk):
    slider = get_object_or_404(Slider, pk=pk)
    if request.method == 'POST':
        form = SliderForm(request.POST, instance=slider)
    else:
        form = SliderForm(instance=slider)
    return save_slider_form(request, form, 'sliders/includes/partial_slider_update.html')


def slider_delete(request, pk):
    slider = get_object_or_404(Slider, pk=pk)
    data = dict()
    if request.method == 'POST':
        slider.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        sliders = Slider.objects.all()
        data['html_slider_list'] = render_to_string('sliders/includes/partial_slider_list.html', {
            'sliders': sliders
        })
    else:
        context = {'slider': slider}
        data['html_form'] = render_to_string('sliders/includes/partial_slider_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def settings(request):
    return render(request, 'home/settings.html')


def theme(request):
    return render(request, 'home/theme.html')


def language(request):
    return render(request, 'home/language.html')


def student_attendance(request):
    context = {}
    school = request.GET.get('school')
    classroom = request.GET.get('classroom')
    context['form'] = AttendanceForm(school, classroom)
    # Filter
    q = request.GET.get('section')
    if q:
        q = q.replace('.', '')
        students = Student.objects.filter(section=str(q))
        context['students'] = students
    return render(request, 'attendance/student_attendance_list.html', context)


def classrooms_ajax(request):
    school = request.GET.get('school')
    classrooms = Classroom.objects.filter(school=school)
    context = {'classrooms': classrooms}
    return render(request, 'attendance/includes/_classrooms.html', context)


def classrooms_choices_ajax(request):
    school = request.GET.get('school')
    classrooms = Classroom.objects.filter(school=school)
    context = {'classrooms': classrooms}
    return render(request, 'attendance/includes/_classrooms_choices.html', context)


def sections_ajax(request):
    classroom = request.GET.get('classroom')
    sections = Section.objects.filter(classroom=classroom)
    context = {'sections': sections}
    return render(request, 'attendance/includes/_sections.html', context)


def sections_choices_ajax(request):
    classroom = request.GET.get('classroom')
    sections = Section.objects.filter(classroom=classroom)
    context = {'sections': sections}
    return render(request, 'attendance/includes/_sections_choices.html', context)


def invoices(request):
    context = {}
    school = request.GET.get('school')
    classroom = request.GET.get('classroom')
    context['form'] = InvoiceForm(school, classroom)
    # Filter
    q = request.GET.get('section')
    if q:
        q = q.replace('.', '')
        students = Student.objects.filter(section=str(q))
        context['students'] = students
    return render(request, 'invoices/invoice_list.html', context)


def classroom_ajax(request):
    school = request.GET.get('school')
    classrooms = Classroom.objects.filter(school=school)
    context = {'classrooms': classrooms}
    return render(request, 'invoices/includes/_classrooms.html', context)


def classroom_choices_ajax(request):
    school = request.GET.get('school')
    classrooms = Classroom.objects.filter(school=school)
    context = {'classrooms': classrooms}
    return render(request, 'invoices/includes/_classrooms_choices.html', context)


def section_ajax(request):
    classroom = request.GET.get('classroom')
    sections = Section.objects.filter(classroom=classroom)
    context = {'sections': sections}
    return render(request, 'invoices/includes/_sections.html', context)


def section_choices_ajax(request):
    classroom = request.GET.get('classroom')
    sections = Section.objects.filter(classroom=classroom)
    context = {'sections': sections}
    return render(request, 'invoices/includes/_sections_choices.html', context)
