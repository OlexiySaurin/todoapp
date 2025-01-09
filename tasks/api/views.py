from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from tasks import models
from tasks.api import serializers


class TaskListCreateAPIView(ListCreateAPIView):
    serializer_class = serializers.SimpleTaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return models.SimpleTask.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        
class TaskRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.SimpleTaskSerializer
    permission_classes = [IsAuthenticated]
    queryset = models.SimpleTask.objects.all()
    lookup_field = 'pk'
    
    def get_queryset(self):
        return models.SimpleTask.objects.filter(user=self.request.user)