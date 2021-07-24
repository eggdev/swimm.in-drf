from rest_framework import viewsets
from rest_framework import permissions
from workout.serializers import (
    TrainingSessionSerializer,
    WorkoutSetSerializer,
)
from workout.models import WorkoutSet, TrainingSession


class WorkoutSetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = WorkoutSet.objects.all().order_by("id")
    serializer_class = WorkoutSetSerializer
    permission_classes = [permissions.IsAuthenticated]


class TrainingSessionViewSet(viewsets.ModelViewSet):
    """
    API Endpoints for a full workout
    """

    queryset = TrainingSession.objects.all()
    serializer_class = TrainingSessionSerializer
    permission_classes = [permissions.IsAuthenticated]