from django.db import models


class SurveyItem(models.Model):
    surveyQuestion = models.TextField(max_length=255)

    def get_question(self):
        choices = SurveyChoice.objects.filter(question=self)
        return {
            'question': self.surveyQuestion,
            'choices': choices,
        }


class SurveyChoice(models.Model):
    text = models.TextField(max_length=255)
    question = models.ForeignKey(SurveyItem)
