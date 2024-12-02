import numpy as np
from PIL import Image, UnidentifiedImageError
from io import BytesIO
from django.shortcuts import render, get_object_or_404
from .forms import ImageUploadForm
from .models import ImageColor


def upload_image(request):
    """
    View function to upload the image from local storage.
    """
    context = {}
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data["image"]

            try:
                # Open the image directly from memory
                image = Image.open(uploaded_file)

                # Ensure the image is valid and can be processed
                image.verify()  # This checks the integrity of the image

                # Reopen the image as it's been verified
                image = Image.open(uploaded_file)

                # Get the width and height of the image for finding the center
                width, height = image.size

                # Center coordinates
                center_x_value = width // 2
                center_y_value = height // 2

                # Get the pixel data directly using numpy
                image_data = np.array(image)

                # Determine the 4 center-most pixels' coordinates
                center_pixels = image_data[
                    center_y_value - 1 : center_y_value + 1, center_x_value - 1 : center_x_value + 1
                ]

                # Average the RGB values of the 4 pixels
                avg_pixel = np.mean(center_pixels, axis=(0, 1)).astype(int)

                # Convert to hex color
                hex_color = f"#{avg_pixel[0]:02x}{avg_pixel[1]:02x}{avg_pixel[2]:02x}"

                # Save the hex color and image to the database
                image_color = ImageColor(image=uploaded_file, hex_color=hex_color)
                image_color.save()

                # Get all images from the database to display
                all_images = ImageColor.objects.all()

                # Prepare context data for rendering
                context["all_images"] = all_images

                return render(request, "extractor/list_images.html", context)

            except UnidentifiedImageError:
                # Handle the case where the file is not a valid image
                form.add_error("image", "The uploaded file could not be identified as a valid image.")
            except Exception as e:
                form.add_error("image", f"An unexpected error occurred: {str(e)}")
        else:
            context["form"] = form
            print(form.errors)
    else:
        form = ImageUploadForm()
        context["form"] = form

    return render(request, "extractor/upload_image.html", context)


def image_detail(request, image_id):
    """
    Get the image details view function.

    Args:
        request: request object containing the request details and information
        image_id: The ID of the image to fetch from the database
    """
    # Get the image by its ID (primary key)
    image = get_object_or_404(ImageColor, id=image_id)

    # Return the image details page
    return render(request, "extractor/image_detail.html", {"image": image})


def list_images(request):
    """
    View function to list all uploaded images and their associated hex colors.
    """
    all_images = ImageColor.objects.all()
    return render(request, "extractor/list_images.html", {"all_images": all_images})
