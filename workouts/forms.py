from django import forms
from .models import Workout

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'date', 'duration']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }