from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response



from .models import ToDo
from .serializers import ToDoSerializer


class ToDoView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()


class ToDoCreateView(generics.CreateAPIView):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()


class getAllView(generics.ListAPIView):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()


