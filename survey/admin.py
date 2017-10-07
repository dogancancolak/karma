from django.contrib import admin

from .models import SurveyItem, SurveyValue

# Register your models here.


admin.site.register(SurveyItem)
admin.site.register(SurveyValue)