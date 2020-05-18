from django.shortcuts import render,get_object_or_404, redirect
from django.forms import modelform_factory

from .models import Meeting,Room

# Create your views here.

def details(request,id):
    meeting = get_object_or_404(Meeting,pk=id)
    return render(request,"meetings/details.html", {"meeting": meeting})

def room(request):
    return render(request,"meetings/room_details.html",
                  {"rooms": Room.objects.all()})

MeetingForm = modelform_factory(Meeting,exclude=[])

def new(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MeetingForm()
        return render(request, "meetings/new.html", {"form": form})

