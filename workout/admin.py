from django.contrib import admin
from workout.models import WorkoutSet, TrainingSession


admin.site.register(WorkoutSet)


class CustomTrainingSession(admin.ModelAdmin):
    model = TrainingSession
    save_on_top = True
    filter_horizontal = ("workout_sets",)


admin.site.register(TrainingSession)
