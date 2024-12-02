from django import forms


class ImageUploadForm(forms.Form):
    """
    Setup the Form to allow uploading the image.
    """
    image = forms.ImageField(label='Upload an image')