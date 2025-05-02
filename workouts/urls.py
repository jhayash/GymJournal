from django.urls import path
from . import views

urlpatterns = [
    path("", views.workout_list, name="workout_list"),
    path("workout/<int:workout_id>/", views.workout_detail, name="workout_detail"),
    path("workout/new/", views.create_workout, name="create_workout"),
    path("workout/delete/<int:workout_id>/", views.delete_workout, name="delete_workout"),
    path("report/", views.report_view, name="report_view"),
]