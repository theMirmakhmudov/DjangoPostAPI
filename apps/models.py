from django.db import models


class FaceModel(models.Model):
    fullname = models.CharField(max_length=255)
    user_id = models.IntegerField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.fullname
