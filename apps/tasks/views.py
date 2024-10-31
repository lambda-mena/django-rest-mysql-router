from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from . import models, serializers


class Tasks(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        user_tasks = models.Task.objects.filter(user=request.user)
        serialized_tasks = serializers.ListTaskSerializer(user_tasks, many=True)
        return Response(serialized_tasks.data, status=200)

    def post(self, request: Request):
        serialized_task = serializers.CreateTaskSerializer(data=request.data)
        if serialized_task.is_valid():
            models.Task.objects.create(user=request.user, **serialized_task.validated_data)
            return Response(status=201)
        else:
            return Response(serialized_task.errors, status=400)


class SavedTasks(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def find_task(self, user, pk):
        user_task = models.Task.objects.filter(user=user, pk=pk).first()
        if not user_task:
            raise NotFound()
        return user_task

    def get(self, request, pk=None):
        user_task = self.find_task(request.user, pk)
        serialized_task = serializers.GetTaskSerializer(user_task)
        return Response(serialized_task.data, status=200)

    def put(self, request, pk=None):
        user_task = self.find_task(request.user, pk)
        serialized_data = serializers.UpdateTaskSerializer(data=request.data)
        if serialized_data.is_valid():
            models.Task.objects.filter(pk=user_task.pk).update(**serialized_data.data)
            return Response(status=200)
        else:
            return Response(serialized_data.errors, status=404)

    def delete(self, request, pk=None):
        user_task = self.find_task(request.user, pk)
        user_task.delete()
        return Response(status=200)
