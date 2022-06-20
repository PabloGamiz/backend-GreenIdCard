from django.contrib import admin
from .models import (ClassificationData, ObjectData)

admin.site.register(ObjectData)
admin.site.register(ClassificationData)
