from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, filters
from .models import Absence_Details, Attendance_Details, Class, Course, Course_Attendance, Division, Center, MainBill, Month, Notification, SalesBill, Student, Subject
from .serializers import Absence_DetailsSerializer, Attendance_DetailsSerializer, ClassSerializer, Course_AttendanceSerializer, CourseSerializer, DivisionSerializer, CenterSerializer, MainBillSerializer, MonthSerializer, NotificationSerializer, SalesBillSerializer, SubjectSerializer, StudentSerializer
from .middleware import api_key_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q
from datetime import datetime
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

###########################################################################################
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


class StudentAttendanceDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = Attendance_DetailsSerializer
    def get_queryset(self):
        student_id = self.kwargs['student_id']
        month = int(self.kwargs['month'])  
        year = int(self.kwargs['year'])  

        # Filter by student, month, and year
        start_date = datetime(year=year, month=month, day=1)
        end_date = datetime(year=year, month=month + 1, day=1)
        return Attendance_Details.objects.filter(
            student_id=student_id,
            date_time__gte=start_date,
            date_time__lt=end_date
        )

    @api_key_required
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data,
            'total': len(response.data)
        }
        return response

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


#----------------------------------------------------------------

# class AttendanceAbsenceCountForStudentInSpecificMonthAndCourseViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Attendance_Details.objects.all()

#     @action(detail=False, methods=['get'], url_path='course-attendance-details')
#     def course_attendance_details(self, request):
#         student_id = request.query_params.get('student_id')
#         year = request.query_params.get('year')
#         month = request.query_params.get('month')
#         course_attend_id = request.query_params.get('course_attend_id')

#         if not student_id or not year or not month or not course_attend_id:
#             return Response({'error': 'Missing student_id, year, month, or course_attend_id'}, status=400)

#         try:
#             year = int(year)
#             month = int(month)
#             course_attend_id = int(course_attend_id)
#         except ValueError:
#             return Response({'error': 'Year, month, and course_attend_id must be integers'}, status=400)

#         try:
#             student = Student.objects.get(id=student_id)
#         except Student.DoesNotExist:
#             return Response({'error': 'Student not found'}, status=404)

#         try:
#             course_attendance = Course_Attendance.objects.get(id=course_attend_id)
#         except Course_Attendance.DoesNotExist:
#             return Response({'error': 'Course attendance not found'}, status=404)

#         attendance_details = Attendance_Details.objects.filter(
#             student_id=student_id,
#             course_attend_id=course_attend_id,
#             course_attend_id__date__year=year,
#             course_attend_id__date__month=month
#         )

#         absence_details = Absence_Details.objects.filter(
#             student_id=student_id,
#             course_attend_id=course_attend_id,
#             course_attend_id__date__year=year,
#             course_attend_id__date__month=month
#         )

#         attendances = [
#             {
#                 'id': ad.id,
#                 'date_time': ad.date_time.isoformat(),
#                 'status': ad.status,
#                 'student_id': ad.student_id.id,
#                 'course_attend_id': ad.course_attend_id.id,
#                 'class_name': ad.course_attend_id.class_id.name,
#                 'student_name': ad.student_id.name,
#                 'attend': 1
#             }
#             for ad in attendance_details
#         ]

#         absences = [
#             {
#                 'id': ab.id,
#                 'date_time': ab.date_time.isoformat(),
#                 'status': None,  # or whatever status you want to represent absence
#                 'student_id': ab.student_id.id,
#                 'course_attend_id': ab.course_attend_id.id,
#                 'class_name': ab.course_attend_id.class_id.name,
#                 'student_name': ab.student_id.name,
#                 'attend': 0
#             }
#             for ab in absence_details
#         ]

#         data = attendances + absences

#         response_data = {
#             'data': data,
#             'attend_num': len(attendances),
#             'absence_num': len(absences)
#         }

#         return Response(response_data)

#     @action(detail=False, methods=['get'], url_path='all-course-attendance-details')
#     def all_course_attendance_details(self, request):
#         student_id = request.query_params.get('student_id')
#         year = request.query_params.get('year')
#         month = request.query_params.get('month')

#         if not student_id or not year or not month:
#             return Response({'error': 'Missing student_id, year, or month'}, status=400)

#         try:
#             year = int(year)
#             month = int(month)
#         except ValueError:
#             return Response({'error': 'Year and month must be integers'}, status=400)

#         try:
#             student = Student.objects.get(id=student_id)
#         except Student.DoesNotExist:
#             return Response({'error': 'Student not found'}, status=404)

#         attendance_details = Attendance_Details.objects.filter(
#             student_id=student_id,
#             course_attend_id__date__year=year,
#             course_attend_id__date__month=month
#         )

#         absence_details = Absence_Details.objects.filter(
#             student_id=student_id,
#             course_attend_id__date__year=year,
#             course_attend_id__date__month=month
#         )

#         attendances = [
#             {
#                 'id': ad.id,
#                 'date_time': ad.date_time.isoformat(),
#                 'status': ad.status,
#                 'student_id': ad.student_id.id,
#                 'course_attend_id': ad.course_attend_id.id,
#                 'class_name': ad.course_attend_id.class_id.name,
#                 'student_name': ad.student_id.name,
#                 'attend': 1
#             }
#             for ad in attendance_details
#         ]

#         absences = [
#             {
#                 'id': ab.id,
#                 'date_time': ab.date_time.isoformat(),
#                 'status': None,  # or whatever status you want to represent absence
#                 'student_id': ab.student_id.id,
#                 'course_attend_id': ab.course_attend_id.id,
#                 'class_name': ab.course_attend_id.class_id.name,
#                 'student_name': ab.student_id.name,
#                 'attend': 0
#             }
#             for ab in absence_details
#         ]

#         data = attendances + absences

#         response_data = {
#             'data': data,
#             'attend_num': len(attendances),
#             'absence_num': len(absences)
#         }

#         return Response(response_data)


class AttendanceAbsenceCountForStudentInSpecificMonthAndCourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Attendance_Details.objects.all()

    @action(detail=False, methods=['get'], url_path='attendance-details')
    def attendance_details(self, request):
        student_id = request.query_params.get('student_id')
        year = request.query_params.get('year')
        month = request.query_params.get('month')
        course_attend_id = request.query_params.get('course_attend_id')

        filters = {}
        
        if student_id:
            filters['student_id'] = student_id
        if year:
            try:
                filters['course_attend_id__date__year'] = int(year)
            except ValueError:
                return Response({'error': 'Year must be an integer'}, status=400)
        if month:
            try:
                filters['course_attend_id__date__month'] = int(month)
            except ValueError:
                return Response({'error': 'Month must be an integer'}, status=400)
        if course_attend_id:
            try:
                filters['course_attend_id'] = int(course_attend_id)
            except ValueError:
                return Response({'error': 'Course_attend_id must be an integer'}, status=400)
        
        try:
            if student_id:
                student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=404)

        attendance_details = Attendance_Details.objects.filter(**filters)
        absence_details = Absence_Details.objects.filter(**filters)

        attendances = [
            {
                'id': ad.id,
                'date_time': ad.date_time.isoformat(),
                'status': ad.status,
                'student_id': ad.student_id.id,
                'course_attend_id': ad.course_attend_id.id,
                'class_name': ad.course_attend_id.class_id.name,
                'student_name': ad.student_id.name,
                'attend': 1
            }
            for ad in attendance_details
        ]

        absences = [
            {
                'id': ab.id,
                'date_time': ab.date_time.isoformat(),
                'status': None,  # or whatever status you want to represent absence
                'student_id': ab.student_id.id,
                'course_attend_id': ab.course_attend_id.id,
                'class_name': ab.course_attend_id.class_id.name,
                'student_name': ab.student_id.name,
                'attend': 0
            }
            for ab in absence_details
        ]

        data = attendances + absences

        response_data = {
            'data': data,
            'attend_num': len(attendances),
            'absence_num': len(absences)
        }

        return Response(response_data)



#----------------------------------------------------------------


###########################################################################################

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

# class SalesBillViewSet(viewsets.ModelViewSet):
#     queryset = SalesBill.objects.all().order_by('date')
#     serializer_class = SalesBillSerializer
    
#     @api_key_required
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
#     def list(self, request, *args, **kwargs):
#         response = super().list(request, *args, **kwargs)
#         response.data = {
#             'data': response.data,
#             'total': len(response.data)
#         }
#         return response
    
#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)


# class SalesBillViewSet(viewsets.ModelViewSet):
#     queryset = SalesBill.objects.all().order_by('date')
#     serializer_class = SalesBillSerializer
    
#     @api_key_required
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         data = serializer.data
        
#         total_remainder = 0

#         for item in data:
#             main_bill = MainBill.objects.get(id=item['bill_id'])
#             class_name = main_bill.course_id.class_id.name
#             subject_name = main_bill.course_id.class_id.subject_id.name
#             total_remain = main_bill.total_remain
#             item['class_name'] = class_name
#             item['subject_name'] = subject_name
#             item['remainder'] = str(total_remain)
#             total_remainder += float(total_remain)

#         response_data = {
#             'data': data,
#             'total_remainder': str(total_remainder),
#             'total': len(data)
#         }

#         return Response(response_data)

#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)



class SalesBillViewSet(viewsets.ModelViewSet):
    queryset = SalesBill.objects.all().order_by('date')
    serializer_class = SalesBillSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['bill_id__course_id__student__id', 'bill_id__course_id__student__code']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        student_id = self.request.query_params.get('student_id', None)
        code = self.request.query_params.get('code', None)
        
        if student_id:
            queryset = queryset.filter(bill_id__course_id__student__id=student_id)
        if code:
            queryset = queryset.filter(bill_id__course_id__student__code=code)
        
        return queryset
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        total_remainder = sum(float(item['remainder']) for item in response.data)
        response.data = {
            'data': response.data,
            'total_remainder': f"{total_remainder:.2f}",
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
