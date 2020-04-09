from django.shortcuts import render, redirect

# Create your views here.
from bobinage.forms import ArchiveCreateForm
from bobinage.models import Archive


def index(request):
    archives = Archive.objects.all()
    dictionary = {
        'archives': archives
    }
    return render(request, 'bobinage/index.html', dictionary)

def add(request):
    if request.method == "POST":
        form = ArchiveCreateForm(request.POST)
        if form.is_valid():
            archive = form.save(commit=False)
            archive.save()
            return redirect('bobinage:index')
    else:
        form = ArchiveCreateForm()
    return render(request, 'bobinage/add.html', {'form': form})