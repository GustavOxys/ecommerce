from tkinter.tix import IMAGE
from django.db import models
from PIL import Image
import os
from django.conf import settings
from django.utils.text import slugify
from utils import utils


class Product(models.Model):

    name = models.CharField(max_length=50)
    description_short = models.TextField(max_length=255)
    description_long = models.TextField()
    image = models.ImageField(upload_to='product_images/%Y/%m/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    price_marketing = models.FloatField(verbose_name='Price')
    price_marketing_promotional = models.FloatField(default=0, verbose_name='Price Promo')
    type = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variable'),
            ('S', 'Simple')
        )
    )

    def get_price_formated(self):
        return utils.formate_price(self.price_marketing)
    get_price_formated.short_description = 'Price'

    def get_price_promotional_formated(self):
        return utils.formate_price(self.price_marketing_promotional)
    
    get_price_promotional_formated.short_description = 'Price Promo'

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return
        
        new_height = round((new_width * original_height) / original_width)
        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )
        
    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.name)}'
            self.slug = slug


        super().save(*args, **kwargs)

        max_image_size = 800

        if self.image:
            self.resize_image(self.image, max_image_size)

    def __str__(self):
        return self.name
    

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    price_promotional = models.FloatField(default=0)
    inventory = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name or self.product.name
    
    class Meta:
        verbose_name = 'Variation'
        verbose_name_plural = 'Variations'


