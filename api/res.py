import os 
import openai
import json
import re
from api.models import Country, Query
from google_images_search import GoogleImagesSearch

gis = GoogleImagesSearch('AIzaSyDdj1tm_nBO-Z0ZAWbwcLDgF5LsbQXB-Qo','c285b6813ec6e4a17')
openai.api_key = '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'

def update_model(final_list):
    '''
    Takes a list with countries, respective prices and query as input. 
    Updates the model with the details. 
    '''
    countries = final_list[0]
    prices = final_list[1]
    query_name = final_list[2]
    query_object, created = Query.objects.get_or_create(query=query_name)
    for i in range(len(countries)):
        name = countries[i].replace(".", "")
        name = name.strip()
        _search_params = {
        'q': name + ' Hospital Building 2022',
        'num': 1,
        'safe': 'off',
        'imgType': 'photo',
        'imgSize': 'medium'
        }

        gis.search(search_params = _search_params)
        url = ''
        for image in gis.results():
            url = image.url

        Country.objects.create(country_name=name,price=prices[i],image_url=url, highlights='', query=query_object)


def get_result(query_name):
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt="Find out the best 10 countries for {0} and the average cost of {1} in the countries. Answer in the following format: \n\n<country name>:<average price>\n".format(query_name, query_name),
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    response = json.loads(str(response))
    response = response["choices"][0]["text"].split("\n")
    result = []
    for r in response:
        r = r[2:]
        result.append(r.split(":"))
    countries = []
    prices = []
    for item in result:
        if len(item) == 2:
            countries.append(item[0])
            prices.append(item[1])

    result = [countries, prices, query_name]

    update_model(result)


def get_highlight(query_name, country_name):
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt="what are the highlights of {0} in {1}. List the top hospitals for {2} in {3} in bullet points.\n".format(query_name, country_name, query_name, country_name),
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    response = json.loads(str(response))
    text = response["choices"][0]["text"]

    return text