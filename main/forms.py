from django import forms

class ImageUploadForm(forms.Form):

    image_url = forms.URLField(required=False)
    image_file = forms.ImageField(help_text='Загрузите картинку', required=False)