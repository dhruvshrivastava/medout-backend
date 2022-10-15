from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.models import Country, Query
from api.serializers import CountrySerializer, QuerySerializer
from api.res import get_result, get_highlight

@csrf_exempt
def country_list(request):
    if request.method == 'GET':
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QuerySerializer(data=data)
        if serializer.is_valid():
            query_name = data['query']
            query_name = query_name.replace("_", " ")
            serializer.save()
            # Get the data from OpenAPI function
            # Update fields in Hospital Model 
            if not Query.objects.get(query=query_name).exists():
                get_result(query_name)
                countries = Country.objects.filter(query__query=query_name)
                serializer_new = CountrySerializer(countries, many=True)
                return JsonResponse(serializer_new.data, safe=False)
            if Query.objects.get(query=query_name).exists():
                countries = Country.objects.filter(query__query=query_name)
                serializer_new = CountrySerializer(countries, many=True)
                return JsonResponse(serializer_new.data, safe=False)

# Get highlight from another function in res.py
# Update the country model with the highlight 
# Return the country details 

@csrf_exempt
def country_detail(request, query_name, country_name):
    query_name = query_name.replace("_", " ")
    country_name = country_name.replace("_", " ")
    query_object = Query.objects.get(query=query_name)
    if request.method == 'GET':
        c_obj = Country.objects.filter(query=query_object, country_name=country_name)
        for obj in c_obj:
            if obj['highlights'] == '':  
                if c_obj.exists():
                    highlight = get_highlight(query_name, country_name)
                    Country.objects.filter(query=query_object, country_name=country_name).update(highlights=highlight)
        
        try: 
            country = Country.objects.filter(query=query_object, country_name=country_name)
        except Country.DoesNotExist:
            return HttpResponse(status=404)

        serializer = CountrySerializer(country, many=True)
        return JsonResponse(serializer.data, safe=False)
