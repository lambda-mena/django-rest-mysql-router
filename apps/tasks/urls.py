from django.urls import path
from . import views

urlpatterns = [
    path("tasks/", views.Tasks.as_view()),
    path("tasks/<int:pk>/", views.SavedTasks.as_view())
]
