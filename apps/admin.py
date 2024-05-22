from django.contrib import admin
from django.utils.html import format_html

from .models import FaceModel


@admin.register(FaceModel)
class FaceModelAdmin(admin.ModelAdmin):
    list_display = ["fullname", "user_id", "image_tag"]

    def image_tag(self, obj):
        return format_html(f'''<a href="{obj.image.url}" target="_blank"><img src="{obj.image.url}"
         alt="image" width="100 height="100" style="object-fit : cover;"/></a>''')
