from django.shortcuts import render

from .models import Activity
from .forms import ActivityInputForm


# Create your views here.
def activity_example_view(request):
    obj = Activity.objects.get(id=2)
    context = {
        'title': obj.title,
        'description': obj.description
    }
    return render(request, "activity_example.html", context)


def activity_input_view(request):
    form = ActivityInputForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "activity_input.html", context)
