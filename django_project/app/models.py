from django.db import models
from django.urls import reverse

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    twogislink = models.CharField(max_length=255, null=True, blank=True)
    enterpreneur = models.ForeignKey('Enterpreneur', on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('company', kwargs={'company_id': self.pk})

    def __str__(self):
        return self.name


class Enterpreneur(models.Model):
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('enterpreneur', kwargs={'person_id': self.pk})

    def __str__(self):
        return self.name
