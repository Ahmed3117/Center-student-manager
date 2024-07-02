from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.db.models import Subquery
from classapp.middleware import api_key_required
from classapp.models import Absence_Details, Attendance_Details, Class, Course_Attendance, SalesBill, Student
from classapp.serializers import Absence_DetailsSerializer, Attendance_DetailsSerializer, Course_AttendanceSerializer, SalesBillSerializer, StudentSerializer

class AdminStudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('name')
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    @api_key_required
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response
    
class StudentsByDivisionViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        division_id = self.kwargs['division_id']
        return Student.objects.filter(division__id=division_id).order_by('name')

    @api_key_required
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response

class StudentsByClassViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        class_id = self.kwargs['class_id']
        return Student.objects.filter(division__class__id=class_id).order_by('name')

    @api_key_required
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response

class StudentsByCenterViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        center_id = self.kwargs['center_id']
        classes_in_center = Class.objects.filter(center_id=center_id)
        return Student.objects.filter(division__in=Subquery(classes_in_center.values('division_id'))).order_by('name')

    @api_key_required
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response
    
#----------------------------------------------------------------

from django.db.models import Q
from datetime import datetime

class CourseAttendanceViewSet(viewsets.ModelViewSet):
    queryset = Course_Attendance.objects.all().order_by('date')
    serializer_class = Course_AttendanceSerializer
    permission_classes = [IsAuthenticated]

    @api_key_required
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response

from datetime import datetime
from rest_framework import status
from rest_framework.response import Response

class CourseAttendanceByDateViewSet(viewsets.ModelViewSet):
    serializer_class = Course_AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        start_date_str = self.kwargs['start_date']
        end_date_str = self.kwargs['end_date']

        # Validate date format
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        except ValueError:
            return None  

        return Course_Attendance.objects.filter(Q(date__gte=start_date) & Q(date__lte=end_date)).order_by('date')

    @api_key_required
    def list(self, request, *args, **kwargs):
        if self.get_queryset() is None:
            return Response({'error': 'Not valid date format'}, status=status.HTTP_400_BAD_REQUEST)

        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response

class CourseAttendanceByMonthViewSet(viewsets.ModelViewSet):
    serializer_class = Course_AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        year_str = self.kwargs['year']
        month_str = self.kwargs['month']

        # Validate year and month format
        try:
            year = int(year_str)
            month = int(month_str)
            if month < 1 or month > 12:
                raise ValueError("Month must be between 1 and 12")
        except ValueError:
            return None  

        start_date = datetime(year, month, 1).date()
        if month == 12:
            end_date = datetime(year + 1, 1, 1).date()
        else:
            end_date = datetime(year, month + 1, 1).date()

        return Course_Attendance.objects.filter(Q(date__gte=start_date) & Q(date__lt=end_date)).order_by('date')

    @api_key_required
    def list(self, request, *args, **kwargs):
        if self.get_queryset() is None:
            return Response({'error': 'Invalid year or month format'}, status=status.HTTP_400_BAD_REQUEST)

        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response

class AttendanceDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = Attendance_DetailsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        course_attend_id = self.kwargs['course_attend_id']
        return Attendance_Details.objects.filter(course_attend_id=course_attend_id)

    @api_key_required
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response

class AbsenceDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = Absence_DetailsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        course_attend_id = self.kwargs['course_attend_id']
        return Absence_Details.objects.filter(course_attend_id=course_attend_id)

    @api_key_required
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response

#----------------------------------------------------------------

class SalesBillViewSet(viewsets.ModelViewSet):
    queryset = SalesBill.objects.all().order_by('date')
    serializer_class = SalesBillSerializer
    permission_classes = [IsAuthenticated]

    @api_key_required
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response

class SalesBillByDateViewSet(viewsets.ModelViewSet):
    serializer_class = SalesBillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        start_date_str = self.kwargs['start_date']
        end_date_str = self.kwargs['end_date']

        # Validate date format
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        except ValueError:
            return None  # Invalid date format

        return SalesBill.objects.filter(Q(date__gte=start_date) & Q(date__lte=end_date)).order_by('date')

    @api_key_required
    def list(self, request, *args, **kwargs):
        if self.get_queryset() is None:
            return Response({'error': 'Not valid date format'}, status=status.HTTP_400_BAD_REQUEST)

        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response

