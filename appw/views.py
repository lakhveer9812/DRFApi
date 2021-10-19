from functools import partial
from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets


class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        x = Student.objects.all()
        y = StudentSerializer(x, many=True)
        return Response(y.data)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            x = Student.objects.get(id=id)
            y = StudentSerializer(x)
            return Response(y.data)

    def create(self,request):
        y = StudentSerializer(data=request.data)
        if y.is_valid():
            y.save()
            return Response({'msg': "Data Created"}, status=status.HTTP_201_CREATED)
        return Response(y.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        id = pk
        x = Student.objects.get(pk=id)
        y = StudentSerializer(x, data=request.data)
        if y.is_valid():
            y.save()
            return Response({'msg': "Complete Data Updated!"})
        return Response(y.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request, pk):
        id = pk
        x = Student.objects.get(pk=id)
        y = StudentSerializer(x, data=request.data, partial=True)
        if y.is_valid():
            y.save()
            return Response({'msg': "Partial Data Updated!"})
        return Response(y.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        id = pk
        x = Student.objects.get(pk=id)
        x.delete()
        return Response({"msg": "Data Deleted"})
