from django.db import models
import imagehash
import os

class ImageModel(models.Model):
    image = models.ImageField('Изображение', upload_to='images/')
    url = models.CharField(verbose_name='Хэш изображения', max_length=200, null=True)
    
    def set_image_hash(self, image):
        self.url = str(imagehash.average_hash(image))
        return self.url