from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskEditView, TaskDeleteView, TaskLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', TaskLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name ='logout'),
    path('', TaskListView.as_view(), name='task'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='detail'),
    path('task/create/', TaskCreateView.as_view(), name='create'),
    path('task/<int:pk>/update/', TaskEditView.as_view(), name='edit'),
    path('task/<int:pk>/delete' ,TaskDeleteView.as_view(), name='delete')
]
