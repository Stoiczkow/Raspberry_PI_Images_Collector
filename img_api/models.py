from django.db import models
import os
# Create your models here.


class ScreenShots(models.Model):
    img = models.ImageField(blank=True, upload_to='img_api/static')
    created = models.DateTimeField(default=None, null=True)
    coordinates = models.TextField(max_length=1024, default=None, null=True)

    def filename(self):
        return os.path.basename(self.img.name)

    def get_img_url(self):
        return self.img.url[8:]