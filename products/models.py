from django.db import models
from ckeditor.fields import RichTextField



# Create your models here.


def upload_product_image(instance, filename):
    name = instance.name.lower().replace(' ', '-')
    return f"products/{name}/{filename}"

def upload_company_logo(instance, filename):
    name = instance.name.upper().replace(' ', '@')
    return f"companies/{name}/{filename}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to=upload_product_image)
    logo = models.ImageField(upload_to=upload_company_logo)

    def __str__(self):
        return self.name






