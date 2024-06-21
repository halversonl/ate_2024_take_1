from django.shortcuts import render, redirect

from .models import Activity
from .forms import ActivityInputForm


# Create your views here.
def activity_example_view(request):
    obj = Activity.objects.get(id=2)
    context = {
        'title': obj.title,
        'description': obj.description,
        'date': obj.date
    }
    return render(request, "activity_example.html", context)


def activity_input_view(request):
    form = ActivityInputForm()
    if request.method == 'POST':
        form = ActivityInputForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        form = ActivityInputForm



    context = {
        'form': form
    }
    return render(request, "activity_input.html", context)

