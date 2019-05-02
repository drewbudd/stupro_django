from django.contrib import admin
from .models import CADModel,Marker,Status,Type

# Register your models here.
admin.site.register(CADModel)
admin.site.register(Marker)
admin.site.register(Status)
admin.site.register(Type)
