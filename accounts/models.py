from django.db import models
class Login(models.Model):
    username = models.CharField(max_length=130)
    password = models.CharField(max_length=30, blank=True)

class Classinformation(models.Model):
    ClassName = models.CharField(max_length=130)
    ClassTeacher = models.CharField(max_length=30, blank=True)
    TotalStudents = models.CharField(max_length=30, blank=True)
    NumberOfSections = models.CharField(max_length=30, blank=True)
    def __str__(self):
        return self.ClassName

class Sectioninformation(models.Model):
    NameOfClass = models.ForeignKey(Classinformation, on_delete=models.PROTECT, blank=True, null=True)
    SectionName = models.CharField(max_length=130)
    SectionTeacher = models.CharField(max_length=30, blank=True)
    NumberOfStudents = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.SectionName
class Teacher(models.Model):
    Name = models.CharField(max_length=130)
    NationaId = models.CharField(max_length=130)
    Responsibility = models.CharField(max_length=130)
    Address = models.CharField(max_length=130)
    Username = models.CharField(max_length=130)
    Password = models.CharField(max_length=130)

    def __str__(self):
        return self.Name

class Subjects(models.Model):
    choices = (
    ('Compulsory','Compulsory'),('Options','Options')
    )
    Subjectname = models.CharField(max_length=130)
    Subjectcode = models.CharField(max_length=130)
    Author = models.CharField(max_length=130)
    Class = models.ForeignKey(Classinformation, on_delete=models.PROTECT, blank=True, null=True)
    SubjectTeacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, blank=True, null=True)
    Type = models.CharField(max_length=130, choices=choices, blank=False)
    OtherNotes = models.TextField(max_length=200, blank=True)
    def __str__(self):
        return self.Subjectname

class Syllabus(models.Model):
    SyllabusType = models.CharField(max_length=130)
    Class = models.ForeignKey(Classinformation, on_delete=models.PROTECT, blank=True, null=True)
    Subject = models.ForeignKey(Subjects, on_delete=models.PROTECT, blank=True, null=True)
    Syllabus = models.FileField(max_length=130, blank=False)
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
    Teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, blank=True, null=True)
    StartTime = models.CharField(max_length=130, default="11:30 AM")
    EndTime = models.CharField(max_length=130, default="1:30 PM")
    Address = models.CharField(max_length=130)
    RoomNumber = models.CharField(max_length=130)

class Assignment(models.Model):
    School = models.CharField(max_length=130)
    AssignmentType = models.CharField(max_length=130)
    Class = models.ForeignKey(Classinformation, on_delete=models.PROTECT, blank=True, null=True)
    Subject = models.ForeignKey(Subjects, on_delete=models.PROTECT, blank=True, null=True)
    Deadline =models.CharField(max_length=130, blank=False)
    Assignment = models.FileField(max_length=130, blank=False)
    Notes = models.TextField(max_length=100)
    def __str__(self):
        return self.Assignment

class ExamGrade(models.Model):
    School = models.CharField(max_length=130)
    ExamGrade =  models.CharField(max_length=130)
    GradePoint = models.CharField(max_length=130)
    MarkFrom = models.CharField(max_length=130)
    MarkTo = models.CharField(max_length=130)
    Notes = models.TextField(max_length=100)
    def __str__(self):
        return self.ExamGrade

class ExamTerm(models.Model):
    School = models.CharField(max_length=130)
    ExamTitle =  models.CharField(max_length=130)
    StartDate = models.CharField(max_length=130)
    Notes = models.TextField(max_length=100)
    def __str__(self):
        return self.ExamTitle

class ExamSchedule(models.Model):
    School = models.CharField(max_length=130)
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
    School = models.CharField(max_length=130)
    SuggestionTitle = models.CharField(max_length=130)
    Exam = models.ForeignKey(ExamTerm, on_delete=models.PROTECT, blank=True, null=True)
    Class = models.ForeignKey(Classinformation, on_delete=models.PROTECT, blank=True, null=True)
    Subject = models.ForeignKey(Subjects, on_delete=models.PROTECT, blank=True, null=True)
    Suggestion = models.FileField(max_length=130, blank=False)
    Notes = models.TextField(max_length=100)
    def __str__(self):
        return self.Assignment

class Library(models.Model):
    School = models.CharField(max_length=130)
    BookTitle = models.CharField(max_length=130)
    ISBN_no = models.CharField(max_length=130)
    BookId= models.CharField(max_length=130)
    Edition = models.CharField(max_length=130)
    Author= models.CharField(max_length=130)
    Language = models.CharField(max_length=130)
    Price = models.CharField(max_length=130)
    Quantity = models.CharField(max_length=130)
    BookCover =  models.FileField(max_length=130, blank=False)

class Transport(models.Model):
    School = models.CharField(max_length=130)
    VehicleNumber = models.CharField(max_length=130)
    VehicleModel = models.CharField(max_length=130)
    Driver= models.CharField(max_length=130)
    VehicleLicense = models.CharField(max_length=130)
    VehicleContact= models.CharField(max_length=130)
    Notes = models.TextField(max_length=100)
class Route(models.Model):
    School = models.CharField(max_length=130)
    RouteTitle = models.CharField(max_length=130)
    StartRoute = models.CharField(max_length=130)
    EndRoute= models.CharField(max_length=130)
    Notes = models.TextField(max_length=100)
    def __str__(self):
        return self.RouteTitle

class Hostel(models.Model):
    choices = (('Boys','Boys'),('Girls','Girls'),('Combined','Combined'))
    School = models.CharField(max_length=130)
    HostelName= models.CharField(max_length=130)
    HostType = models.CharField(max_length=130, choices=choices, blank=False, null=True)
    Address= models.CharField(max_length=130)
    Notes = models.TextField(max_length=110)
    def __str__(self):
        return self.HostelName

class HostelRooms(models.Model):
    choices = (('AC','AC'),('No AC ','No AC'))
    School = models.CharField(max_length=130)
    Room_no= models.CharField(max_length=130)
    Hostel= models.ForeignKey(Hostel,  on_delete=models.PROTECT, blank=True, null=True)
    RoomType = models.CharField(max_length=130, choices=choices, blank=False, null=True)
    SeatTotal= models.CharField(max_length=130)
    CostPerSeat= models.CharField(max_length=130)
    Notes = models.TextField(max_length=110)
    def __str__(self):
        return self.Room_no
class VisitorInfor(models.Model):
    School = models.CharField(max_length=130)
    Name= models.CharField(max_length=130)
    Phone= models.CharField(max_length=130)
    ComingFrom= models.CharField(max_length=130)
    ToMeetUserType=models.CharField(max_length=130)
    ReasonToMeet=models.CharField(max_length=130)
    Notes = models.TextField(max_length=110)
    def __str__(self):
        return self.Name

class SalaryGrade(models.Model):
    School = models.CharField(max_length=130)
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
        return self.NetSalary

class Discount(models.Model):
    School = models.CharField(max_length=130)
    Title= models.CharField(max_length=130)
    Amount= models.CharField(max_length=130)
    Notes = models.TextField(max_length=110)
    def __str__(self):
        return self.Title

class FeeType(models.Model):
    choices = (('General Fee','General Fee'),('Transport','Transport'),('Hostel','Hostel'))
    School = models.CharField(max_length=130)
    FeeTitle= models.CharField(max_length=130)
    FeeType = models.CharField(max_length=130, choices=choices, blank=False, null=True)
    Notes = models.TextField(max_length=110)
    def __str__(self):
        return self.FeeTitle

class FeeCollection(models.Model):
    fee = (('General Fee','General Fee'),('Transport','Transport'),('Hostel','Hostel'))
    choices = (('Yes','Yes'),('No','No'))
    status = (('Paid','Paid'),('Unpaid','Unpaid'))
    School = models.CharField(max_length=130)
    Class = models.ForeignKey(Classinformation, on_delete=models.PROTECT, blank=True, null=True)
    Student =models.CharField(max_length=130)
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
    School = models.CharField(max_length=130)
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
    School = models.CharField(max_length=130)
    ExpenditureHead=models.CharField(max_length=130, choices=head,  blank=False, null=True)
    ExpenditureMethod=models.CharField(max_length=130, choices=method,  blank=False, null=True)
    Amount = models.CharField(max_length=130)
    Date = models.CharField(max_length=130)
    Notes = models.TextField(max_length=50)
    def __str__(self):
        return self.ExpenditureHead

class Events(models.Model):
    School = models.CharField(max_length=130)
    EventTitle=models.CharField(max_length=130)
    EventFor=models.CharField(max_length=130)
    EventPlace=models.CharField(max_length=130)
    Amount = models.CharField(max_length=130)
    FromDate = models.CharField(max_length=130)
    ToDate = models.CharField(max_length=130)
    Image = models.FileField(max_length=130, blank=False)
    Notes = models.TextField(max_length=50)
    def __str__(self):
        return self.ExpenditureHead

class Notice(models.Model):
    School = models.CharField(max_length=130)
    NoticeTitle=models.CharField(max_length=130)
    NoticeDate=models.CharField(max_length=130, default="02-July-2019")
    NoticeFor=models.CharField(max_length=130)
    Notice=models.TextField(max_length=130)
    def __str__(self):
        return self.NoticeTitle

class News(models.Model):
    School = models.CharField(max_length=130)
    NewsTitle=models.CharField(max_length=130)
    Date=models.CharField(max_length=130, default="02-July-2019")
    Image = models.FileField(max_length=130, blank=False)
    News=models.TextField(max_length=130)
    def __str__(self):
        return self.NewsTitle

class Holiday (models.Model):
    School = models.CharField(max_length=130)
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
    Photo = models.FileField(max_length=130, blank=False)
    Resume = models.FileField(max_length=130, blank=False)
    OtherInfo = models.TextField(max_length=120)
class Student (models.Model):
    sex = (('M','Male'),('F','Female'))
    group = (('A','Arts'),('S','Sciences'))
    blood = (('A-','A-'), ('A+','A+'),('B-','B-'),('B+','B+'),
          ('O+','O+'),('O-','O-'), ('AB-','AB-'), ('AB+','AB-'))
    parent = (('Father','Father'), ('Mother','Mother'),('Brother','Brother'),('Sister','Sister'),
          ('Uncle','Uncle'),('Auntie','Auntie'),  ('Other','Others'))
    Name =  models.CharField(max_length=130)
    AdmissionNo = models.CharField(max_length=130)
    AdmissionDate = models.CharField(max_length=130)
    Gender = models.CharField(max_length=130, choices=sex)
    DateOfBirth = models.CharField(max_length=130)
    BloodType = models.CharField(max_length=130, choices=blood)
    Religion = models.CharField(max_length=130)
    Guardian = models.CharField(max_length=130)
    RelationshipWithGuardian=models.CharField(max_length=130, choices=parent)
    PresentAdress=models.CharField(max_length=130)
    PermanentAddress =models.CharField(max_length=130)
    Phone = models.CharField(max_length=130)
    NationalId = models.CharField(max_length=130)
    Class = models.ForeignKey(Classinformation, on_delete=models.PROTECT, blank=True, null=True)
    Section= models.ForeignKey(Sectioninformation, on_delete=models.PROTECT, blank=True, null=True)
    Group = models.CharField(max_length=130, choices=group)
    RollNo = models.CharField(max_length=130)
    RegistrationNo = models.CharField(max_length=130, blank=False)
    SecondLang = models.CharField(max_length=130, blank=False)
    def __str__(self):
        return self.Name
