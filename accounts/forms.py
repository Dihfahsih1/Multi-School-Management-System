from django import forms
from .models import *
from django.forms.widgets import RadioSelect
class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ('username', 'password')

class ClassinformationForm(forms.ModelForm):
    class Meta:
        model = Classinformation
        fields = ('ClassName', 'ClassTeacher', 'TotalStudents', 'NumberOfSections')
class EditclassinformationForm(forms.ModelForm):
    class Meta:
        model = Classinformation
        fields = ('ClassName', 'ClassTeacher', 'TotalStudents', 'NumberOfSections')

class SectioninformationForm(forms.ModelForm):
    class Meta:
        model = Sectioninformation
        fields = ('StreamTeacher','NameOfClass','NumberOfStudents', 'SectionName')
class EditsectioninformationForm(forms.ModelForm):
    class Meta:
        model = Sectioninformation
        fields = ('StreamTeacher','NameOfClass', 'SectionName')

class CreateTeacherForm(forms.ModelForm):
    class Meta:
        model = TeachersInformation
        fields = ('Name', 'NationaId', 'Responsibility', 'Gender', 'BloodGroup',
        'Religion', 'DateOfBirth', 'PermanentAddress', 'PresentAddress', 'Email','Resume',
        'Username', 'Password','Salary', 'SalaryType', 'JoiningDate', 'TeacherPhoto', 'OtherInfo')
        widgets = {'JoiningDate': forms.DateTimeInput(attrs={'class': 'datetime-input'})}
class EditTeacherForm(forms.ModelForm):
    class Meta:
        model = TeachersInformation
        fields =('Name', 'Responsibility')

class AddSubjectForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ('Subjectname', 'Subjectcode', 'Author', 'Class', 'SubjectTeacher','Type','OtherNotes')
class EditSubjectForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ('Subjectname', 'Subjectcode', 'Author', 'Class', 'SubjectTeacher','Type','OtherNotes')

class AddSyllabusForm(forms.ModelForm):
    class Meta:
        model = Syllabus
        fields = ('SyllabusType', 'Subject', 'Class', 'Syllabus','Notes')
class EditSyllabusForm(forms.ModelForm):
    class Meta:
        model = Syllabus
        fields = ('SyllabusType', 'Subject', 'Class', 'Syllabus','Notes')

class AddHumanResourceForm(forms.ModelForm):
    class Meta:
        model = HumanResource
        fields = ('Name', 'NationaId', 'Designation', 'Phone','Address', 'Gender', 'Religion')
class EditHumanResourceForm(forms.ModelForm):
    class Meta:
        model = HumanResource
        fields = ('Name', 'Designation', 'Phone','Address')

class AddRoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ('Class', 'Section', 'Subject', 'Day','Teacher', 'StartTime', 'EndTime','Address','RoomNumber')

class EditRoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ('Class', 'Section', 'Subject', 'Day','Teacher', 'StartTime', 'EndTime','Address','RoomNumber')

class AddAssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('School','AssignmentType', 'Subject', 'Class', 'Assignment','Notes')
class EditAssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('School','AssignmentType', 'Subject', 'Class', 'Assignment','Notes')

class AddExamGradeForm(forms.ModelForm):
    class Meta:
        model = ExamGrade
        fields = ('School','ExamGrade', 'GradePoint', 'MarkFrom', 'MarkTo','Notes')
class EditExamGradeForm(forms.ModelForm):
    class Meta:
        model = ExamGrade
        fields = ('School','ExamGrade', 'GradePoint', 'MarkFrom', 'MarkTo','Notes')


class AddExamTermForm(forms.ModelForm):
    class Meta:
        model = ExamTerm
        fields = ('School','ExamTitle', 'StartDate','Notes')
class EditExamTermForm(forms.ModelForm):
    class Meta:
        model = ExamTerm
        fields =('School','ExamTitle', 'StartDate','Notes')
class AddExamScheduleForm(forms.ModelForm):
    class Meta:
        model = ExamSchedule
        fields = ('School','Exam', 'Class', 'Subject', 'ExamDate','StartTime','EndTime','RoomNumber','Notes')
class EditExamScheduleForm(forms.ModelForm):
    class Meta:
        model = ExamSchedule
        fields = ('School','Exam', 'Class', 'Subject', 'ExamDate','StartTime','EndTime','RoomNumber','Notes')

class AddExamSuggestionForm(forms.ModelForm):
    class Meta:
        model = ExamSuggestion
        fields = ('School','SuggestionTitle', 'Class', 'Subject', 'Suggestion','Notes')
class EditExamSuggestionForm(forms.ModelForm):
    class Meta:
        model = ExamSuggestion
        fields = ('School','SuggestionTitle', 'Class', 'Subject', 'Suggestion','Notes')

class AddLibraryBookForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ('School','BookTitle', 'ISBN_no', 'BookId', 'Edition','Author', 'Language', 'Price', 'Quantity','BookCover')
class EditLibraryBookForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ('School','BookTitle', 'ISBN_no', 'BookId', 'Edition','Author', 'Language', 'Price', 'Quantity','BookCover')


class AddVehicleForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = ('School','VehicleNumber', 'VehicleModel', 'Driver', 'VehicleLicense','VehicleContact', 'Notes')
class EditVehicleForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = ('School','VehicleNumber', 'VehicleModel', 'Driver', 'VehicleLicense','VehicleContact', 'Notes')

class AddRouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ('School','RouteTitle', 'StartRoute', 'EndRoute','Notes')
class EditRouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ('School','RouteTitle', 'StartRoute', 'EndRoute','Notes')

class AddHostelForm(forms.ModelForm):
    class Meta:
        model = Hostel
        fields = ('School','HostelName', 'HostType', 'Address','Notes')
class EditHostelForm(forms.ModelForm):
    class Meta:
        model = Hostel
        fields = ('School','HostelName', 'HostType', 'Address','Notes')

class AddHostelRoomForm(forms.ModelForm):
    class Meta:
        model = HostelRooms
        fields = ('School','Room_no','Hostel', 'RoomType', 'CostPerSeat','SeatTotal','Notes')
class EditHostelRoomForm(forms.ModelForm):
    class Meta:
        model = HostelRooms
        fields = ('School','Room_no','Hostel', 'RoomType', 'CostPerSeat','SeatTotal','Notes')

class AddVistorInfoForm(forms.ModelForm):
    class Meta:
        model = VisitorInfor
        fields = ('School','Name','Phone', 'ComingFrom', 'ToMeetUserType','ReasonToMeet','Notes')
class EditVistorInfoForm(forms.ModelForm):
    class Meta:
        model = VisitorInfor
        fields = ('School','Name','Phone', 'ComingFrom', 'ToMeetUserType','ReasonToMeet','Notes')


class AddSalaryGradeForm(forms.ModelForm):
    class Meta:
        model = SalaryGrade
        fields = ('GradeName','BasicSalary', 'HouseRent', 'TransportAllowance','MedicalAllowance',
        'OverTimeHourlyRate', 'ProvidentFund','HourlyRate','TotalAllowance', 'TotalDeduction', 'GrossPay',
        'NetSalary','Notes')
class EditSalaryGradeForm(forms.ModelForm):
    class Meta:
        model = SalaryGrade
        fields = ('GradeName','BasicSalary', 'HouseRent', 'TransportAllowance','MedicalAllowance',
        'OverTimeHourlyRate', 'ProvidentFund','HourlyRate','TotalAllowance', 'TotalDeduction', 'GrossPay',
        'NetSalary','Notes')

class AddDiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ('School','Title','Amount','Notes')
class EditDiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields =('School','Title','Amount','Notes')

class AddFeeTypeForm(forms.ModelForm):
    class Meta:
        model = FeeType
        fields = ('School','FeeType','FeeTitle','Notes')
class EditFeeTypeForm(forms.ModelForm):
    class Meta:
        model = FeeType
        fields = ('School','FeeType','FeeTitle','Notes')

class AddFeeCollectionForm(forms.ModelForm):
    class Meta:
        model = FeeCollection
        fields = ('School','Class','Student','FeeType','FeeAmount','Month','IsApplicableDiscount','PaidStatus','Notes')
class EditFeeCollectionForm(forms.ModelForm):
    class Meta:
        model = FeeCollection
        fields = ('School','Class','Student','FeeType','FeeAmount','Month','IsApplicableDiscount','PaidStatus','Notes')

class AddIncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ('School','IncomeHead','PaymentMethod','Amount','Date','Notes')
class EditIncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ('School','IncomeHead','PaymentMethod','Amount','Date','Notes')

class AddExpenditureForm(forms.ModelForm):
    class Meta:
        model = Expenditure
        fields = ('School','ExpenditureHead','ExpenditureMethod','Amount','Date','Notes')
class EditExpenditureForm(forms.ModelForm):
    class Meta:
        model = Expenditure
        fields = ('School','ExpenditureHead','ExpenditureMethod','Amount','Date','Notes')

class AddEventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('School','EventTitle','EventFor','EventPlace','FromDate','ToDate','Image','Notes')
class EditEventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('School','EventTitle','EventFor','EventPlace','FromDate','ToDate','Image','Notes')

class AddNoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ('School','NoticeTitle','NoticeDate','NoticeFor','Notice')
class EditNoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ('School','NoticeTitle','NoticeDate','NoticeFor','Notice')

class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('School','NewsTitle','Date','Image','News')
class EditNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields =('School','NewsTitle','Date','Image','News')

class AddHolidaysForm(forms.ModelForm):
    class Meta:
        model = Holiday
        fields = ('School','HolidayTitle','FromDate','ToDate','Notes')
class EditHolidaysForm(forms.ModelForm):
    class Meta:
        model = Holiday
        fields =('School','HolidayTitle','FromDate','ToDate','Notes')

class AddProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('Name','Phone','PresentAdress','PermanentAddress','Gender',
        'DateOfBirth','Religion','Email','Photo','Resume', 'OtherInfo')
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('Name','Phone','PresentAdress','PermanentAddress','Gender',
        'DateOfBirth','Religion','Email','Photo','Resume', 'OtherInfo')

class AddSchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('SchoolName','SchoolCode','Address','Phone','DateOfRegistration')

class EditSchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('SchoolName','SchoolCode','Address','Phone','DateOfRegistration')

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = DataStudent
        fields = ('school', 'name', 'username','gender', 'religion','Class','stream', 'admission_no',
                  'admission_date','Guardian','GuardianRelationshipToStudent',
                  'NationaId','phone','PresentAddress','PermanentAddress',
                  'previous_school','previous_class',
                  'FatherName','FatherPhone','FatherProfession','FatherDesignation',
                  'MotherName','MotherPhone','MotherProfession','MotherDesignation',
                  'email','password','health_condition','Transfer_Certificate',
                  'Father_Photo','Student_Photo','Mother_Photo','Birth_Date')

class EditStudentForm(forms.ModelForm):
    class Meta:
        model = DataStudent
        fields = ('name','username','religion','Class','phone', 'PresentAddress','health_condition')
class AddStudentAttendanceForm(forms.ModelForm):
    class Meta:
        model = StudentPresence
        fields = ('Student_Name','Attendance','Attendance_Date')
