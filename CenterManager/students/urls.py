from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'courses/(?P<student_code>\w+)', views.StudentCoursesViewSet, basename='student_courses')
router.register(r'main_bills/(?P<student_code>\w+)', views.StudentMainBillsViewSet, basename='student_main_bills')
router.register(r'sales_bills/(?P<student_code>\w+)', views.StudentSalesBillsViewSet, basename='student_sales_bills')
router.register(r'sales_bills_by_date/(?P<student_code>\w+)/(?P<start_date>\d{4}-\d{2}-\d{2})/(?P<end_date>\d{4}-\d{2}-\d{2})', views.StudentSalesBillsByDateViewSet, basename='student_sales_bills_by_date')
router.register(r's_bills/(?P<main_bill_id>\d+)', views.SalesBillsByMainBillViewSet, basename='sales_bills_by_main_bill')
router.register(r'attendance/(?P<student_code>\w+)', views.StudentAttendanceViewSet, basename='student_attendance')
router.register(r'attendance_by_date/(?P<student_code>\w+)/(?P<start_date>\d{4}-\d{2}-\d{2})/(?P<end_date>\d{4}-\d{2}-\d{2})', views.StudentAttendanceByDateViewSet, basename='student_attendance_by_date')
router.register(r'notifications/(?P<student_code>\w+)', views.StudentNotificationsViewSet, basename='student_notifications')

urlpatterns = [
    path('', include(router.urls)),
]
