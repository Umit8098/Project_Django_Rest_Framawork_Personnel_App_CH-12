from django.shortcuts import render
from .models import Department, Personnel
from .serializers import DepartmentSerializer, PersonnelSerializer, DepartmentPersonnelSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsStafforReadOnly, IsOwnerAndStaffOrReadOnly
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class DepartmentView(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    permission_classes = [IsAuthenticated, IsStafforReadOnly]


class PersonnelListCreateView(generics.ListCreateAPIView):
    serializer_class = PersonnelSerializer
    queryset = Personnel.objects.all()
    # permission_classes = [IsAuthenticated, IsStafforReadOnly]
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if self.request.user.is_staff:
            personnel = self.perform_create(serializer)
            data = {
                "message": f"Personnel {personnel.first_name} saved succesfully.",
                "personnel": serializer.data
            }
        else:
            data = {
                "message": "You are not authorized to perform this operation."
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        person = serializer.save()
        person.create_user = self.request.user
        person.save()
        return person


class PersonnelGetUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    # permission_classes = [IsAuthenticated, IsOwnerAndStaffOrReadOnly]
    permission_classes = [IsAuthenticated, ]
    
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user.is_staff and (instance.create_user == self.request.user):
            return self.update(request, *args, **kwargs)
        else:
            data = {
                "message": "You are not authorized to perform this operation"
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    
    def delete(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return self.destroy(request, *args, **kwargs)
        else:
            data = {
                "message": "You are not authorized to perform this operation"
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)


# 1. Yöntem dinamik url ->
class DepartmentPersonnelView(generics.ListAPIView):
    serializer_class = DepartmentPersonnelSerializer
    queryset = Department.objects.all()
    
    def get_queryset(self):
        name = self.kwargs['department']
        return Department.objects.filter(name__iexact=name)


# 2. Yöntem dinamik url ->
class DepartmentPersonnelViewCustom(generics.RetrieveAPIView):
    serializer_class = DepartmentPersonnelSerializer
    queryset = Department.objects.all()
    lookup_field= "name"
    