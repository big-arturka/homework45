"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from webapp.views import IndexView, ProjectView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, \
    ProjectUserUpdate
from webapp.views.task_views import TaskCreateView, TaskView, TaskUpdateView, TaskDeleteView

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_view'),
    path('project/add/', ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('project/<int:pk>/task/add/', TaskCreateView.as_view(), name='task_create'),
    path('project/<int:project_pk>/task/<int:pk>', TaskView.as_view(), name='task_view'),
    path('project/<int:project_pk>/task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_update'),
    path('project/<int:project_pk>/task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),

    path('project/<int:pk>/users/', ProjectUserUpdate.as_view(), name='users_add'),

    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),

    path('accounts/', include('accounts.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
