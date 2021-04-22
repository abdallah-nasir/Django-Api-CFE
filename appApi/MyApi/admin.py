from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.

class StatusAdmin(admin.ModelAdmin):
    list_display=["user","updated"]
    class Meta:
        model = Status
admin.site.register(Status,StatusAdmin)
