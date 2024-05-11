from django.urls import path

from dormitory.views import NewsListView, PointsHistoryListView, student_dossier_view, PointsHistorySortsListView

urlpatterns = [
    path('', NewsListView.as_view(), name='main'),
    path('students/', PointsHistoryListView.as_view(), name='student_list'),
    path('student/<int:student_id>/points_history/', PointsHistoryListView.as_view(), name='points_history_list'),
    path('student/<int:student_id>/', student_dossier_view, name='student-dossier'),
    path('statistics/', PointsHistorySortsListView.as_view(), name='student-statistics'),

]
