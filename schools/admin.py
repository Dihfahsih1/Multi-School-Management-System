from django.contrib import admin
from schools.models import *

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

# Register your models here.
admin.site.site_header = 'Welcome to M.S.M.S Administration Portal'


# Register your models here.
admin.site.register(Year)
admin.site.register(Subject)
admin.site.register(Routine)
admin.site.register(Guardian)
admin.site.register(BulkStudent)
admin.site.register(StudentAttendance)
admin.site.register(TeacherAttendance)
admin.site.register(EmployeeAttendance)
admin.site.register(AbsentEmail)
admin.site.register(AbsentSMS)
admin.site.register(Exam)
admin.site.register(ExamSchedule)
admin.site.register(ExamSuggestion)
admin.site.register(ExamAttendance)
admin.site.register(Promotion)
admin.site.register(CertificateType)
admin.site.register(GenerateCertificate)
admin.site.register(Book)
admin.site.register(LibraryMember)
admin.site.register(Issue)
admin.site.register(Vehicle)
admin.site.register(Route)
admin.site.register(TransportMember)
admin.site.register(Hostel)
admin.site.register(Room)
admin.site.register(HostelMember)
admin.site.register(Email)
admin.site.register(SMS)
admin.site.register(Notice)
admin.site.register(News)
admin.site.register(Holiday)
admin.site.register(Event)
admin.site.register(Visitor)
admin.site.register(SalaryGrade)
admin.site.register(Discount)
admin.site.register(FeeType)
admin.site.register(Invoice)
admin.site.register(DueFeeEmail)
admin.site.register(DueFeeSMS)
admin.site.register(IncomeHead)
admin.site.register(Income)
admin.site.register(ExpenditureHead)
admin.site.register(Expenditure)
admin.site.register(Gallery)
admin.site.register(Image)
admin.site.register(Page)
admin.site.register(Slider)


admin.site.unregister(Group)


# Register your models here.
admin.site.register(Role)
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Superuser)
admin.site.register(Student)
admin.site.register(School)
admin.site.register(Classroom)
admin.site.register(Section)
admin.site.register(Teacher)
admin.site.register(Designation)
admin.site.register(Employee)
