from django.conf.urls import url

from .views import get_survey, submit_survey

urlpatterns = [
    url(r'^submit$', submit_survey),
    url(r'^$', get_survey),
]

