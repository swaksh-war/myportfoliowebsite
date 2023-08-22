from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Blog)
admin.site.register(models.Education)
admin.site.register(models.Experience)
admin.site.register(models.Project)