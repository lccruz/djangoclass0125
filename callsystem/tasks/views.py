from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer


@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.filter(owner=request.user)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        task = serializer.save()
        task.owner.add(request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Reponse(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

