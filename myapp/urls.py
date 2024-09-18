from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TaskListCreateView,
    TaskDetailUpdateDeleteView,
    SubTaskListCreateView,
    SubTaskDetailUpdateDeleteView,
    CategoryViewSet,
    UserTaskListView,
    UserSubTaskListView
)

# Создаем маршрутизатор и регистрируем в нем ViewSet для категорий
router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    # Маршруты для задач (Task)
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailUpdateDeleteView.as_view(), name='task-detail-update-delete'),

    # Маршруты для подзадач (SubTask)
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail-update-delete'),

    # Маршруты для получения задач и подзадач текущего пользователя
    path('user/tasks/', UserTaskListView.as_view(), name='user-task-list'),
    path('user/subtasks/', UserSubTaskListView.as_view(), name='user-subtask-list'),

    # Добавление маршрутов, зарегистрированных через DefaultRouter для Category
    path('', include(router.urls)),
]