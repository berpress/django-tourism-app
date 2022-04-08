from django.shortcuts import render
from .models import Accommodation
from django.shortcuts import get_object_or_404


def main(request):
    return render(request, "mainapp/index.html")


def about(request):
    return render(request, "mainapp/about.html")


def book(request, name="Hotel", cost="1000"):
    content = {"name": name, "cost": cost}
    return render(request, "mainapp/book.html", content)


def accommodations(request):
    title = "accommodation"
    list_of_accommodations = Accommodation.objects.filter(is_active=True)
    content = {"title": title, "list_of_accommodations": list_of_accommodations}
    return render(request, "mainapp/accommodations.html", content)


def accommodation(request, pk):
    title = "products"
    content = {"title": title, "accommodation": get_object_or_404(Accommodation, pk=pk)}
    return render(request, "mainapp/accommodation_details.html", content)
