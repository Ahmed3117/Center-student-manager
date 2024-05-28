from django.db import models

#--------------------------------------------------------------
class Division(models.Model):
    name = models.CharField(max_length=255)

class Center(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

class Subject(models.Model):
    name = models.CharField(max_length=255)

class Class(models.Model):
    name = models.CharField(max_length=255)
    ActiveStudentnumbers = models.IntegerField()
    monthCount = models.IntegerField()
    session_teacher_fee = models.DecimalField(max_digits=18, decimal_places=2)
    session_center_fee = models.DecimalField(max_digits=18, decimal_places=2)
    session_total_fee  =  models.DecimalField(max_digits=18, decimal_places=2)
    month_teacher_fee = models.DecimalField(max_digits=18, decimal_places=2)
    month_center_fee =  models.DecimalField(max_digits=18, decimal_places=2)
    month_total_fee  =  models.DecimalField(max_digits=18, decimal_places=2)
    center_id  =  models.ForeignKey(Center, on_delete=models.CASCADE) 
    division_id = models.ForeignKey(Division, on_delete=models.CASCADE) 
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE) 

class Student(models.Model):
    name = models.CharField(max_length=255)
    phone_num = models.CharField(max_length=20)
    parent_phone = models.CharField(max_length=20)
    registration_date = models.DateField(auto_now_add=True)
    code = models.CharField(max_length=50)
    notes = models.TextField()
    active = models.BooleanField(default=True)
    block = models.BooleanField(default=False)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
#-----------------------------------------------------------------
class Month(models.Model):
    name = models.CharField(max_length=255)
    month_num = models.IntegerField()
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)

class Course_Attendance(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    total_students = models.IntegerField()
    attend = models.IntegerField()
    absence = models.IntegerField()
    count = models.IntegerField()
    user_id = models.IntegerField()
    status = models.IntegerField()
    month_id = models.ForeignKey(Month, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)

class Attendance_Details(models.Model):
    date_time = models.DateTimeField()
    status = models.IntegerField()
    out_attend = models.IntegerField()
    notes = models.CharField(max_length=255)
    home_work = models.IntegerField()
    video_view = models.IntegerField()
    teacher_paid_status = models.IntegerField()
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)  
    course_attend_id = models.ForeignKey(Course_Attendance, on_delete=models.CASCADE) 
    
class Absence_Details(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    permission = models.IntegerField()
    notes = models.CharField(max_length=255)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)  
    course_attend_id = models.ForeignKey(Course_Attendance, on_delete=models.CASCADE) 

#----------------------------------------------------------------
class Course(models.Model):
    notes = models.TextField()
    register_date = models.DateField(auto_now_add=True)
    paid_status = models.IntegerField()
    current_status = models.IntegerField()
    teacher_fee = models.DecimalField(max_digits=18, decimal_places=2)
    center_fee = models.DecimalField(max_digits=18, decimal_places=2)
    total_fee = models.DecimalField(max_digits=18, decimal_places=2)
    no_paid = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    
class MainBill(models.Model):
    date = models.DateField(auto_now_add=True)
    notes = models.TextField()
    paid_type = models.CharField(max_length=50)
    paid_status = models.IntegerField()
    total_before = models.DecimalField(max_digits=18, decimal_places=2)
    center_discount = models.DecimalField(max_digits=18, decimal_places=2)
    teacher_discount = models.DecimalField(max_digits=18, decimal_places=2)
    discount = models.DecimalField(max_digits=18, decimal_places=2)
    total_after = models.DecimalField(max_digits=18, decimal_places=2)
    center_fee = models.DecimalField(max_digits=18, decimal_places=2)
    teacher_fee = models.DecimalField(max_digits=18, decimal_places=2)
    total_paid = models.DecimalField(max_digits=18, decimal_places=2)
    center_paid = models.DecimalField(max_digits=18, decimal_places=2)
    teacher_paid = models.DecimalField(max_digits=18, decimal_places=2)
    total_remain = models.DecimalField(max_digits=18, decimal_places=2)
    center_remain = models.DecimalField(max_digits=18, decimal_places=2)
    teacher_remain = models.DecimalField(max_digits=18, decimal_places=2)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    month_id = models.ForeignKey(Month, on_delete=models.CASCADE)

class SalesBill(models.Model):
    date = models.DateField(auto_now_add=True)
    notes = models.TextField()
    paid_type = models.CharField(max_length=50)
    paid_status = models.IntegerField()
    total_before = models.DecimalField(max_digits=18, decimal_places=2)
    center_discount = models.DecimalField(max_digits=18, decimal_places=2)
    teacher_discount = models.DecimalField(max_digits=18, decimal_places=2)
    discount = models.DecimalField(max_digits=18, decimal_places=2)
    total_after = models.DecimalField(max_digits=18, decimal_places=2)
    center_fee = models.DecimalField(max_digits=18, decimal_places=2)
    teacher_fee = models.DecimalField(max_digits=18, decimal_places=2)
    total_paid = models.DecimalField(max_digits=18, decimal_places=2)
    center_paid = models.DecimalField(max_digits=18, decimal_places=2)
    teacher_paid = models.DecimalField(max_digits=18, decimal_places=2)
    total_remain = models.DecimalField(max_digits=18, decimal_places=2)
    center_remain = models.DecimalField(max_digits=18, decimal_places=2)
    teacher_remain = models.DecimalField(max_digits=18, decimal_places=2)
    bill_id = models.ForeignKey(MainBill, on_delete=models.CASCADE)
    
#----------------------------------------------------------------
class Notification(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    notification = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField()

    class Meta:
        db_table = 'Notification'
