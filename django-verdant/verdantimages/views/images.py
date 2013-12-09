from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from verdantimages.models import get_image_model
from verdantimages.forms import get_image_form
from verdantadmin.forms import SearchForm

@login_required
def index(request):
    Image = get_image_model()
    form = SearchForm()

    q = None
    p = request.GET.get("p", 1)
    is_searching = False

    if 'q' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']

            is_searching = True
            images = Image.search(q, results_per_page=20, page=p)
        else:
            images = Image.objects.order_by('-created_at')
    else:
        images = Image.objects.order_by('-created_at')
        form = SearchForm()

    if not is_searching:
        paginator = Paginator(images, 20)

        try:
            images = paginator.page(p)
        except PageNotAnInteger:
            images = paginator.page(1)
        except EmptyPage:
            images = paginator.page(paginator.num_pages)

    if request.is_ajax():
        return render(request, "verdantimages/images/results.html", {
            'images': images,
            'is_searching': is_searching,
            'search_query': q,
        })
    else:
        return render(request, "verdantimages/images/index.html", {
            'form': form,
            'images': images,
            'is_searching': is_searching,
            'popular_tags': Image.popular_tags(),
            'search_query': q,
        })


@login_required
def edit(request, image_id):
    Image = get_image_model()
    ImageForm = get_image_form()

    image = get_object_or_404(Image, id=image_id)

    if request.POST:
        original_file = image.file
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            if 'file' in form.changed_data:
                # if providing a new image file, delete the old one and all renditions.
                # NB Doing this via original_file.delete() clears the file field,
                # which definitely isn't what we want...
                original_file.storage.delete(original_file.name)
                image.renditions.all().delete()
            form.save()
            messages.success(request, "Image '%s' updated." % image.title)
            return redirect('verdantimages_index')
        else:
            messages.error(request, "The image could not be saved due to errors.")
    else:
        form = ImageForm(instance=image)

    return render(request, "verdantimages/images/edit.html", {
        'image': image,
        'form': form,
    })


@login_required
def delete(request, image_id):
    image = get_object_or_404(get_image_model(), id=image_id)

    if request.POST:
        image.delete()
        messages.success(request, "Image '%s' deleted." % image.title)
        return redirect('verdantimages_index')

    return render(request, "verdantimages/images/confirm_delete.html", {
        'image': image,
    })


@login_required
def add(request):
    ImageForm = get_image_form()

    if request.POST:
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            messages.success(request, "Image '%s' added." % image.title)
            return redirect('verdantimages_index')
        else:
            messages.error(request, "The image could not be created due to errors.")
    else:
        form = ImageForm()

    return render(request, "verdantimages/images/add.html", {
        'form': form,
    })


@login_required
def search(request):
    Image = get_image_model()
    images = []
    q = None
    is_searching = False
    if 'q' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']

            # page number
            p = request.GET.get("p", 1)
            is_searching = True
            images = Image.search(q, results_per_page=20, page=p)
    else:
        form = SearchForm()

    if request.is_ajax():
        return render(request, "verdantimages/images/results.html", {
            'images': images,
            'is_searching': is_searching,
            'search_query': q,
        })
    else:
        return render(request, "verdantimages/images/index.html", {
            'form': form,
            'images': images,
            'is_searching': is_searching,
            'popular_tags': Image.popular_tags(),
            'search_query': q,
        })
