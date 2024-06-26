from django.urls import path, include
from . import views

urlpatterns = [
    path("tasks/", views.Tasks.as_view()),
    path("tasks/<int:pk>/", views.SavedTasks.as_view())
]
