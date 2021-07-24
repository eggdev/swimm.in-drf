from django.contrib.auth import get_user_model
from rest_framework import serializers
from workout.models import WorkoutSet, TrainingSession


class WorkoutSetSerializer(
    serializers.PrimaryKeyRelatedField, serializers.ModelSerializer
):
    id = serializers.ReadOnlyField()
    # Sets can have a name - optional
    # repetitions - required
    # distance - required
    # stroke - required (default Free)
    # interval - required
    # equipment - optional (default none)
    # created_by = UserField() - required, only one
    # target_heart_rate_range - optional

    class Meta:
        model = WorkoutSet
        fields = ["id", "repetitions", "distance", "stroke", "interval", "equipment"]


class TrainingSessionSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    workout_sets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=WorkoutSet.objects.all()
    )

    # This will be the athletes that should have access to this training session
    # athletes = AthleteSerializer(many=True, required=False)

    # Calculated value on creation/update - can be used for sorting
    # total_distance = _get_total_distance(sets=sets)

    @classmethod
    def _get_total_distance(workout_sets):
        # math to add up all the distance in each set
        return

    # I want to add multiple sets
    # Add rest after individual sets (would a rest count as a set, but not one that is created?)
    # The order matters in generating this so would this be a new object?

    # What distance metric will be used? Yards or Meters

    # Calculate total yardage of all combined sets
    # Calculate total time the workout will take

    # Must have 1 set to make a workout
    # Workouts can be named
    # Who created the workout
    # What athletes workout should be sent to

    # Will have sections to it
    ## Warmup, drill, mainset. User can define section names
    class Meta:
        model = TrainingSession
        fields = ["id", "name", "workout_sets"]