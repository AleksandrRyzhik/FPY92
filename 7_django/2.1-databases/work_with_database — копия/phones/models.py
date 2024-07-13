from django.db import models

class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50, null=True)
    price = models.SmallIntegerField(null=True)
    image = models.URLField(max_length=200, null=True, unique=True)
    release_date = models.DateField(null=True)
    lte_exists = models.BooleanField(null=True)
    slug = models.SlugField(null=True)