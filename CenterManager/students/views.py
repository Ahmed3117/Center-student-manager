from rest_framework import viewsets
from django.db.models import Q
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status

from classapp.middleware import api_key_required
from classapp.models import Attendance_Details, Course, MainBill, Notification, SalesBill
from classapp.serializers import Attendance_DetailsSerializer, CourseSerializer, MainBillSerializer, NotificationSerializer, SalesBillSerializer

class StudentCoursesViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer

    def get_queryset(self):
        student_code = self.kwargs['student_code']
        return Course.objects.filter(student__code=student_code)

    @api_key_required
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response

class StudentMainBillsViewSet(viewsets.ModelViewSet):
    serializer_class = MainBillSerializer


    def get_queryset(self):
        student_code = self.kwargs['student_code']
        return MainBill.objects.filter(course_id__student__code=student_code)

    @api_key_required
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response

class StudentSalesBillsViewSet(viewsets.ModelViewSet):
    serializer_class = SalesBillSerializer

    def get_queryset(self):
        student_code = self.kwargs['student_code']
        return SalesBill.objects.filter(bill_id__course_id__student__code=student_code)

    @api_key_required
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response

class StudentSalesBillsByDateViewSet(viewsets.ModelViewSet):
    serializer_class = SalesBillSerializer

    def get_queryset(self):
        student_code = self.kwargs['student_code']
        start_date_str = self.kwargs['start_date']
        end_date_str = self.kwargs['end_date']

        # Validate date format
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        except ValueError:
            return None  # Invalid date format

        return SalesBill.objects.filter(Q(date__gte=start_date) & Q(date__lte=end_date) & Q(bill_id__course_id__student__code=student_code))

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



##########################################################################


class SalesBillsByMainBillViewSet(viewsets.ModelViewSet):
    serializer_class = SalesBillSerializer

    def get_queryset(self):
        main_bill_id = self.kwargs['main_bill_id']
        return SalesBill.objects.filter(bill_id=main_bill_id)

    @api_key_required
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response

class StudentAttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = Attendance_DetailsSerializer


    def get_queryset(self):
        student_code = self.kwargs['student_code']
        return Attendance_Details.objects.filter(student_id__code=student_code).order_by('date_time')

    @api_key_required
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response

class StudentAttendanceByDateViewSet(viewsets.ModelViewSet):
    serializer_class = Attendance_DetailsSerializer

    def get_queryset(self):
        student_code = self.kwargs['student_code']
        start_date_str = self.kwargs['start_date']
        end_date_str = self.kwargs['end_date']

        # Validate date format
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        except ValueError:
            return None  # Invalid date format

        return Attendance_Details.objects.filter(Q(date_time__date__gte=start_date) & Q(date_time__date__lte=end_date) & Q(student_id__code=student_code)).order_by('date_time')

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

class StudentNotificationsViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        student_code = self.kwargs['student_code']
        return Notification.objects.filter(student__code=student_code)

    @api_key_required
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    # permission_classes = [IsAuthenticated]

    # @api_key_required
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)