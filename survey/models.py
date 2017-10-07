from django.db import models


class SurveyItem(models.Model):
    surveyQuestion = models.CharField(max_length=255)
    value = models.BooleanField(default=None)

class SurveyValue(models.Model):
    userId = models.IntegerField() # should be user later
    surveyItem = models.ForeignKey(SurveyItem)
    answer = models.BooleanField()