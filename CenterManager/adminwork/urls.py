from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
app_name='adminwork'

router = DefaultRouter()
router.register(r'students', views.AdminStudentViewSet)
router.register(r'students_by_division/(?P<division_id>\d+)', views.StudentsByDivisionViewSet, basename='students_by_division')
router.register(r'students_by_class/(?P<class_id>\d+)', views.StudentsByClassViewSet, basename='students_by_class')
router.register(r'students_by_center/(?P<center_id>\d+)', views.StudentsByCenterViewSet, basename='students_by_center')
router.register(r'attendances', views.CourseAttendanceViewSet, basename='attendances')
router.register(r'attendances_by_date/(?P<start_date>\d{4}-\d{2}-\d{2})/(?P<end_date>\d{4}-\d{2}-\d{2})', views.CourseAttendanceByDateViewSet, basename='attendances_by_date')
router.register(r'attendance_details/(?P<course_attend_id>\d+)', views.AttendanceDetailsViewSet, basename='attendance_details')
router.register(r'absence_details/(?P<course_attend_id>\d+)', views.AbsenceDetailsViewSet, basename='absence_details')
router.register(r'sales_bills', views.SalesBillViewSet, basename='sales_bills')
router.register(r'sales_bills_by_date/(?P<start_date>\d{4}-\d{2}-\d{2})/(?P<end_date>\d{4}-\d{2}-\d{2})', views.SalesBillByDateViewSet, basename='sales_bills_by_date')

urlpatterns = [
    path('', include(router.urls)),
]

