from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Absence_Details, Attendance_Details, Class, Course, Course_Attendance, Division, Center, MainBill, Month, Notification, SalesBill, Student, Subject
from .serializers import Absence_DetailsSerializer, Attendance_DetailsSerializer, ClassSerializer, Course_AttendanceSerializer, CourseSerializer, DivisionSerializer, CenterSerializer, MainBillSerializer, MonthSerializer, NotificationSerializer, SalesBillSerializer, SubjectSerializer, StudentSerializer
from .middleware import api_key_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all().order_by('name')
    serializer_class = DivisionSerializer
    @api_key_required
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response


    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class CenterViewSet(viewsets.ModelViewSet):
    queryset = Center.objects.all().order_by('name')
    serializer_class = CenterSerializer
    @api_key_required
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response


    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all().order_by('name')
    serializer_class = SubjectSerializer
    @api_key_required
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response


    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all().order_by('name')
    serializer_class = ClassSerializer
    @api_key_required
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response


    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('name')
    serializer_class = StudentSerializer

    @api_key_required
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Check if username and password are provided
        if not username or not password:
            return Response({"detail": "bad input parameter."}, status=400)

        # Check if username equals password
        if username != password:
            return Response({"detail": "Authentication credentials were not provided."}, status=401)

        try:
            student = Student.objects.get(code=username)
        except Student.DoesNotExist:
            return Response({"detail": "Student not found"}, status=404)

        serializer = StudentSerializer(student)
        return Response(serializer.data)

class MonthViewSet(viewsets.ModelViewSet):
    queryset = Month.objects.all().order_by('name')
    serializer_class = MonthSerializer
    
    @api_key_required
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class Course_AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Course_Attendance.objects.all().order_by('name')
    serializer_class = Course_AttendanceSerializer
    
    @api_key_required
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class Attendance_DetailsViewSet(viewsets.ModelViewSet):
    queryset = Attendance_Details.objects.all().order_by('date_time')
    serializer_class = Attendance_DetailsSerializer
    
    @api_key_required
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class Absence_DetailsViewSet(viewsets.ModelViewSet):
    queryset = Absence_Details.objects.all().order_by('date_time')
    serializer_class = Absence_DetailsSerializer
    
    @api_key_required
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('register_date')
    serializer_class = CourseSerializer
    
    @api_key_required
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class MainBillViewSet(viewsets.ModelViewSet):
    queryset = MainBill.objects.all().order_by('date')
    serializer_class = MainBillSerializer
    
    @api_key_required
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class SalesBillViewSet(viewsets.ModelViewSet):
    queryset = SalesBill.objects.all().order_by('date')
    serializer_class = SalesBillSerializer
    
    @api_key_required
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

#---------------------------------------------
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    # permission_classes = [IsAuthenticated]

    @api_key_required
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
