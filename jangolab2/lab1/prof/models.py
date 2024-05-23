from django.db import models
from django.shortcuts import reverse

class Prof(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    registration_date = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=100, null=True)
    department = models.CharField(max_length=100)
    rank = models.CharField(max_length=50)

    @classmethod
    def get_list_url(cls):
        return reverse('prof_list')
