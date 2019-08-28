from django.db import models
from django.utils import timezone
from datetime import datetime
class School (models.Model):
    SchoolCode=models.CharField(max_length=130)
    SchoolName=models.CharField(max_length=130)
    Address=models.CharField(max_length=130)
    Phone=models.CharField(max_length=130)
    DateOfRegistration=models.CharField(max_length=130)
    def __str__(self):
        return self.SchoolName
class Guardian(models.Model):
    name = models.CharField(max_length=100, default="guardian name")
    phone = models.CharField(max_length=150, default="phone number")
    profession =  models.CharField(max_length=100, default="career")
    Present_Address = models.CharField(max_length=100, default="current area")
    Permanent_Address = models.CharField(max_length=100, default="home")
    National_Id = models.CharField(max_length=150, default="Use NIN")
    sex = (('female','female'), ('male','male'))
    reli = (('moslem','moslem'), ('Christian','Christian'),('Others','Others'))
    role = (('Brother','Brother'), ('Sister','Sister'), ('Uncle','Uncle'),('Auntie','Auntie'),
    ('Guardian','Guardian'),('Other','Other'))
    religion = models.CharField(max_length=130, choices=reli, blank=False)
    Role = models.CharField(max_length=130, choices=role, default="next of kin",blank=False)
    username = models.CharField(max_length=100)
    gender = models.CharField(max_length=130, choices=sex, blank=False)
    Email= models.CharField(max_length=100, default="email")
    password = models.CharField(max_length=100, default="password")
    Other_Info = models.CharField(max_length=130, default="Notes")
    Photo = models.ImageField(upload_to="gallery", default="text")
    def __str__(self):
        return self.name

class SalaryGrade(models.Model):
    GradeName= models.CharField(max_length=130)
    BasicSalary= models.CharField(max_length=130)
    HouseRent= models.CharField(max_length=130)
    TransportAllowance=models.CharField(max_length=130)
    MedicalAllowance=models.CharField(max_length=130)
    OverTimeHourlyRate= models.CharField(max_length=130)
    ProvidentFund= models.CharField(max_length=130)
    HourlyRate=models.CharField(max_length=130)
    TotalAllowance=models.CharField(max_length=130)
    TotalDeduction= models.CharField(max_length=130)
    GrossPay= models.CharField(max_length=130)
    NetSalary=models.CharField(max_length=130)
    Notes = models.TextField(max_length=110)
    def __str__(self):
        return self.GradeName
class TeachersInformation(models.Model):
    choices = (('female','female'), ('male', 'male'))
    type = (('Monthly','Monthly'), ('hourly', 'hourly'))
    blood= (('A+','A+'), ('A-', 'A-'),('B+','B+'), ('B-', 'B-'),('AB+','AB+'), ('AB-', 'AB-'),
    ('O+','O+'), ('O-', 'O-'))
    responsibility = (('Mathematics','Mathematics'), ('English', 'English'),('History','History'), ('Biology', 'Biology')
    ,('Chemistry','Chemistry'), ('Physics', 'Physics'),('Geography','Geography'), ('Economics', 'Economics'))
    Name = models.CharField(max_length=130)
    NationaId = models.CharField(max_length=130)
    Responsibility = models.CharField(max_length=100, choices=responsibility, blank=False)
    Gender=models.CharField(max_length=10, choices=choices, blank=False, null=True)
    BloodGroup=models.CharField(max_length=10, choices=blood, blank=False, null=True)
    Religion =models.CharField(max_length=130)
    DateOfBirth=models.CharField(max_length=130, default="15-10-1990")
    PermanentAddress=models.CharField(max_length=130)
    PresentAddress=models.CharField(max_length=130 )
    Email=models.CharField(max_length=130)
    Password=models.CharField(max_length=130)
    Username=models.CharField(max_length=130)
    Salary = models.ForeignKey(SalaryGrade, on_delete=models.PROTECT, blank=True, null=True)
    SalaryType =models.CharField(max_length=10, choices=type, blank=False)
    JoiningDate=models.CharField(max_length=130,  default="15-10-1990")
    Resume=models.FileField(upload_to="gallery")
    TeacherPhoto=models.ImageField(upload_to="gallery")
    OtherInfo=models.TextField(max_length=100,  default="Enter Other Notes")
    def __str__(self):
        return self.Name

class Login(models.Model):
    username = models.CharField(max_length=130)
    password = models.CharField(max_length=30, blank=True)

class Classinformation(models.Model):
    nameclass= (('Form_One','Form_One'), ('Form_Two', 'Form_Two'),('Form_Three','Form_Three'), ('Form_Four', 'Form_Four'),
    ('Form_Five_Arts','Form_Five_Arts'), ('Form_Five_Sciences', 'Form_Five_Sciences'),
    ('Form_Five_Six','Form_Six_Arts'), ('Form_Six_Sciences', 'Form_Six_Sciences'))
    ClassName = models.CharField(max_length=130, choices=nameclass, blank=False)
    ClassTeacher = models.ForeignKey(TeachersInformation, on_delete=models.PROTECT, blank=True, null=True)
    TotalStudents = models.CharField(max_length=30, blank=True)
    NumberOfSections = models.CharField(max_length=30, blank=True)
    def __str__(self):
        return self.ClassName

class Sectioninformation(models.Model):
    options = (('A','A'),('B','B'))
    NameOfClass = models.ForeignKey(Classinformation, on_delete=models.PROTECT, blank=True, null=True)
    StreamTeacher = models.ForeignKey(TeachersInformation, on_delete=models.PROTECT, blank=True, null=True)
    SectionName = models.CharField(max_length=130, choices=options, blank=False)
    NumberOfStudents = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.SectionName
class Subjects(models.Model):
    choices = (('Compulsory','Compulsory'),('Optional','Optional'))
    Subjectname = models.CharField(max_length=130)
    Subjectcode = models.CharField(max_length=130)
    Author = models.CharField(max_length=130)
    Class = models.ForeignKey(Classinformation, on_delete=models.PROTECT, blank=True, null=True)
    SubjectTeacher = models.ForeignKey(TeachersInformation, on_delete=models.PROTECT, blank=True, null=True)
    Type = models.CharField(max_length=130, choices=choices, blank=False)
    OtherNotes = models.TextField(max_length=200, blank=True)
    def __str__(self):
        return self.Subjectname

class Syllabus(models.Model):
    SyllabusType = models.CharField(max_length=130)
    Class = models.ForeignKey(Classinformation, on_delete=models.PROTECT, blank=True, null=True)
    Subject = models.ForeignKey(Subjects, on_delete=models.PROTECT, blank=True, null=True)
    Syllabus = models.FileField(upload_to="gallery", default="text")
    Notes = models.TextField(max_length=100)
    def __str__(self):
        return self.Syllabus

class HumanResource(models.Model):
    choices = (('female','female'), ('male', 'male'))
    Name = models.CharField(max_length=130)
    NationaId = models.CharField(max_length=130)
    Designation = models.CharField(max_length=130)
    Phone = models.CharField(max_length=130)
    Gender = models.CharField(max_length=10, choices=choices, blank=False, null=True)
    Address = models.CharField(max_length=130)
    Religion = models.CharField(max_length=130)
    def __str__(self):
        return self.Name

class Routine(models.Model):
    choices = (('Monday','Monday'), ('Tuesday', 'Tuesday'),
     ('Wednesday','Wednesday'), ('Thursday', 'Thursday'),
     ('Friday','Friday'), ('Saturday', 'Saturday'),
     ('Sunday','Sunday'))
    Class = models.ForeignKey(Classinformation, on_delete=models.PROTECT, blank=True, null=True)
    Section = models.ForeignKey(Sectioninformation, on_delete=models.PROTECT, blank=True, null=True)
    Subject = models.ForeignKey(Subjects, on_delete=models.PROTECT, blank=True, null=True)
    Day = models.CharField(max_length=10, choices=choices, blank=False, null=True)
    Teacher = models.ForeignKey(TeachersInformation, on_delete=models.PROTECT, blank=True, null=True)
    StartTime = models.CharField(max_length=130, default="11:30 AM")
    EndTime = models.CharField(max_length=130, default="1:30 PM")
    Address = models.CharField(max_length=130)
    RoomNumber = models.CharField(max_length=130)

class Assignment(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    AssignmentType = models.CharField(max_length=130)
    Class = models.ForeignKey(Classinformation, on_delete=models.PROTECT, blank=True, null=True)
    Subject = models.ForeignKey(Subjects, on_delete=models.PROTECT, blank=True, null=True)
    Deadline =models.CharField(max_length=130, blank=False)
    Assignment = models.FileField(upload_to="gallery", default="text")
    Notes = models.TextField(max_length=100)
    def __str__(self):
        return self.Assignment

class ExamGrade(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    ExamGrade =  models.CharField(max_length=130)
    GradePoint = models.CharField(max_length=130)
    MarkFrom = models.CharField(max_length=130)
    MarkTo = models.CharField(max_length=130)
    Notes = models.TextField(max_length=100)
    def __str__(self):
        return self.ExamGrade

class ExamTerm(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    ExamTitle =  models.CharField(max_length=130)
    StartDate = models.CharField(max_length=130)
    Notes = models.TextField(max_length=100)
    def __str__(self):
        return self.ExamTitle

class ExamSchedule(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    Exam = models.ForeignKey(ExamTerm, on_delete=models.PROTECT, blank=True, null=True)
    Class = models.ForeignKey(Classinformation, on_delete=models.PROTECT, blank=True, null=True)
    Subject = models.ForeignKey(Subjects, on_delete=models.PROTECT, blank=True, null=True)
    ExamDate = models.CharField(max_length=130)
    StartTime = models.CharField(max_length=130)
    EndTime = models.CharField(max_length=130)
    RoomNumber =  models.CharField(max_length=100, blank=True)
    Notes = models.TextField(max_length=100)
    def __str__(self):
        return self.ExamDate
class ExamSuggestion(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    SuggestionTitle = models.CharField(max_length=130)
    Exam = models.ForeignKey(ExamTerm, on_delete=models.PROTECT, blank=True, null=True)
    Class = models.ForeignKey(Classinformation, on_delete=models.PROTECT, blank=True, null=True)
    Subject = models.ForeignKey(Subjects, on_delete=models.PROTECT, blank=True, null=True)
    Suggestion = models.FileField(max_length=130, blank=False)
    Notes = models.TextField(max_length=100)
    def __str__(self):
        return self.Assignment

class Library(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    BookTitle = models.CharField(max_length=130)
    ISBN_no = models.CharField(max_length=130)
    BookId= models.CharField(max_length=130)
    Edition = models.CharField(max_length=130)
    Author= models.CharField(max_length=130)
    Language = models.CharField(max_length=130)
    Price = models.CharField(max_length=130)
    Quantity = models.CharField(max_length=130)
    BookCover =  models.ImageField(upload_to="gallery")

class Transport(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    VehicleNumber = models.CharField(max_length=130)
    VehicleModel = models.CharField(max_length=130)
    Driver= models.CharField(max_length=130)
    VehicleLicense = models.CharField(max_length=130)
    VehicleContact= models.CharField(max_length=130)
    Notes = models.TextField(max_length=100)
class Route(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    RouteTitle = models.CharField(max_length=130)
    StartRoute = models.CharField(max_length=130)
    EndRoute= models.CharField(max_length=130)
    Notes = models.TextField(max_length=100)
    def __str__(self):
        return self.RouteTitle

class Hostel(models.Model):
    choices = (('Boys','Boys'),('Girls','Girls'),('Combined','Combined'))
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    HostelName= models.CharField(max_length=130)
    HostType = models.CharField(max_length=130, choices=choices, blank=False, null=True)
    Address= models.CharField(max_length=130)
    Notes = models.TextField(max_length=110)
    def __str__(self):
        return self.HostelName

class HostelRooms(models.Model):
    choices = (('AC','AC'),('No AC ','No AC'))
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    Room_no= models.CharField(max_length=130)
    Hostel= models.ForeignKey(Hostel,  on_delete=models.PROTECT, blank=True, null=True)
    RoomType = models.CharField(max_length=130, choices=choices, blank=False, null=True)
    SeatTotal= models.CharField(max_length=130)
    CostPerSeat= models.CharField(max_length=130)
    Notes = models.TextField(max_length=110)
    def __str__(self):
        return self.Room_no
class VisitorInfor(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    Name= models.CharField(max_length=130)
    Phone= models.CharField(max_length=130)
    ComingFrom= models.CharField(max_length=130)
    ToMeetUserType=models.CharField(max_length=130)
    ReasonToMeet=models.CharField(max_length=130)
    Notes = models.TextField(max_length=110)
    def __str__(self):
        return self.Name

class Discount(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    Title= models.CharField(max_length=130)
    Percentage= models.CharField(max_length=130)
    Notes = models.TextField(max_length=110)
    def __str__(self):
        return self.Title

class FeeType(models.Model):
    choices = (('General Fee','General Fee'),('Transport','Transport'),('Hostel','Hostel'))
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    FeeTitle= models.CharField(max_length=130)
    FeeType = models.CharField(max_length=130, choices=choices, blank=False, null=True)
    Notes = models.TextField(max_length=110)
    def __str__(self):
        return self.FeeTitle

class DataStudent(models.Model):
    sex = (('female','female'), ('male','male'))
    reli = (('moslem','moslem'), ('Christian','Christian'),('Others','Others'))
    relation = (('Brother','Brother'), ('Sister','Sister'),('Mother','Mother'),
    ('Father','Father'), ('Uncle','Uncle'),('Auntie','Auntie'))
    school = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    religion = models.CharField(max_length=130, choices=reli, blank=False)
    name = models.CharField(max_length=100, default="Student_name")
    username = models.CharField(max_length=100)
    gender = models.CharField(max_length=130, choices=sex, blank=False)
    Class = models.ForeignKey(Classinformation, on_delete=models.PROTECT, blank=True, null=True)
    stream = models.ForeignKey(Sectioninformation, on_delete=models.PROTECT, blank=True, null=True)
    admission_no = models.CharField(max_length=130, default="nypefjhjhd")
    admission_date = models.CharField(max_length=100, default="nyfjhjpd")
    Birth_Date= models.CharField(max_length=100, default="nyfjhjpd")
    Guardian = models.ForeignKey(Guardian,on_delete=models.PROTECT, null=True, blank=True)
    GuardianRelationshipToStudent = models.CharField(max_length=130, choices=relation, default="text",blank=False)
    phone = models.CharField(max_length=150, default="Use NIN")
    NationaId = models.CharField(max_length=150, default="Use NIN")
    PresentAddress = models.CharField(max_length=100, default="current area")
    PermanentAddress = models.CharField(max_length=100, default="home")
    previous_class = models.CharField(max_length=100, default="home")
    previous_school = models.CharField(max_length=100, default="home")
    FatherName = models.CharField(max_length=100, default="text")
    FatherPhone =  models.CharField(max_length=100, default="text")
    FatherProfession =  models.CharField(max_length=100, default="text")
    FatherDesignation = models.CharField(max_length=100, default="text")
    MotherName = models.CharField(max_length=100, default="text")
    MotherPhone =  models.CharField(max_length=100, default="text")
    MotherProfession =  models.CharField(max_length=100, default="text")
    MotherDesignation = models.CharField(max_length=100, default="text")
    email = models.CharField(max_length=100, default="text")
    health_condition = models.CharField(max_length=100, default="text")
    password = models.CharField(max_length=100, default="text")
    Transfer_Certificate = models.ImageField(upload_to="gallery", default="text")
    Father_Photo = models.ImageField(upload_to="gallery", default="text")
    Student_Photo = models.ImageField(upload_to="gallery", default="text")
    Mother_Photo = models.ImageField(upload_to="gallery", default="text")
    def __str__(self):
        return self.name

class StudentPresence(models.Model):
    attend = (('1','Present'), ('0','Absent'))
    Student_Name = models.ForeignKey(DataStudent,on_delete=models.PROTECT, blank=False)
    Attendance=models.CharField(max_length=8, choices=attend,null=True,default="none")
    Attendance_Date = models.DateField(default=timezone.now())
    def __str__(self):
        return self.Student_Name

class FeeCollection(models.Model):
    fee = (('General Fee','General Fee'),('Transport','Transport'),('Hostel','Hostel'))
    choices = (('Yes','Yes'),('No','No'))
    status = (('Paid','Paid'),('Unpaid','Unpaid'))
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    Class = models.ForeignKey(Classinformation, on_delete=models.PROTECT, blank=True, null=True)
    Student_Name = models.ForeignKey(DataStudent,on_delete=models.PROTECT, blank=True, null=True)
    FeeType = models.CharField(max_length=130, choices=fee, blank=False, null=True)
    FeeAmount = models.CharField(max_length=130)
    Month = models.CharField(max_length=130)
    IsApplicableDiscount = models.CharField(max_length=130, choices=choices, blank=False, null=True)
    PaidStatus=models.CharField(max_length=130, choices=status, blank=False, null=True)
    Notes = models.TextField(max_length=60)
    def __str__(self):
        return self.PaidStatus

class Income(models.Model):
    method = (('Cheque','Cheque'),('Cash','Cash'))
    head = (('General','General'),('Others','Others'))
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    IncomeHead=models.CharField(max_length=130, choices=head,  blank=False, null=True)
    PaymentMethod=models.CharField(max_length=130, choices=method,  blank=False, null=True)
    Amount = models.CharField(max_length=130)
    Date = models.CharField(max_length=130)
    Notes = models.TextField(max_length=50)
    def __str__(self):
        return self.IncomeHead

class Expenditure(models.Model):
    method = (('Cheque','Cheque'),('Cash','Cash'))
    head = (('General','General'),('Others','Others'))
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    ExpenditureHead=models.CharField(max_length=130, choices=head,  blank=False, null=True)
    ExpenditureMethod=models.CharField(max_length=130, choices=method,  blank=False, null=True)
    Amount = models.CharField(max_length=130)
    Date = models.CharField(max_length=130)
    Notes = models.TextField(max_length=50)
    def __str__(self):
        return self.ExpenditureHead

class Events(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    EventTitle=models.CharField(max_length=130)
    EventFor=models.CharField(max_length=130)
    EventPlace=models.CharField(max_length=130)
    Amount = models.CharField(max_length=130)
    FromDate = models.CharField(max_length=130)
    ToDate = models.CharField(max_length=130)
    Image = models.ImageField(upload_to="gallery")
    Notes = models.TextField(max_length=50)
    def __str__(self):
        return self.ExpenditureHead

class Notice(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    NoticeTitle=models.CharField(max_length=130)
    NoticeDate=models.CharField(max_length=130, default="02-July-2019")
    NoticeFor=models.CharField(max_length=130)
    Notice=models.TextField(max_length=130)
    def __str__(self):
        return self.NoticeTitle

class News(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    NewsTitle=models.CharField(max_length=130)
    Date=models.CharField(max_length=130, default="02-July-2019")
    Image = models.ImageField(upload_to="gallery")
    News=models.TextField(max_length=130)
    def __str__(self):
        return self.NewsTitle

class Holiday (models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    HolidayTitle=models.CharField(max_length=130)
    FromDate = models.CharField(max_length=130)
    ToDate = models.CharField(max_length=130)
    Notes = models.TextField(max_length=50)
    def __str__(self):
        return self.HolidayTitle
class Profile (models.Model):
    sex = (('female','female'), ('male','male'))
    Name =  models.CharField(max_length=130)
    Phone = models.CharField(max_length=130)
    PresentAdress=models.CharField(max_length=130)
    PermanentAddress =models.CharField(max_length=130)
    Gender = models.CharField(max_length=130, choices=sex, blank=False)
    DateOfBirth = models.CharField(max_length=130)
    Religion = models.CharField(max_length=130)
    Email = models.CharField(max_length=130)
    Photo =models.ImageField(upload_to="gallery")
    Resume = models.ImageField(upload_to="gallery")
    OtherInfo = models.TextField(max_length=120)
    def __str__(self):
        return self.Name
