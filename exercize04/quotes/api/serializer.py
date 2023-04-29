from rest_framework import serializers
from quotes.models import quote
from datetime import datetime
from django.utils.timesince import timesince

class QuotesSerializer(serializers.ModelSerializer):
    date_since_publication = serializers.SerializerMethodField()
    
    class Meta:
        model = quote
        fields = "__all__"
    
    def get_date_since_publication(self, obj):
        time_delta = timesince(obj.create_at, datetime.now())
        return time_delta 