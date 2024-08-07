from rest_framework import serializers
from .models import Absence_Details, Attendance_Details, Class, Course, Course_Attendance, Division, Center, MainBill, Month, Notification, SalesBill, Subject, Student

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'

class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Month
        fields = '__all__'
        
class Course_AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_Attendance
        fields = '__all__'
        
class Attendance_DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance_Details
        fields = '__all__'

class Absence_DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absence_Details
        fields = '__all__'
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class MainBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainBill
        fields = '__all__'

class SalesBillSerializer(serializers.ModelSerializer):
    class_name = serializers.CharField(source='bill_id.course_id.class_id.name', read_only=True)
    subject_name = serializers.CharField(source='bill_id.course_id.class_id.subject_id.name', read_only=True)
    remainder = serializers.DecimalField(source='bill_id.total_remain', max_digits=18, decimal_places=2, read_only=True)

    class Meta:
        model = SalesBill
        fields = ['id', 'date', 'notes', 'paid_type', 'paid_status', 'total_before', 'center_discount', 'teacher_discount',
                'discount', 'total_after', 'center_fee', 'teacher_fee', 'total_paid', 'center_paid', 'teacher_paid',
                'total_remain', 'center_remain', 'teacher_remain', 'bill_id', 'class_name', 'subject_name', 'remainder']
        
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'




###########################################################
