from django.db import models
import os
# Create your models here.


class ScreenShots(models.Model):
    img = models.ImageField(blank=True, upload_to='django_project/static')
    img_name = models.TextField(max_length=256,default=None, null=True)
    created = models.TextField(max_length=256,default=None, null=True)
    latitude = models.TextField(max_length=256, default=None, null=True)
    longitude = models.TextField(max_length=256, default=None, null=True)


    @property
    def filename(self):
        return os.path.basename(self.img.name)

    def get_img_url(self):
        return self.filename


class Files(models.Model):
    file = models.FileField(blank=True, upload_to='django_project/static')
    file_name = models.TextField(max_length=256,default=None, null=True)