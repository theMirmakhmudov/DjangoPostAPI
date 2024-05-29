import os
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import FaceModel


@receiver(pre_delete, sender=FaceModel)
def delete_image_file(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
