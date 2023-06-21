"""
URL mappings for the todoitem app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from todo_item import views


router = DefaultRouter()
router.register('todo_item', views.TodoItemViewSet)

app_name = 'todo_item'

urlpatterns = [
    path('', include(router.urls)),
]
