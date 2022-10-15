from rest_framework import serializers
from api.models import Country, Query

#TODO; Create serializers for Hospital and Medical Service

class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ['id', 'query']

class CountrySerializer(serializers.ModelSerializer):
   class Meta:
    model = Country
    fields = ['id', 'country_name', 'price','image_url', 'highlights', 'query']

