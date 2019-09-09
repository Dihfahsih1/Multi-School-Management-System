from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser


class School(models.Model):
    school_code = models.CharField(max_length=130)
    school_name = models.CharField(max_length=130)
    address = models.CharField(max_length=130)
    phone = models.CharField(max_length=130)
    registration_date = models.DateField(null=True)
    email_address = models.EmailField(max_length=120)
    fax = models.CharField(max_length=130)
    footer = models.CharField(max_length=130)

    currency = models.CharField(max_length=130)
    currency_symbol = models.CharField(max_length=130)
    START = (('January', 'January'),
             ('February', 'February'),
             ('March', 'March'),
             ('April', 'April'),
             ('May', 'May'),
             ('June', 'June'),
             ('July', 'July'),
             ('August', 'August'),
             ('September', 'September'),
             ('September', 'September'),
             ('September', 'September'),
             ('October', 'October'),
             ('November', 'November'),
             ('December', 'December'))
    session_start_month = models.CharField(max_length=130, blank=False, choices=START)
    END = (
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('September', 'September'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'))
    session_end_month = models.CharField(max_length=130, blank=False, choices=END)
    academic_year = models.CharField(max_length=100, default="")
    OPTIONS = (('Yes', 'Yes'),
               ('No', 'No'))
    enable_frontend = models.CharField(max_length=130, blank=False, choices=OPTIONS)
    RESULTS = (('Average of all exams', 'Average of all exams'),
               ('Only based on final exams', 'Only based on final exams'))
    exam_final_result = models.CharField(max_length=130, blank=False, choices=RESULTS)
    latitude = models.CharField(max_length=130)
    longitude = models.CharField(max_length=130)

    facebook_url = models.CharField(max_length=130)
    twitter_url = models.CharField(max_length=130)
    linkedIn_url = models.CharField(max_length=130)
    google_plus_url = models.CharField(max_length=130)
    youtube_url = models.CharField(max_length=130)
    instagram_url = models.CharField(max_length=130)
    pinterest_url = models.CharField(max_length=130)

    logo = models.FileField(upload_to='avatars/', blank=False)
    STATUS = (('Active', 'Active'),
              ('Inactive', 'Inactive'))
    status = models.CharField(max_length=130, blank=False, choices=STATUS)
    THEMES = (('Black', 'Black'),
              ('Navy Blue', 'Navy Blue'),
              ('Red', 'Red'),
              ('Maroon', 'Maroon'),
              )
    theme = models.CharField(max_length=130, blank=False, choices=THEMES)

    def __str__(self):
        return self.school_name

    class Meta:
        ordering = ('school_name',)
        verbose_name = 'school'
        verbose_name_plural = 'schools'


class User(AbstractUser):
    full_name = models.CharField(max_length=255, blank=False, null=True)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=30, unique=True)
    national_ID = models.CharField(max_length=100, blank=False, null=True)
    phone = models.CharField(max_length=100)
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'))
    gender = models.CharField(max_length=100, blank=False, choices=GENDER)
    ROLE1 = (
        ('Superuser', 'Superuser'),)
    role = models.CharField(max_length=100, blank=False, choices=ROLE1)
    ROLE2 = (
        ('Teacher', 'Teacher'),)
    roles = models.CharField(max_length=100, blank=False, choices=ROLE2)
    ROLES = (('Admin', 'Admin'),
             ('Teacher', 'Teacher'),
             ('Others', 'Others'))
    duty = models.CharField(max_length=100, blank=False, choices=ROLES)
    RELIGIONS = (('Christian', 'Christian'),
                 ('Muslim', 'Muslim'),
                 ('Others', 'Others'))
    religion = models.CharField(max_length=100, blank=False, choices=RELIGIONS)

    present_address = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=100)

    BLOOD = (('A+', 'A+'),
             ('A-', 'A-'),
             ('B+', 'B+'),
             ('B-', 'B-'),
             ('O+', 'O+'),
             ('O-', 'O-'),
             ('AB+', 'AB+'),
             ('AB-', 'AB-'))
    blood_group = models.CharField(max_length=100, blank=False, choices=BLOOD)
    birth_date = models.DateField(null=True, blank=False)
    resume = models.FileField(upload_to='resume/', blank=False)
    bio = models.CharField(max_length=200)

    responsibility = models.CharField(max_length=200)
    salary_grade = models.ForeignKey('SalaryGrade', on_delete=models.CASCADE, blank=False, null=True)
    TYPE = (('Monthly', 'Monthly'),
            ('Hourly', 'Hourly'))
    salary_type = models.CharField(max_length=100, blank=False, choices=TYPE)
    facebook_url = models.CharField(max_length=130)
    twitter_url = models.CharField(max_length=130)
    linkedIn_url = models.CharField(max_length=130)
    google_plus_url = models.CharField(max_length=130)
    youtube_url = models.CharField(max_length=130)
    instagram_url = models.CharField(max_length=130)
    pinterest_url = models.CharField(max_length=130)
    IS = (('Yes', 'Yes'),
          ('No', 'No'))
    Is_View_on_Web = models.CharField(max_length=100, blank=False, choices=IS)

    profession = models.CharField(max_length=100)

    designation = models.ForeignKey('Designation', on_delete=models.CASCADE, blank=False, null=True)

    admission_no = models.CharField(max_length=100)
    admission_date = models.DateField(null=True)
    guardian = models.ForeignKey('Guardian', on_delete=models.CASCADE, blank=False, null=True, related_name='guardians')
    RELATION = (('Father', 'Father'),
                ('Mother', 'Mother'),
                ('Sister', 'Sister'),
                ('Bother', 'Bother'),
                ('Uncle', 'Uncle'),
                ('Maternal Uncle', 'Maternal Uncle'),
                ('Aunt', 'Aunt'),
                ('Other Relative', 'Other Relative'))
    relation_With_Guardian = models.CharField(max_length=100, blank=False, choices=RELATION)
    classroom = models.ForeignKey('Classroom', on_delete=models.CASCADE, blank=False, null=True)
    section = models.ForeignKey('Section', on_delete=models.CASCADE, blank=False, null=True)
    GROUP = (
        ('Science', 'Science'),
        ('Arts', 'Arts'),
        ('Commerce', 'Commerce'))
    group = models.CharField(max_length=100, blank=False, choices=GROUP)
    roll_no = models.CharField(max_length=100)
    registration_no = models.CharField(max_length=100)
    discount = models.CharField(max_length=100)
    second_language = models.CharField(max_length=100)

    previous_school = models.CharField(max_length=100)
    previous_class = models.CharField(max_length=100)
    transfer_certificate = models.FileField(upload_to='certificates/', null=True, blank=False)

    father_name = models.CharField(max_length=100)
    father_phone = models.CharField(max_length=100)
    father_education = models.CharField(max_length=100)
    father_profession = models.CharField(max_length=100)
    father_designation = models.CharField(max_length=100)
    father_photo = models.FileField(upload_to='avatar/', null=True, blank=False)

    mother_name = models.CharField(max_length=100)
    mother_phone = models.CharField(max_length=100)
    mother_education = models.CharField(max_length=100)
    mother_profession = models.CharField(max_length=100)
    mother_designation = models.CharField(max_length=100)
    mother_photo = models.FileField(upload_to='avatar/', null=True, blank=False)
    health_condition = models.CharField(max_length=100)

    other_info = models.TextField(max_length=200)
    photo = models.ImageField(upload_to='avatars/', blank=False)
    is_active = models.BooleanField(default=True)  # can login
    is_staff = models.BooleanField(default=False)  # staff user non superuser
    joining_date = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)

    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_guardian = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_accountant = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)
    is_receptionist = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Designation(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, blank=False, null=True)
    designation = models.CharField(max_length=130)
    note = models.TextField(max_length=300)

    def __str__(self):
        return self.designation


class Superuser(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='superuser')

    def __str__(self):
        return self.user.username


class Admin(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin')

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')

    def __str__(self):
        return self.user.username


class Employee(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')

    def __str__(self):
        return self.user.username


class Guardian(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='guardians')

    def __str__(self):
        return self.user.username


class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if instance.is_superuser:
        Superuser.objects.get_or_create(user=instance)

    elif instance.is_admin:
        Admin.objects.get_or_create(user=instance)

    elif instance.is_teacher:
        Teacher.objects.get_or_create(user=instance)

    elif instance.is_student:
        Student.objects.get_or_create(user=instance)

    elif instance.is_receptionist:
        Employee.objects.get_or_create(user=instance)

    else:
        Guardian.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_user(sender, instance, **kwargs):
    if instance.is_superuser:
        instance.superuser.save()

    elif instance.is_admin:
        instance.admin.save()

    elif instance.is_teacher:
        instance.teacher.save()

    elif instance.is_student:
        instance.student.save()

    elif instance.is_receptionist:
        instance.employee.save()

    else:
        Guardian.objects.get_or_create(user=instance)


class Classroom(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    classroom = models.CharField(max_length=130)
    numeric_name = models.CharField(max_length=130)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=False, null=True)
    note = models.CharField(max_length=130)

    def __str__(self):
        return self.classroom

    class Meta:
        ordering = ('classroom',)
        verbose_name = 'classroom',
        verbose_name_plural = 'classrooms'


class Section(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    section = models.CharField(max_length=130)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, blank=False, null=True)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=False, null=True)
    note = models.CharField(max_length=130)

    def __str__(self):
        return self.section

    class Meta:
        ordering = ('section',)
        verbose_name = 'section'
        verbose_name_plural = 'sections'


class Role(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name


class Year(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    Year = (('July 2020', 'June 2021'),
            ('July 2021', 'June 2022'),
            ('July 2022', 'June 2023'),
            ('July 2023', 'June 2024'),
            )
    year = models.CharField(max_length=130, blank=False, choices=Year)
    is_running = models.BooleanField(default=False)
    note = models.TextField(max_length=300)

    def __str__(self):
        return self.year


class Subject(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    subject_name = models.CharField(max_length=130)
    subject_code = models.CharField(max_length=130)
    author = models.CharField(max_length=130)
    TYPE = (('Mandatory', 'Mandatory'),
            ('Optional', 'Optional'))
    type = models.CharField(max_length=100, blank=False, choices=TYPE)

    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, blank=False, null=True)
    subject_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=False, null=True)
    note = models.TextField(max_length=250)

    def __str__(self):
        return self.subject_name


class Syllabus(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    syllabus_title = models.CharField(max_length=130)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, blank=False, null=True)
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=False, null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, blank=False, null=True)
    syllabus = models.FileField(upload_to='syllabus/', null=True, blank=False)
    note = models.TextField(max_length=250)

    def __str__(self):
        return self.syllabus_title


class Routine(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, blank=False, null=True)
    section = models.CharField(max_length=130)
    subject_name = models.CharField(max_length=130)
    DAYS = (('Saturday', 'Saturday'),
            ('Sunday', 'Sunday'),
            ('Monday', 'Monday'),
            ('Tuesday', 'Tuesday'),
            ('Wednesday', 'Wednesday'),
            ('Thursday', 'Thursday'),
            ('Friday', 'Friday'))
    day = models.CharField(max_length=100, blank=False, choices=DAYS)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=False, null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    room_no = models.CharField(max_length=130)

    def __str__(self):
        return self.start_time


class BulkStudent(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, blank=False, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=False, null=True)


class StudentAttendance(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, blank=False, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=False, null=True)
    date = models.DateField(null=True)


class TeacherAttendance(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    date = models.DateField(null=True)


class EmployeeAttendance(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    date = models.DateField(null=True)


class AbsentEmail(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    PRO = (('Admin', 'Admin'),
           ('Guardian', 'Guardian'),
           ('Student', 'Student'),
           ('Teacher', 'Teacher'),
           ('Accountant', 'Accountant'),
           ('Librarian', 'Librarian'),
           ('Receptionist', 'Receptionist'),
           ('Staff', 'Staff'),
           ('Servant', 'Servant'),
           ('General Accountant', 'General Accountant'))
    receiver_type = models.CharField(max_length=100, blank=False, choices=PRO)
    ABSENTEE = (('Admin', 'Admin'),
                ('Guardian', 'Guardian'),
                ('Student', 'Student'),
                ('Teacher', 'Teacher'),
                ('Accountant', 'Accountant'),
                ('Librarian', 'Librarian'),
                ('Receptionist', 'Receptionist'),
                ('Staff', 'Staff'),
                ('Servant', 'Servant'),
                ('General Accountant', 'General Accountant'))
    absent_user = models.CharField(max_length=100, blank=False, choices=ABSENTEE)
    template = models.CharField(max_length=100)
    absent_date = models.DateField(null=True)
    subject = models.CharField(max_length=100)
    email_body = models.TextField(max_length=300)


class AbsentSMS(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    PRO = (('Admin', 'Admin'),
           ('Guardian', 'Guardian'),
           ('Student', 'Student'),
           ('Teacher', 'Teacher'),
           ('Accountant', 'Accountant'),
           ('Librarian', 'Librarian'),
           ('Receptionist', 'Receptionist'),
           ('Staff', 'Staff'),
           ('Servant', 'Servant'),
           ('General Accountant', 'General Accountant'))
    receiver_type = models.CharField(max_length=100, blank=False, choices=PRO)
    ABSENTEE = (('Admin', 'Admin'),
                ('Guardian', 'Guardian'),
                ('Student', 'Student'),
                ('Teacher', 'Teacher'),
                ('Accountant', 'Accountant'),
                ('Librarian', 'Librarian'),
                ('Receptionist', 'Receptionist'),
                ('Staff', 'Staff'),
                ('Servant', 'Servant'),
                ('General Accountant', 'General Accountant'))
    absent_user = models.CharField(max_length=100, blank=False, choices=ABSENTEE)
    template = models.CharField(max_length=100)
    absent_date = models.DateField(null=True)
    SMS = models.TextField(max_length=300)
    gateway = models.CharField(max_length=100)


class Assignment(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    assignment_title = models.CharField(max_length=100)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, blank=False, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=False, null=True)
    deadline = models.DateField(null=True)
    assignment = models.FileField(upload_to='assignment/', null=True, blank=False)
    note = models.TextField(max_length=300)


class ExamGrade(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    exam_grade = models.CharField(max_length=100)
    grade_point = models.CharField(max_length=100)
    mark_from = models.CharField(max_length=100)
    mark_to = models.CharField(max_length=100)
    note = models.TextField(max_length=300)


class Exam(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    exam_title = models.CharField(max_length=100)
    start_date = models.DateField(null=True)
    note = models.TextField(max_length=300)

    def __str__(self):
        return self.exam_title


class ExamSchedule(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, blank=False, null=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, blank=False, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=False, null=True)
    exam_date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    room_no = models.CharField(max_length=300)
    note = models.TextField(max_length=300)


class ExamSuggestion(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    suggestion_title = models.CharField(max_length=300)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, blank=False, null=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, blank=False, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=False, null=True)
    suggestion = models.FileField(upload_to='suggestion/', null=True, blank=False)
    note = models.TextField(max_length=300)

    def __str__(self):
        return self.suggestion_title


class ExamAttendance(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, blank=False, null=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, blank=False, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=False, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=False, null=True)


class Promotion(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    running_session = models.CharField(max_length=100)
    promote_to_session = models.CharField(max_length=100)
    current_class = models.ForeignKey(Classroom, on_delete=models.CASCADE, blank=False, null=True)
    promote_to_class = models.CharField(max_length=100)


class CertificateType(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    certificate_name = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)
    certificate_text = models.TextField(max_length=400)
    footer_left_text = models.CharField(max_length=100)
    footer_middle_text = models.CharField(max_length=100)
    footer_right_text = models.CharField(max_length=100)
    background = models.FileField(upload_to='background/', null=True, blank=False)

    def __str__(self):
        return self.certificate_name


class GenerateCertificate(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, blank=False, null=True)
    certificate_type = models.ForeignKey(CertificateType, on_delete=models.CASCADE, blank=False, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=False, null=True)


class Book(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    book_title = models.CharField(max_length=100)
    book_ID = models.CharField(max_length=100)
    ISBN_no = models.CharField(max_length=100)
    edition = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    almira_no = models.CharField(max_length=100)
    book_cover = models.FileField(upload_to='cover', blank=False)

    def __str__(self):
        return self.book_ID + " " + "|" + " " + self.book_title


class LibraryMember(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    photo = models.FileField(upload_to='avatar/', null=True, blank=False)
    library_ID = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    classroom = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=100)


class Issue(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    select_book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=False, null=True)
    library_member = models.ForeignKey(LibraryMember, on_delete=models.CASCADE, blank=False, null=True)
    ISBN_no = models.CharField(max_length=100)
    edition = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    almira_no = models.CharField(max_length=100)
    book_cover = models.FileField(upload_to='cover/', null=True, blank=False)
    issue_date = models.DateField(null=True)
    due_date = models.DateField(null=True)
    return_date = models.DateField(null=True)


class Vehicle(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    vehicle_number = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    driver = models.CharField(max_length=100)
    vehicle_licence = models.CharField(max_length=100)
    vehicle_contact = models.CharField(max_length=100)
    note = models.CharField(max_length=100)


class Route(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    route_title = models.CharField(max_length=100)
    route_start = models.CharField(max_length=100)
    route_end = models.CharField(max_length=100)
    vehicle_for_route = models.CharField(max_length=100)
    stop_name = models.CharField(max_length=100)
    stop_km = models.CharField(max_length=100)
    stop_fare = models.CharField(max_length=100)
    note = models.CharField(max_length=100)


class TransportMember(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    photo = models.FileField(upload_to='avatar/', null=True, blank=False)
    name = models.ForeignKey(Student, on_delete=models.CASCADE, blank=False, null=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, blank=False, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=False, null=True)
    roll_no = models.CharField(max_length=100)
    transport_route_name = models.CharField(max_length=100)


class Hostel(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    hostel_name = models.CharField(max_length=100)
    TYPE = (
        ('Single - Boys', 'Single - Boys'),
        ('Single - Girls', 'Single - Girls'),
        ('Mixed', 'Mixed'))
    hostel_type = models.CharField(max_length=100, blank=False, choices=TYPE)
    address = models.CharField(max_length=100)
    note = models.TextField(max_length=300)

    def __str__(self):
        return self.hostel_name


class Room(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    room_no = models.CharField(max_length=100)
    TYPE = (
        ('AC', 'AC'),
        ('Non AC', 'Non AC'))
    room_type = models.CharField(max_length=100, blank=False, choices=TYPE)
    seat_total = models.CharField(max_length=100)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, blank=False, null=True)
    cost_per_seat = models.CharField(max_length=100)
    note = models.TextField(max_length=300)


class HostelMember(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    photo = models.FileField(upload_to='avatar/', null=True, blank=False)
    name = models.ForeignKey(Student, on_delete=models.CASCADE, blank=False, null=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, blank=False, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=False, null=True)
    roll_no = models.CharField(max_length=100)
    hostel_name = models.ForeignKey(Hostel, on_delete=models.CASCADE, blank=False, null=True)
    room_no = models.CharField(max_length=100)
    TYPE = (
        ('AC', 'AC'),
        ('Non AC', 'Non AC'))
    room_type = models.CharField(max_length=100, blank=False, choices=TYPE)


class Email(models.Model):
    school_name = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    PRO = (('Admin', 'Admin'),
           ('Guardian', 'Guardian'),
           ('Student', 'Student'),
           ('Teacher', 'Teacher'),
           ('Accountant', 'Accountant'),
           ('Librarian', 'Librarian'),
           ('Receptionist', 'Receptionist'),
           ('Staff', 'Staff'),
           ('Servant', 'Servant'),
           ('General Accountant', 'General Accountant'))
    receiver_type = models.CharField(max_length=100, blank=False, choices=PRO)
    RECEIPT = (('Admin', 'Admin'),
               ('Guardian', 'Guardian'),
               ('Student', 'Student'),
               ('Teacher', 'Teacher'),
               ('Accountant', 'Accountant'),
               ('Librarian', 'Librarian'),
               ('Receptionist', 'Receptionist'),
               ('Staff', 'Staff'),
               ('Servant', 'Servant'),
               ('General Accountant', 'General Accountant'))
    receiver = models.CharField(max_length=100, blank=False, choices=RECEIPT)
    subject = models.CharField(max_length=100)
    email_body = models.TextField(max_length=300)
    attachment = models.FileField(upload_to='attachment/', null=True, blank=False)


class SMS(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    PRO = (('Admin', 'Admin'),
           ('Guardian', 'Guardian'),
           ('Student', 'Student'),
           ('Teacher', 'Teacher'),
           ('Accountant', 'Accountant'),
           ('Librarian', 'Librarian'),
           ('Receptionist', 'Receptionist'),
           ('Staff', 'Staff'),
           ('Servant', 'Servant'),
           ('General Accountant', 'General Accountant'))
    receiver_type = models.CharField(max_length=100, blank=False, choices=PRO)
    RECEIPT = (('Admin', 'Admin'),
               ('Guardian', 'Guardian'),
               ('Student', 'Student'),
               ('Teacher', 'Teacher'),
               ('Accountant', 'Accountant'),
               ('Librarian', 'Librarian'),
               ('Receptionist', 'Receptionist'),
               ('Staff', 'Staff'),
               ('Servant', 'Servant'),
               ('General Accountant', 'General Accountant'))
    receiver = models.CharField(max_length=100, blank=False, choices=RECEIPT)
    SMS = models.TextField(max_length=300)
    gateway = models.CharField(max_length=100)


class Notice(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    notice_title = models.CharField(max_length=100)
    date = models.DateField(null=True)
    PRO = (('Admin', 'Admin'),
           ('Guardian', 'Guardian'),
           ('Student', 'Student'),
           ('Teacher', 'Teacher'),
           ('Accountant', 'Accountant'),
           ('Librarian', 'Librarian'),
           ('Receptionist', 'Receptionist'),
           ('Staff', 'Staff'),
           ('Servant', 'Servant'),
           ('General Accountant', 'General Accountant'))
    notice_for = models.CharField(max_length=100, blank=False, choices=PRO)
    notice = models.TextField(max_length=300)
    IS = (('Yes', 'Yes'),
          ('No', 'No'))
    Is_View_on_Web = models.CharField(max_length=100, blank=False, choices=IS)


class News(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    news_title = models.CharField(max_length=100)
    date = models.DateField(null=True)
    image = models.FileField(upload_to='images/', null=True, blank=False)
    news = models.TextField(max_length=300)
    IS = (('Yes', 'Yes'),
          ('No', 'No'))
    Is_View_on_Web = models.CharField(max_length=100, blank=False, choices=IS)


class Holiday(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    holiday_title = models.CharField(max_length=100)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)
    note = models.TextField(max_length=300)
    IS = (('Yes', 'Yes'),
          ('No', 'No'))
    Is_View_on_Web = models.CharField(max_length=100, blank=False, choices=IS)


class Event(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    event_title = models.CharField(max_length=100)
    PRO = (('Admin', 'Admin'),
           ('Guardian', 'Guardian'),
           ('Student', 'Student'),
           ('Teacher', 'Teacher'),
           ('Accountant', 'Accountant'),
           ('Librarian', 'Librarian'),
           ('Receptionist', 'Receptionist'),
           ('Staff', 'Staff'),
           ('Servant', 'Servant'),
           ('General Accountant', 'General Accountant'))
    event_for = models.CharField(max_length=100, blank=False, choices=PRO)
    event_place = models.CharField(max_length=100)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)
    image = models.FileField(upload_to='images/', null=True, blank=False)
    note = models.TextField(max_length=300)
    IS = (('Yes', 'Yes'),
          ('No', 'No'))
    Is_View_on_Web = models.CharField(max_length=100, blank=False, choices=IS)


class Visitor(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    coming_from = models.CharField(max_length=100)
    PRO = (('Admin', 'Admin'),
           ('Guardian', 'Guardian'),
           ('Student', 'Student'),
           ('Teacher', 'Teacher'),
           ('Accountant', 'Accountant'),
           ('Librarian', 'Librarian'),
           ('Receptionist', 'Receptionist'),
           ('Staff', 'Staff'),
           ('Servant', 'Servant'),
           ('General Accountant', 'General Accountant'))
    to_meet_user_type = models.CharField(max_length=100, blank=False, choices=PRO)
    to_meet_user = models.CharField(max_length=100)
    PRO = (('Vendor', 'Vendor'),
           ('Guardian', 'Guardian'),
           ('Relative', 'Relative'),
           ('Friend', 'Friend'),
           ('Family', 'Family'),
           ('Interview', 'Interview'),
           ('Meeting', 'Meeting'),
           ('Other', 'Other'))
    reason_to_meet = models.CharField(max_length=100, blank=False, choices=PRO)
    check_in = models.TimeField(null=True)
    check_out = models.TimeField(null=True)

    note = models.TextField(max_length=300)


class SalaryGrade(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    grade_name = models.CharField(max_length=100)
    basic_salary = models.CharField(max_length=100)
    house_rent = models.CharField(max_length=100)
    transport_allowance = models.CharField(max_length=100)
    medical_allowance = models.CharField(max_length=100)
    over_time_hourly_pay = models.CharField(max_length=100)
    provident_fund = models.CharField(max_length=100)
    hourly_rate = models.CharField(max_length=100)
    total_allowance = models.CharField(max_length=100)
    total_deduction = models.CharField(max_length=100)
    gross_salary = models.CharField(max_length=100)
    net_salary = models.CharField(max_length=100)
    note = models.TextField(null=True, blank=False)

    def __str__(self):
        return self.grade_name


class Discount(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    title = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    note = models.TextField(max_length=300)


class FeeType(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    IS = (('General Fee', 'General Fee'),
          ('Hostel', 'Hostel'),
          ('Transport', 'Transport'))
    fee_type = models.CharField(max_length=100, blank=False, choices=IS)

    fee_title = models.CharField(max_length=100)
    note = models.TextField(max_length=300)


class Invoice(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, blank=False, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=False, null=True)
    fee_type = models.CharField(max_length=100)
    fee_amount = models.CharField(max_length=100)
    discount = models.CharField(max_length=100)
    month = models.DateField(max_length=100)
    IS = (('Yes', 'Yes'),
          ('No', 'No'))
    is_discount_applicable = models.CharField(max_length=100, blank=False, choices=IS)
    STATUS = (('Paid', 'Paid'),
              ('Pending', 'Pending'))
    paid_status = models.CharField(max_length=100, blank=False, choices=STATUS)
    gross_amount = models.CharField(max_length=100)
    invoice_number = models.CharField(max_length=100)
    note = models.TextField(max_length=300)
    date = models.DateField(null=True)


class BulkInvoice(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, blank=False, null=True)
    fee_type = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    IS = (('Yes', 'Yes'),
          ('No', 'No'))
    is_discount_applicable = models.CharField(max_length=100, blank=False, choices=IS)
    month = models.DateField(max_length=100)
    STATUS = (('Paid', 'Paid'),
              ('Pending', 'Pending'))
    paid_status = models.CharField(max_length=100, blank=False, choices=STATUS)
    note = models.TextField(max_length=300)


class DueFeeEmail(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    PRO = (('Guardian', 'Guardian'),
           ('Student', 'Student'))
    receiver_role = models.CharField(max_length=100, blank=False, choices=PRO)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, blank=False, null=True)

    due_fee_student = models.CharField(max_length=100)
    template = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email_body = models.TextField(max_length=300)
    attachment = models.FileField(upload_to='attachment/', null=True, blank=False)


class DueFeeSMS(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    PRO = (('Guardian', 'Guardian'),
           ('Student', 'Student'))
    receiver_type = models.CharField(max_length=100, blank=False, choices=PRO)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, blank=False, null=True)
    due_fee_student = models.CharField(max_length=100)
    template = models.CharField(max_length=100)
    SMS = models.TextField(max_length=300)
    gateway = models.CharField(max_length=100)


class IncomeHead(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    income_head = models.CharField(max_length=100)
    note = models.TextField(max_length=300)


class Income(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    income_head = models.ForeignKey(IncomeHead, on_delete=models.CASCADE, blank=False, null=True)
    payment_method = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    date = models.DateField(null=True)
    note = models.TextField(max_length=300)


class ExpenditureHead(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    expenditure_head = models.CharField(max_length=100)
    note = models.TextField(max_length=300)


class Expenditure(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    expenditure_head = models.ForeignKey(ExpenditureHead, on_delete=models.CASCADE, blank=False, null=True)
    expenditure_method = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    date = models.DateField(null=True)
    note = models.TextField(max_length=300)


class Gallery(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    gallery_title = models.CharField(max_length=100)
    note = models.TextField(max_length=300)
    IS = (('Yes', 'Yes'),
          ('No', 'No'))
    Is_View_on_Web = models.CharField(max_length=100, blank=False, choices=IS)


class Image(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    gallery_title = models.ForeignKey(Gallery, on_delete=models.CASCADE, blank=False, null=True)
    gallery_image = models.FileField(upload_to='images/', null=True, blank=False)
    image_caption = models.CharField(max_length=100)


class Page(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    IS = (('Header', 'Header'),
          ('Footer', 'Footer'))
    page_location = models.CharField(max_length=100, blank=False, choices=IS)
    page_title = models.CharField(max_length=100)
    page_description = models.TextField(max_length=300)
    page_image = models.FileField(upload_to='images/', null=True, blank=False)


class Slider(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, null=True)
    slider_image = models.FileField(upload_to='sliders/', null=True, blank=False)
    image_title = models.CharField(max_length=100)
