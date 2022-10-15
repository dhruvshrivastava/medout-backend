from django.db import models

class Query(models.Model):
    query = models.CharField(max_length=10000)

class Country(models.Model):
    country_name = models.CharField(max_length=1000)
    price = models.CharField(max_length=10000)
    image_url = models.CharField(max_length=100000)
    highlights = models.TextField()
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    
    class Meta: 
        ordering = ['price']

class Hospital(models.Model):
    hospital_name = models.CharField(max_length=1000)
    country_name = models.CharField(max_length=10000)
    address = models.TextField()
    website_url = models.CharField(max_length=10000)
    phone = models.CharField(max_length=100)

    # TODO: Add image support 

class MedicalService(models.Model):

    # TODO: Migrate to PostgreSQL and add Array field for medical_service and price 

    medical_service = models.CharField(max_length=10000)
    price = models.CharField(max_length=10000)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)


