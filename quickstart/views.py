from django.shortcuts import get_object_or_404
#from django.views.decorators.cache import never_cache
from rest_framework.response import Response
from rest_framework import viewsets,generics
from quickstart.models import Student,Teacher,Department,ReportCard
from quickstart.serializers import StudentSerializer, TeacherSerializer, DepartmentSerilaizer, ReportCardSerializer

class StudentviewSet(viewsets.ViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    #@never_cache
    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)
        
    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors) 

    def update(self, request, pk=None):
        instance = self.queryset.get(pk=pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)    

    def destroy(self, request, pk=None):
        instance = self.queryset.get(pk=pk)
        instance.delete()    

class TeacherviewSet(viewsets.ViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
    def list(self,request):
        serializer = self.serializer_class(self.queryset,many=True)
        return Response(serializer.data)  

    def retrieve(self, request, pk=None):
        t = Teacher.objects.get(pk=pk)
        serializer = self.serializer_class(t)
        return Response(serializer.data)
        
    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, pk=None):
        instance = self.queryset.get(pk=pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
  
    def destroy(self, request, pk=None):
        instance = self.queryset.get(pk=pk)
        instance.delete()
        return Response(status=204)

class DepartmentViewSet(viewsets.ViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerilaizer

    def list(self,request):
        serializer = self.serializer_class(self.queryset,many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self,request,pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        instance = self.queryset.get(pk=pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
  
    def destroy(self, request, pk=None):
        instance = self.queryset.get(pk=pk)
        instance.delete()
        return Response(status=204)


class ReportCardViewSet(viewsets.ViewSet):
    queryset = ReportCard.objects.all()
    serializer_class = ReportCardSerializer

    def list(self,request):
        serializer = self.serializer_class(self.queryset,many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self,request,pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        instance = self.queryset.get(pk=pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
  
    def destroy(self, request, pk=None):
        instance = self.queryset.get(pk=pk)
        instance.delete()
        return Response(status=204)

