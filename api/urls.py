from django.urls import path 
from api import views

urlpatterns = [
    path('api/', views.country_list),
    path('api/<str:query_name>/<str:country_name>/', views.country_detail)
]