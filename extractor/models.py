from django.db import models


class ImageColor(models.Model):
    """
    Image color Model to store the image and the hex color for the center-most pixel.
    """
    image = models.ImageField(upload_to='uploads/')
    hex_color = models.CharField(max_length=7)

    def __str__(self):
        return f"ImageColor({self.hex_color})"
