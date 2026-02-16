from django.urls import path
from .views import ListListView, ListDetailView, ListCreateView, TaskCreateView
from .views import ListDeleteView, TaskDeleteView

urlpatterns = [
    path('', ListListView.as_view(), name='list-list'),
    path('list/<int:pk>/', ListDetailView.as_view(), name='list-detail'),

    path('add-list/', ListCreateView.as_view(), name='add-list'),
    path('add-task/', TaskCreateView.as_view(), name='add-task'),

    path('list/<int:pk>/delete/', ListDeleteView.as_view(), name='list-delete'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),

]
