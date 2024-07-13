from django.shortcuts import render, get_object_or_404

from photo.models import Photo


def photo(request, id):
    photo = Photo.objects.filter(user_photo=id)
    return render(request, 'photo.html', {'photo': photo})

def photo_det(request, pk):
    photo = get_object_or_404(Photo, id=pk)
    photo_det = Photo.objects.filter(photo=pk)
    return render(request, 'photo_det.html', {'photo_det': photo_det})