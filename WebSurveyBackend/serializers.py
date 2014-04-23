__author__ = 'isr'

from rest_framework import serializers
from WebSurveyBackend.models import Poll


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('question', 'pub_date', 'choices')