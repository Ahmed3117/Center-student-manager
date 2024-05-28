from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
app_name='classapp'

router = DefaultRouter()
router.register(r'classes', views.ClassViewSet)
router.register(r'divisions', views.DivisionViewSet)
router.register(r'centers', views.CenterViewSet)
router.register(r'subjects', views.SubjectViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'months', views.MonthViewSet)
router.register(r'course_attendances', views.Course_AttendanceViewSet)
router.register(r'attendance_details', views.Attendance_DetailsViewSet)
router.register(r'absence_details', views.Absence_DetailsViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'main_bills', views.MainBillViewSet)
router.register(r'sales_bills', views.SalesBillViewSet)
router.register(r'notifications', views.NotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('students/login/', views.LoginStudent.as_view(), name='loginstudent'),
]
