from django.contrib import admin
from django.utils.html import format_html

from .models import FaceModel, ExampleModel


@admin.register(FaceModel)
class FaceModelAdmin(admin.ModelAdmin):
    list_display = ["fullname", "user_id_bold", "image_tag"]

    def image_tag(self, obj):
        return format_html(f'''<a href="{obj.image.url}" target="_blank"><img src="{obj.image.url}"
         alt="image" width="100 height="100" style="object-fit : cover;"/></a>''')

    def user_id_bold(self, obj):
        return format_html(f"<b>{obj.user_id}</b>")
