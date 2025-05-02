from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.db.models import Avg, Count
from .models import UserProfile, Exercise, Workout, WorkoutExercise

# Custom admin for Workout with a report view
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "date", "duration")

    change_list_template = "admin/workouts/change_list_with_report_link.html"

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        custom_urls = [
            path("report/", self.admin_site.admin_view(self.report_view), name="workout_report"),
        ]
        return custom_urls + urls

    def report_view(self, request):

        exercises = Exercise.objects.all()
        selected_exercise_id = request.GET.get("exercise")
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")

        workouts = Workout.objects.all()

        if start_date:
            workouts = workouts.filter(date__gte=start_date)
        if end_date:
            workouts = workouts.filter(date__lte=end_date)
        if selected_exercise_id:
            workouts = workouts.filter(workoutexercise__exercise__id=selected_exercise_id)

        stats = workouts.aggregate(
            avg_duration=Avg("duration"),
            total_workouts=Count("id"),
        )

        context = dict(
            self.admin_site.each_context(request),
            exercises=exercises,
            stats=stats,
            selected_exercise_id=selected_exercise_id,
            start_date=start_date,
            end_date=end_date,
        )
        return render(request, "admin/workouts/report.html", context)

# Register your models here.
admin.site.register(UserProfile)
#admin.site.register(Exercise)
@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("name", "muscle_group")
admin.site.register(Workout, WorkoutAdmin)
#admin.site.register(WorkoutExercise)
@admin.register(WorkoutExercise)
class WorkoutExerciseAdmin(admin.ModelAdmin):
    list_display = ("workout", "exercise", "sets", "reps", "weight")
    list_filter = ("workout",)