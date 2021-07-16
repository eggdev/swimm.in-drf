from django.contrib.auth import get_user_model
from rest_framework import serializers
from workout.models import Set


class SetSerializer(serializers.ModelSerializer):
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
        model = Set
        fields = ["id", "repetitions", "distance", "stroke", "interval", "equipment"]


class WorkoutSerializer(serializers.HyperlinkedModelSerializer):
    sets = SetSerializer(many=True, required=True)
    # athletes = AthleteSerializer(many=True, required=False)
    # total_distance = _get_total_distance(sets=sets)

    @classmethod
    def _get_total_distance(sets):
        # math to add up all the distance in each set
        return

    # I want to add multiple sets
    # Add rest after individual sets (would a rest count as a set?)
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
        # model = User
        fields = ["sets"]