from django.http.response import JsonResponse
from rest_framework.decorators import api_view

from .models import SurveyItem
from .serializers import SurveyItemSerializer, SurveyValueSerializer


@api_view(['GET'])
# Create your views here.
def get_survey(request):
    questions = SurveyItem.objects.all()
    serializer = SurveyItemSerializer(questions, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def submit_survey(request):
    if request.method == 'POST':
        serializer = SurveyValueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data, safe=False)