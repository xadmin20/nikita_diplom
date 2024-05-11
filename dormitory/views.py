from pprint import pprint

from django.db.models import ExpressionWrapper, IntegerField, F, Sum, Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from dormitory.models import News, PointsHistory, Student, Dormitory


class NewsListView(ListView):
    """Выдача списка новостей."""
    model = News
    template_name = 'news.html'

    def get_queryset(self):
        return News.objects.order_by('-date')


class PointsHistoryListView(ListView):
    """Выдача истории баллов для конкретного студента."""
    model = PointsHistory
    template_name = 'students.html'  # Убедитесь, что это правильный шаблон

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        students = Student.objects.all()
        for student in students:
            student.history = PointsHistory.objects.filter(student=student)
        context['students'] = students
        pprint(context)
        return context


def student_dossier_view(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    points_history = PointsHistory.objects.filter(student=student).select_related('event')

    # Аннотируем объект студента, добавляя сумму баллов по типам событий
    student = Student.objects.filter(id=student_id).annotate(
        total_admin_points=Sum('pointshistory__event__points', filter=Q(pointshistory__event__event_type='admin')),
        total_sso_points=Sum('pointshistory__event__points', filter=Q(pointshistory__event__event_type='sso'))
    ).first()

    total_students = Student.objects.count()
    middle_index = total_students // 2
    red_threshold = total_students - 10

    # Определение позиции студента
    ranking = Student.objects.annotate(
        total_points=Sum('pointshistory__event__points')
    ).order_by('-total_points').values_list('id', flat=True)
    position = list(ranking).index(student.id) + 1  # Indexing from 1

    context = {
        'student': student,
        'points_history': points_history,
        'ranking_position': position,
        'total_students': total_students,
        'middle_index': middle_index,
        'red_threshold': red_threshold,
    }
    return render(request, 'student_dossier.html', context)


class PointsHistorySortsListView(ListView):
    model = Student
    template_name = 'statistics.html'
    context_object_name = 'students'

    def get_queryset(self):
        queryset = Student.objects.annotate(
            total_admin_points=Sum('pointshistory__event__points', filter=Q(pointshistory__event__event_type='admin')),
            total_sso_points=Sum('pointshistory__event__points', filter=Q(pointshistory__event__event_type='sso')),
            total_points=F('total_admin_points') + F('total_sso_points')
        ).order_by('-total_points')

        dormitory = self.request.GET.get('dormitory')
        group = self.request.GET.get('group')
        room = self.request.GET.get('room')

        if dormitory:
            queryset = queryset.filter(dormitory__id=dormitory)
        if group:
            queryset = queryset.filter(group=group)
        if room:
            queryset = queryset.filter(room=room)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dormitories'] = Dormitory.objects.all()  # Добавляем список общежитий
        return context




