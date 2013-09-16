from django.shortcuts import get_object_or_404

import json

from verdantadmin.modal_workflow import render_modal_workflow
from verdantimages.models import Image
from verdantimages.forms import ImageForm


def get_image_json(image):
    """
    helper function: given an image, return the json to pass back to the
    image chooser panel
    """
    preview_image = image.get_in_format('130x100')

    return json.dumps({
        'id': image.id,
        'title': image.title,
        'preview': {
            'url': preview_image.url,
            'width': preview_image.width,
            'height': preview_image.height,
        }
    })

def chooser(request):
    images = Image.objects.order_by('title')
    form = ImageForm()

    return render_modal_workflow(
        request, 'verdantimages/chooser/chooser.html', 'verdantimages/chooser/chooser.js',
        {'images': images, 'form': form}
    )


def image_chosen(request, image_id):
    image = get_object_or_404(Image, id=image_id)

    return render_modal_workflow(
        request, None, 'verdantimages/chooser/image_chosen.js',
        {'image_json': get_image_json(image)}
    )


def chooser_upload(request):
    if request.POST:
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            image = form.save()
            return render_modal_workflow(
                request, None, 'verdantimages/chooser/image_chosen.js',
                {'image_json': get_image_json(image)}
            )
    else:
        form = ImageForm()

    images = Image.objects.order_by('title')

    return render_modal_workflow(
        request, 'verdantimages/chooser/chooser.html', 'verdantimages/chooser/chooser.js',
        {'images': images, 'form': form}
    )
