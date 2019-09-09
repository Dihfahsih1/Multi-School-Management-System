from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.db import transaction
from schools.models import *


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School

        fields = ('school_name', 'school_code', 'address', 'phone', 'registration_date', 'email_address', 'fax',
                  'footer', 'currency', 'currency_symbol', 'session_start_month', 'session_end_month',
                  'enable_frontend', 'exam_final_result', 'latitude', 'longitude', 'facebook_url', 'twitter_url',
                  'linkedIn_url', 'google_plus_url', 'youtube_url', 'instagram_url', 'pinterest_url', 'status', 'logo',
                  'theme')


class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ('designation', 'note')


class SuperuserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'national_ID', 'phone', 'gender', 'blood_group', 'religion', 'birth_date',
                  'present_address', 'permanent_address', 'email', 'username', 'is_superuser', 'resume',
                  'other_info', 'photo']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_superuser = True
        user.save()
        return user


# # class SuperUserEditForm(UserChangeForm):
# #     class Meta:
# #         model = User
# #
# #         fields = ['first_name', 'last_name', 'national_ID', 'phone', 'gender', 'religion',
# #                   'present_address', 'permanent_address', 'username', 'roles']
#
#
class AdminForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['full_name', 'national_ID', 'phone', 'gender', 'blood_group', 'religion', 'birth_date',
                  'present_address', 'permanent_address', 'email', 'username', 'is_admin', 'resume',
                  'other_info', 'bio', 'photo']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        user.save()
        return user


#
# class AdminProfileForm(forms.ModelForm):
#     class Meta:
#         model = Admin
#
#         fields = ['note',]
#
#
class TeacherForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['full_name', 'national_ID', 'responsibility', 'phone', 'gender', 'blood_group',
                  'religion', 'birth_date', 'present_address', 'permanent_address', 'email', 'username', 'salary_grade',
                  'salary_type', 'roles', 'resume', 'Is_View_on_Web', 'facebook_url', 'linkedIn_url',
                  'twitter_url', 'google_plus_url', 'instagram_url', 'youtube_url', 'pinterest_url', 'other_info',
                  'photo']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        return user


#
# class TeacherProfileForm(forms.ModelForm):
#     class Meta:
#         model = Teacher
#
#         fields = ['note',]
#
#
class EmployeeForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['full_name', 'national_ID', 'designation', 'phone', 'gender', 'blood_group', 'religion',
                  'birth_date', 'present_address', 'permanent_address', 'email', 'username', 'salary_grade',
                  'salary_type', 'is_receptionist', 'resume', 'Is_View_on_Web', 'facebook_url', 'linkedIn_url',
                  'twitter_url', 'google_plus_url', 'instagram_url', 'youtube_url', 'pinterest_url', 'other_info',
                  'photo']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_receptionist = True
        user.save()
        return user


#
#
# class EmployeeProfileForm(forms.ModelForm):
#     class Meta:
#         model = Employee
#
#         fields = ['note',]
#
#
class GuardianForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['full_name', 'phone', 'profession', 'religion', 'present_address', 'permanent_address',
                  'national_ID', 'is_guardian', 'email', 'username', 'other_info', 'photo']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_guardian = True
        user.save()
        return user


class StudentForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('full_name', 'admission_no', 'admission_date', 'birth_date', 'gender', 'blood_group',
                  'religion', 'guardian', 'relation_With_Guardian', 'phone', 'national_ID', 'present_address',
                  'permanent_address', 'classroom', 'section', 'group', 'roll_no', 'registration_no', 'is_student',
                  'discount', 'second_language', 'previous_school', 'previous_class', 'transfer_certificate',
                  'father_name', 'father_phone', 'father_education', 'father_profession', 'father_designation',
                  'father_photo', 'mother_name', 'mother_phone', 'mother_education', 'mother_profession',
                  'mother_designation', 'mother_photo', 'email', 'username', 'health_condition', 'other_info', 'photo')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        return user


#
# class GuardianProfileForm(forms.ModelForm):
#     class Meta:
#         model = Guardian
#
#         fields = ['note',]
#
#
# class StudentForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ['email', 'username', 'roles']
#
#
# class StudentProfileForm(forms.ModelForm):
#     class Meta:
#         model = Student
#
#         fields = ['note',]


class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ('classroom', 'numeric_name', 'class_teacher', 'note')


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ('school', 'section', 'classroom', 'class_teacher', 'note')


class YearForm(forms.ModelForm):
    class Meta:
        model = Year
        fields = ('school', 'year', 'is_running', 'note')


# class EmployeeForm(UserCreationForm):
#     class Meta(UserCreationForm):
#         model = Employee
#         fields = ('school', 'name', 'national_ID', 'designation', 'phone', 'gender', 'blood_group', 'religion',
#                   'birth_date', 'present_address', 'permanent_address', 'email', 'username', 'salary_grade',
#                   'salary_type', 'role', 'resume', 'Is_View_on_Web', 'facebook_url', 'linkedIn_url', 'twitter_url',
#                   'google_plus_url', 'instagram_url', 'youtube_url', 'pinterest_url', 'other_info', 'employee_photo')


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('subject_name', 'subject_code', 'author', 'type', 'classroom', 'subject_teacher', 'note')


class SyllabusForm(forms.ModelForm):
    class Meta:
        model = Syllabus
        fields = ('syllabus_title', 'classroom', 'subject_name', 'syllabus', 'note')


class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ('classroom', 'section', 'subject_name', 'day', 'teacher', 'start_time', 'end_time',
                  'room_no')


# class GuardianForm(UserCreationForm):
#     class Meta(UserCreationForm):
#         model = Guardian
#         fields = ()
#
#

class BulkStudentForm(forms.ModelForm):
    class Meta:
        model = BulkStudent
        fields = ('school', 'classroom', 'section')


class StudentAttendanceForm(forms.ModelForm):
    class Meta:
        model = StudentAttendance
        fields = ('school', 'classroom', 'section', 'date')


class TeacherAttendanceForm(forms.ModelForm):
    class Meta:
        model = StudentAttendance
        fields = ('school', 'date')


class EmployeeAttendanceForm(forms.ModelForm):
    class Meta:
        model = StudentAttendance
        fields = ('school', 'date')


class AbsentEmailForm(forms.ModelForm):
    class Meta:
        model = AbsentEmail
        fields = ('school', 'receiver_type', 'absent_user', 'template', 'absent_date', 'subject', 'email_body')


class AbsentSMSForm(forms.ModelForm):
    class Meta:
        model = AbsentSMS
        fields = ('school', 'receiver_type', 'absent_user', 'template', 'absent_date', 'gateway')


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('school', 'assignment_title', 'classroom', 'subject', 'deadline', 'assignment', 'note')


class ExamGradeForm(forms.ModelForm):
    class Meta:
        model = ExamGrade
        fields = ('school', 'exam_grade', 'grade_point', 'mark_from', 'mark_to', 'note')


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ('school', 'exam_title', 'start_date', 'note')


class ExamScheduleForm(forms.ModelForm):
    class Meta:
        model = ExamSchedule
        fields = ('school', 'exam', 'classroom', 'subject', 'exam_date', 'start_time', 'end_time', 'room_no', 'note')


class ExamSuggestionForm(forms.ModelForm):
    class Meta:
        model = ExamSuggestion
        fields = ('school', 'suggestion_title', 'exam', 'classroom', 'subject', 'suggestion', 'note')


class ExamAttendanceForm(forms.ModelForm):
    class Meta:
        model = ExamAttendance
        fields = ('school', 'exam', 'classroom', 'section', 'subject')


class CertificateForm(forms.ModelForm):
    class Meta:
        model = CertificateType
        fields = ('certificate_name', 'school_name', 'certificate_text', 'footer_left_text',
                  'footer_middle_text', 'footer_right_text', 'background')


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('book_title', 'book_ID', 'ISBN_no', 'edition',
                  'author', 'language', 'price', 'quantity', 'almira_no', 'book_cover')


class LibraryMemberForm(forms.ModelForm):
    class Meta:
        model = LibraryMember
        fields = ('school', 'photo', 'library_ID', 'name', 'classroom', 'section',
                  'roll_no')


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('school', 'select_book', 'ISBN_no', 'edition', 'author', 'language', 'price',
                  'quantity', 'almira_no', 'book_cover', 'return_date', 'library_member')


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('school', 'vehicle_number', 'vehicle_model', 'driver', 'vehicle_licence', 'vehicle_contact', 'note')


class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ('school', 'route_title', 'route_start', 'route_end', 'vehicle_for_route', 'stop_name', 'stop_km',
                  'stop_fare', 'note')


class TransportMemberForm(forms.ModelForm):
    class Meta:
        model = TransportMember
        fields = ('school', 'photo', 'name', 'classroom', 'section', 'roll_no', 'transport_route_name')


class HostelForm(forms.ModelForm):
    class Meta:
        model = Hostel
        fields = ('school', 'hostel_name', 'hostel_type', 'address', 'note')


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('school', 'room_no', 'room_type', 'seat_total', 'hostel', 'cost_per_seat', 'note')


class HostelMemberForm(forms.ModelForm):
    class Meta:
        model = HostelMember
        fields = ('school', 'photo', 'name', 'classroom', 'section', 'roll_no', 'hostel_name', 'room_no',
                  'room_type')


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ('school_name', 'receiver_type', 'receiver', 'subject', 'email_body', 'attachment')


class SMSForm(forms.ModelForm):
    class Meta:
        model = SMS
        fields = ('school', 'receiver_type', 'receiver', 'SMS', 'gateway')


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ('school', 'notice_title', 'date', 'notice_for', 'notice', 'Is_View_on_Web')


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('school', 'news_title', 'date', 'image', 'news', 'Is_View_on_Web')


class HolidayForm(forms.ModelForm):
    class Meta:
        model = Holiday
        fields = ('school', 'holiday_title', 'from_date', 'to_date', 'note', 'Is_View_on_Web')


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('school', 'event_title', 'event_for', 'event_place', 'from_date', 'to_date', 'image', 'note',
                  'Is_View_on_Web')


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ('school', 'name', 'phone', 'coming_from', 'to_meet_user_type', 'to_meet_user', 'reason_to_meet',
                  'check_in', 'check_out', 'note')


class SalaryGradeForm(forms.ModelForm):
    class Meta:
        model = SalaryGrade
        fields = ('grade_name', 'basic_salary', 'house_rent', 'transport_allowance', 'medical_allowance',
                  'over_time_hourly_pay', 'provident_fund', 'hourly_rate', 'total_allowance', 'total_deduction',
                  'gross_salary', 'net_salary', 'note')


class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ('title', 'amount', 'note')


class FeeTypeForm(forms.ModelForm):
    class Meta:
        model = FeeType
        fields = ('school', 'fee_type', 'fee_title', 'note')


class BulkInvoiceForm(forms.ModelForm):
    class Meta:
        model = BulkInvoice
        fields = ('school', 'classroom', 'fee_type', 'student_name', 'is_discount_applicable',
                  'month', 'paid_status', 'note')


class DueFeeEmailForm(forms.ModelForm):
    class Meta:
        model = DueFeeEmail
        fields = ('school', 'receiver_role', 'classroom', 'due_fee_student', 'template',
                  'subject', 'email_body', 'attachment')


class DueFeeSMSForm(forms.ModelForm):
    class Meta:
        model = DueFeeSMS
        fields = ('school', 'receiver_type', 'classroom', 'due_fee_student', 'template',
                  'SMS', 'gateway')


class IncomeHeadForm(forms.ModelForm):
    class Meta:
        model = IncomeHead
        fields = ('school', 'income_head', 'note')


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ('school', 'income_head', 'payment_method', 'amount', 'date', 'note')


class ExpenditureHeadForm(forms.ModelForm):
    class Meta:
        model = ExpenditureHead
        fields = ('school', 'expenditure_head', 'note')


class ExpenditureForm(forms.ModelForm):
    class Meta:
        model = Expenditure
        fields = ('school', 'expenditure_head', 'expenditure_method', 'amount', 'date', 'note')


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('school', 'gallery_title', 'note', 'Is_View_on_Web')


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('school', 'gallery_title', 'gallery_image', 'image_caption')


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ('school', 'page_location', 'page_title', 'page_description', 'page_image')


class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ('school', 'slider_image', 'image_title')


class AttendanceForm(forms.Form):
    school = forms.ModelChoiceField(
        queryset=School.objects.all(),
        required=False
    )

    classroom = forms.ModelChoiceField(
        queryset=Classroom.objects.none(),
        required=False
    )

    section = forms.ModelChoiceField(
        queryset=Section.objects.none(),
        required=False
    )

    class Meta:
        fields = ('school', 'classroom', 'section')

    def __init__(self, school=None, classroom=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['classroom'].queryset = Classroom.objects.filter(school=school)
        if classroom:
            self.fields['section'].queryset = Section.objects.filter(
                classroom=classroom)


class InvoiceForm(forms.Form):
    school = forms.ModelChoiceField(
        queryset=School.objects.all(),
        required=False
    )

    classroom = forms.ModelChoiceField(
        queryset=Classroom.objects.none(),
        required=False
    )

    section = forms.ModelChoiceField(
        queryset=Section.objects.none(),
        required=False
    )

    class Meta:
        fields = ('school', 'classroom', 'section')

    def __init__(self, school=None, classroom=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['classroom'].queryset = Classroom.objects.filter(school=school)
        if classroom:
            self.fields['section'].queryset = Section.objects.filter(
                classroom=classroom)
