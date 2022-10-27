from django.db.models import lookups
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from .serializers import TodoSerializer
from .models import Todo
from django.http import Http404
from django.db.models import Q

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    @action(detail = True)
    def search(self, request, pk=None):
        query = request.GET.get('search')
        result = Todo.objects.all()
        
        if query is not None:
            lookups = Q(title__icontains = query)
            result = Todo.objects.filter(lookups).distinct()
        
        serializer = TodoSerializer(result, many = True)
        json = serializer.data
        
        return Response(json, status = status.HTTP_201_CREATED)

# class searchTodo(viewsets.ModelViewSet):
#     serializer_class = TodoSerializer
#     queryset = Todo.objects.all()

#     @action(detail = True)
#     def search(self, request, pk=None):
#         query = request.GET.get('search')
#         result = Todo.objects.all()
        
#         if query is not None:
#             lookups = Q(title__icontains = query)
#             result = Todo.objects.filter(lookups).distinct()
        
#         serializer = TodoSerializer(result, many = True)
#         json = serializer.data
        
#         return Response(json, status = status.HTTP_201_CREATED)