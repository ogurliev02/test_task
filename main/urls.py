from django.urls import path
from .views import ImagesView, UploadImageView, ImageDetailView

urlpatterns = [
    path('', ImagesView.as_view()),
    path('upload/', UploadImageView.as_view()),
    path('<str:image_hash>/', ImageDetailView.as_view()),
]