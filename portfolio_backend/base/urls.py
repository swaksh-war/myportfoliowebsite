from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('blog', views.BlogView, basename='blog')
router.register('project', views.ProjectView, basename='project')
router.register('education', views.EducationView, basename='education')
router.register('experience', views.ExperienceView, basename='experience')

urlpatterns = [
    path('', include(router.urls))
]
