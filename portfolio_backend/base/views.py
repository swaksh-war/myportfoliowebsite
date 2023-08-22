from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action

from .models import Blog, Experience, Education, Project
from .serializers import BlogSerializer, EducationSerializer, ExperienceSerializer, ProjectSerializer

# Create your views here.

class BlogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def list(self, request, *args, **kwargs):
        projects = self.get_queryset()
        serialized_projects = self.serializer_class(projects, many=True).data

        custom_response = {
            'status': 'success',
            'message': 'Projects retrieved successfully',
            'data': serialized_projects
        }

        return Response(custom_response)



class EducationView(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def list(self, request, *args, **kwargs):
        projects = self.get_queryset()
        serialized_projects = self.serializer_class(projects, many=True).data

        custom_response = {
            'status': 'success',
            'message': 'Projects retrieved successfully',
            'data': serialized_projects
        }

        return Response(custom_response)


class ExperienceView(viewsets.ModelViewSet):
    queryset =Experience.objects.all()
    serializer_class = ExperienceSerializer

    def list(self, request, *args, **kwargs):
        projects = self.get_queryset()
        serialized_projects = self.serializer_class(projects, many=True).data

        custom_response = {
            'status': 'success',
            'message': 'Projects retrieved successfully',
            'data': serialized_projects
        }

        return Response(custom_response)
    

class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def list(self, request, *args, **kwargs):
        projects = self.get_queryset()
        serialized_projects = self.serializer_class(projects, many=True).data

        custom_response = {
            'status': 'success',
            'message': 'Projects retrieved successfully',
            'data': serialized_projects
        }

        return Response(custom_response)
