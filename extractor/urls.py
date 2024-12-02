from django.urls import path

from .views import upload_image, image_detail, list_images

urlpatterns = [
    path("", upload_image, name="upload_image"),
    path("list", list_images, name="list_images"),
    path("image/<int:image_id>/", image_detail, name="image_detail"),
]
