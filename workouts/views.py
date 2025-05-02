from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Workout, Exercise, WorkoutExercise
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from .forms import WorkoutForm
from django.db import transaction

# Create your views here.
@login_required
def workout_list(request):
    workouts = Workout.objects.filter(user=request.user)
    return render(request, "workouts/workout_list.html", {"workouts": workouts})

@login_required
def workout_detail(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id, user=request.user)
    return render(request, "workouts/workout_detail.html", {"workout": workout})

@login_required
@transaction.atomic
def create_workout(request):
    if request.method == "POST":
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect("workout_list")
    else:
        form = WorkoutForm()
    return render(request, "workouts/workout_form.html", {"form": form})

@login_required
def delete_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id, user=request.user)
    workout.delete()
    return redirect("workout_list")

@login_required
def report_view(request):
    user_id = request.user.id
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM get_user_workout_stats(%s, %s, %s);",
            [user_id, start_date, end_date]
        )
        row = cursor.fetchone()
        avg_duration = row[0] if row else 0
        total_workouts = row[1] if row else 0

    return render(request, "workouts/reports.html", {
        "avg_duration": avg_duration,
        "total_workouts": total_workouts,
        "start_date": start_date,
        "end_date": end_date
    })
#def report_view(request):
#    workouts = Workout.objects.filter(user=request.user)
#    avg_duration = workouts.aggregate(Avg("duration"))['duration__avg']
#    total_workouts = workouts.count()
#    
#    return render(request, "workouts/report.html", {
#        "workouts": workouts,
#        "avg_duration": avg_duration,
#        "total_workouts": total_workouts,
#    }) 

