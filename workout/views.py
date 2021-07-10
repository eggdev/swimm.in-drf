from rest_framework import viewsets
from rest_framework import permissions
from workout.serializers import SetSerializer
from workout.models import Set


class SetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Set.objects.all().order_by("id")
    serializer_class = SetSerializer
    permission_classes = []