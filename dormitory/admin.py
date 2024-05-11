from django.contrib import admin

from dormitory.models import Dormitory, Student, Event, PointsHistory, News


@admin.register(Dormitory)
class DormitoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    search_fields = ('name', 'address', 'phone')
    list_filter = ('name', 'phone')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'dormitory', 'institute', 'group', 'room', 'admin_points', 'sso_points')
    search_fields = ('full_name', 'dormitory', 'institute', 'group', 'room', 'admin_points', 'sso_points')
    list_filter = ('full_name', 'dormitory', 'institute', 'group', 'room', 'admin_points', 'sso_points')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'points', 'event_type', )
    search_fields = ('name', 'points', 'event_type', )
    list_filter = ('name', 'points', 'event_type', )


@admin.register(PointsHistory)
class PointsHistoryAdmin(admin.ModelAdmin):
    list_display = ('student', 'event', 'date', 'event_type', 'event_points', 'total_points')
    search_fields = ('student', 'event', 'date')
    list_filter = ('student', 'event', 'date')

    def event_type(self, obj):
        return obj.event.event_type
    event_type.short_description = 'Тип события'

    def event_points(self, obj):
        return obj.event.points
    event_points.short_description = 'Баллы'

    def total_points(self, obj):
        return obj.student.total_points()
    total_points.short_description = 'Общее количество баллов'


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'dormitory', 'images')
    search_fields = ('title', 'date', 'dormitory', 'images')
    list_filter = ('title', 'date', 'dormitory', 'images')


