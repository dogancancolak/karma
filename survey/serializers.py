from rest_framework import serializers

from survey.models import SurveyItem, SurveyValue


class SurveyItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyItem
        fields = '__all__'

class SurveyValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyValue
        fields = '__all__'
