from django.db import models
from django.urls import reverse
import re

# Create your models here.


def create_slug(text):
    # Транслитерация
    transliteration_map = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh',
        'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
        'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts',
        'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu',
        'я': 'ya',
    }
    slug = ''.join(transliteration_map.get(c, c) for c in str(text).lower())
    # Замена пробелов и других символов на дефисы
    slug = re.sub(r'[^\w-]+', '-', slug).strip('-')
    slug = re.sub(r'[-]+', '-', slug)
    return slug


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='Россия', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Company(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    field = models.CharField(max_length=255)
    city = models.ForeignKey('City', on_delete=models.PROTECT)
    twogislink = models.CharField(max_length=255, blank=True, default='')
    enterpreneur = models.ForeignKey('Enterpreneur', on_delete=models.PROTECT)
    photoname = models.CharField(max_length=255, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('company', kwargs={'company_slug': self.slug})

    def save(self, **kwargs):
        slug = create_slug(self.name)
        count = 0
        while Company.objects.filter(slug=slug).exists():
            slug = slug[:-2] + '-' + str(count) if count != 0 else slug + '-' + str(count)
            count += 1
        self.slug = slug
        super().save(**kwargs)

    def __str__(self):
        return self.name


class Enterpreneur(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, blank=True, default='')
    fathername = models.CharField(max_length=255, blank=True, default='')
    phone = models.CharField(max_length=255, null=True, default='')
    email = models.CharField(max_length=255, null=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('enterpreneur', kwargs={'person_id': self.pk})

    def __str__(self):
        return f'{self.surname} {self.name} {self.fathername}: {self.phone}, {self.email}'
