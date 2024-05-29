import os
import shutil

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from shutil import copyfile


class FaceModel(models.Model):
    fullname = models.CharField(max_length=255)
    user_id = models.IntegerField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.fullname


class CheckFaceModel(models.Model):
    FaceModelCheck = models.ForeignKey('apps.FaceModel', on_delete=models.CASCADE)


@receiver(post_save, sender=CheckFaceModel)
def move_image_to_checked_images(sender, instance, **kwargs):
    if instance.FaceModelCheck.image:
        source_path = instance.FaceModelCheck.image.path
        destination_dir = "media/checked_images"
        destination_path = os.path.join(destination_dir, os.path.basename(source_path))
        if os.path.exists(source_path):
            os.makedirs(destination_dir, exist_ok=True)
            copyfile(source_path, destination_path)
