from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView )

from task.models import Task
from api.serializers import TaskSerializer

# Example using function based views
# -----------------------------------

@api_view(['GET', 'POST'])
def task_list(request):
    """
    List all task, or create a new one
    """

    # GET Request
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks)
        return Response(serializer.data)

    # POST Request
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.DATA)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    """
    Get, update, or delete a specific task
    """
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # GET request
    if request.method == 'GET':
        serializer = TaskSerializer( task )
        return Response( serializer.data )

    # PUT request
    if request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.DATA)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    # DELETE request
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Example using class based views
# -----------------------------------
# class TaskMixin(object):
#     """
#     Mixin to inherit from.
#     Here we're setting the query set and the serializer
#     """
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

# class TaskList(TaskMixin, ListCreateAPIView):
#     """
#     Return a list of all the tasks, or
#     create new ones
#     """
#     pass

# class TaskDetail(TaskMixin, RetrieveUpdateDestroyAPIView):
#     """
#     Return a specific task, update it, or delete it.
#     """
#     pass






