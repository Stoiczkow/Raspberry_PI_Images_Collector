from django.db import models
import os
# Create your models here.


class ScreenShots(models.Model):
    img = models.ImageField(blank=True, upload_to='django_project/static')
    created = models.TextField(max_length=256,default=None, null=True)
    latitude = models.TextField(max_length=256, default=None, null=True)
    longitude = models.TextField(max_length=256, default=None, null=True)


    @property
    def filename(self):
        return os.path.basename(self.img.name)

    def get_img_url(self):
        return self.filename
