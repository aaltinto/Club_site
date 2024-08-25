from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Episode)
admin.site.register(models.Serie)
admin.site.register(models.Season)
admin.site.register(models.Actor)
admin.site.register(models.Category)
