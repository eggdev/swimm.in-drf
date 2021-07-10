from rest_framework import serializers
from workout.models import Set


# class WorkoutSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         # model = User
#         fields = ["sets"]


class SetSerializer(serializers.Serializer):
    class Meta:
        model = Set
        fields = ["repetitions", "stroke", "distance", "interval", "equipment"]