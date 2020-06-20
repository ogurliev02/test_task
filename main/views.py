from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import HttpResponse
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from .models import ImageModel
from .forms import ImageUploadForm
import requests
from PIL import Image
import os
from io import BytesIO

class ImagesView(View):

    def get(self, request):
        images = ImageModel.objects.all()
        return render(request, 'images/images_list.html', {'images_list': images})

class UploadImageView(View):

    def get(self, request): return render(request, 'images/upload.html', {'form': ImageUploadForm})
    
    def post(self, request):
        image_file = request.FILES
        image_url = request.POST['image_url']
        if image_file and image_url: return render(request, 'images/upload_error.html')
        if image_file:
            form = ImageUploadForm(request.POST, request.FILES)
            if form.is_valid():
                m = ImageModel()
                m.image = form.cleaned_data['image_file']
                image = Image.open(form.cleaned_data['image_file'])
                m.image.name = m.set_image_hash(image)
                m.save()
                return render(request, 'images/image_detail.html', {'image': m})
        else:
            raw_image = requests.get(image_url)
            image_for_hash = Image.open(BytesIO(raw_image.content))

            image = ImageModel()
            image.save()

            img_temp = NamedTemporaryFile(delete = True)
            img_temp.write(raw_image.content)
            img_temp.flush()

            image.image.save(image.set_image_hash(image_for_hash), File(img_temp))
            image.save()
            return HttpResponse('Загрузили фотографию, проверяй в списке')

class ImageDetailView(View):

    def get(self, request, image_hash):
        image = ImageModel.objects.filter(url=image_hash)
        width, height, size = request.GET.get('width'), request.GET.get('height'), request.GET.get('size')
        sizes = [width, height, size]

        return render(request, 'images/image_detail.html', {'image': image, 'sizes': sizes})