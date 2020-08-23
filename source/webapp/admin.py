from django.contrib import admin

from webapp.models import Task, Status, Task_type, Project

admin.site.register(Task)
admin.site.register(Task_type)
admin.site.register(Status)
admin.site.register(Project)
