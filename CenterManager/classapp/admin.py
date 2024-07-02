import datetime
from dateutil.relativedelta import relativedelta
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import SimpleListFilter
from rangefilter.filters import DateRangeFilter
from .models import (
    Division, Center, Subject, Class, Student, Month, 
    Course_Attendance, Attendance_Details, Absence_Details, 
    Course, MainBill, SalesBill, Notification
)


class CenterNameFilter(SimpleListFilter):
    title = _('Center')
    parameter_name = 'center'

    def lookups(self, request, model_admin):
        return (
            (center.id, center.name) for center in Center.objects.all()
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(center_id=self.value())
        return queryset

class DivisionNameFilter(SimpleListFilter):
    title = _('Division')
    parameter_name = 'division'

    def lookups(self, request, model_admin):
        return (
            (division.id, division.name) for division in Division.objects.all()
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(division_id=self.value())
        return queryset

class SubjectNameFilter(SimpleListFilter):
    title = _('Subject')
    parameter_name = 'subject'

    def lookups(self, request, model_admin):
        return (
            (subject.id, subject.name) for subject in Subject.objects.all()
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(subject_id=self.value())
        return queryset

class ClassNameFilter(SimpleListFilter):
    title = _('Class')
    parameter_name = 'class'

    def lookups(self, request, model_admin):
        return (
            (class_var.id, class_var.name) for class_var in Class.objects.all()
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(class_id=self.value())
        return queryset
class MonthNameFilter(SimpleListFilter):
    title = _('Month')
    parameter_name = 'month'

    def lookups(self, request, model_admin):
        return (
            (month.id, month.name) for month in Month.objects.all()
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(month_id=self.value())
        return queryset

ADMIN_ORDERING = (
    ('classapp', ('Division', 'Center', 'Subject', 'Class', 'Student', 'Month', 'Course_Attendance', 'Attendance_Details', 'Absence_Details', 'Course', 'MainBill', 'SalesBill', 'Notification')),
    ('accounts', ('CustomUser',)),
    ('auth', ('Group',)),
    ('admin_interface', ('Theme',)),
)

def get_app_list(self, request, app_label=None):
    app_dict = self._build_app_dict(request, app_label)
    if not app_dict:
        return
    NEW_ADMIN_ORDERING = []
    if app_label:
        for ao in ADMIN_ORDERING:
            if ao[0] == app_label:
                NEW_ADMIN_ORDERING.append(ao)
                break
    if not app_label:
        for app_key in list(app_dict.keys()):
            if not any(app_key in ao_app for ao_app in ADMIN_ORDERING):
                app_dict.pop(app_key)
    app_list = sorted(
        app_dict.values(), key=lambda x: [ao[0] for ao in ADMIN_ORDERING].index(x['app_label'])
    )
    for app, ao in zip(app_list, NEW_ADMIN_ORDERING or ADMIN_ORDERING):
        if app['app_label'] == ao[0]:
            for model in list(app['models']):
                if not model['object_name'] in ao[1]:
                    app['models'].remove(model)
        app['models'].sort(key=lambda x: ao[1].index(x['object_name']))
    return app_list

admin.AdminSite.get_app_list = get_app_list

class DivisionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    search_fields = ('name', 'phone')

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'ActiveStudentnumbers', 'monthCount', 'center_id', 'division_id', 'subject_id')
    list_filter = (
        CenterNameFilter,
        DivisionNameFilter,
        SubjectNameFilter,
    )
    search_fields = ('name',)
    autocomplete_fields = ('center_id', 'division_id', 'subject_id')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_num', 'parent_phone', 'registration_date', 'code', 'active', 'block', 'division')
    list_filter = ('active', 'block', DivisionNameFilter)
    search_fields = ('name', 'phone_num', 'parent_phone', 'code')
    readonly_fields = ('registration_date',)
    autocomplete_fields = ('division',)

class MonthAdmin(admin.ModelAdmin):
    list_display = ('name', 'month_num', 'class_id')
    list_filter = ('class_id',)
    search_fields = ('name',)
    autocomplete_fields = ('class_id',)

class CourseAttendanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'total_students', 'attend', 'absence', 'count', 'user_id', 'status', 'month_id', 'class_id')
    list_filter = ('status', MonthNameFilter, ClassNameFilter,('date', DateRangeFilter))
    search_fields = ('name',)
    readonly_fields = ('date',)
    autocomplete_fields = ('month_id', 'class_id')

class AttendanceDetailsAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'status', 'out_attend', 'notes', 'home_work', 'video_view', 'teacher_paid_status', 'student_id', 'course_attend_id')
    list_filter = ('status', 'teacher_paid_status', 'student_id', 'course_attend_id')
    search_fields = ('notes','student_id__name', 'course_attend_id__name')
    autocomplete_fields = ('student_id', 'course_attend_id')

class AbsenceDetailsAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'permission', 'notes', 'student_id', 'course_attend_id')
    list_filter = ('permission', 'student_id', 'course_attend_id')
    search_fields = ('notes','student_id__name', 'course_attend_id__name')
    readonly_fields = ('date_time',)
    autocomplete_fields = ('student_id', 'course_attend_id')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('register_date', 'paid_status', 'current_status', 'teacher_fee', 'center_fee', 'total_fee', 'no_paid', 'student', 'class_id')
    list_filter = ('paid_status', 'current_status', ClassNameFilter)
    search_fields = ('notes','student__name', 'class_id__name')
    readonly_fields = ('register_date',)
    autocomplete_fields = ('student', 'class_id')

class MainBillAdmin(admin.ModelAdmin):
    list_display = ('date', 'paid_type', 'paid_status', 'total_before', 'center_discount', 'teacher_discount', 'discount', 'total_after', 'center_fee', 'teacher_fee', 'total_paid', 'center_paid', 'teacher_paid', 'total_remain', 'center_remain', 'teacher_remain', 'course_id', 'month_id')
    list_filter = ('paid_status', MonthNameFilter, 'paid_type')
    search_fields = ('notes', 'paid_type')
    readonly_fields = ('date',)
    autocomplete_fields = ('course_id', 'month_id')

class SalesBillAdmin(admin.ModelAdmin):
    list_display = ('date', 'paid_type', 'paid_status', 'total_before', 'center_discount', 'teacher_discount', 'discount', 'total_after', 'center_fee', 'teacher_fee', 'total_paid', 'center_paid', 'teacher_paid', 'total_remain', 'center_remain', 'teacher_remain', 'bill_id')
    list_filter = ('paid_status', 'bill_id')
    search_fields = ('notes', 'paid_type')
    readonly_fields = ('date',)
    autocomplete_fields = ('bill_id',)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('student', 'notification', 'date', 'status')
    list_filter = ('status', 'student')
    search_fields = ('notification',)
    readonly_fields = ('date',)
    autocomplete_fields = ('student',)




admin.site.register(Division, DivisionAdmin)
admin.site.register(Center, CenterAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Month, MonthAdmin)
admin.site.register(Course_Attendance, CourseAttendanceAdmin)
admin.site.register(Attendance_Details, AttendanceDetailsAdmin)
admin.site.register(Absence_Details, AbsenceDetailsAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(MainBill, MainBillAdmin)
admin.site.register(SalesBill, SalesBillAdmin)
admin.site.register(Notification, NotificationAdmin)
