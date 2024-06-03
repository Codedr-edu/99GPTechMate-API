from django.shortcuts import render
from .GPTeensearch import GPTeen
from .GPTeacher import search_document, search_image
from .models import *
from .GPTuniversity import gptu_check
# Create your views here.


def GPTeen_image(request):
    if request.method == "POST":
        image = request.FILE.get("images")

        sql = ImageSaver(image=image)
        sql.save()

        result = search_image(image=sql.image.url)
        context = {"result": result}

        return render(request, "GPTeen/image/result.html", context=context)
    return render(request, "GPTeen/image/index.html")


def GPTeen_document(request):
    if request.method == "POST":
        document = request.FILE.get("document")

        sql = DocumentSaver(document=document)
        sql.save()

        result = search_document(image=sql.document.url)
        context = {"result": result}

        return render(request, "GPTeen/document/result.html", context=context)
    return render(request, "GPTeen/document/index.html")


def GPTeen(request):
    if request.method == "POST":
        text = request.POST.get("gpteen")

        result = GPTeen(prompt=text)
        context = {"result": result}

        return render(request, "GPTeen/result.html", context=context)
    return render(request, "GPTeen/index.html")


def GPTUniversity(request):
    if request.method == "POST":
        document = request.FILE.get("document")

        sql = UniversitySaver(document=document)
        sql.save()

        result = gptu_check(image=sql.document.url)
        context = {"result": result}

        return render(request, "GPTeen/university/result.html", context=context)
    return render(request, "GPTeen/university/index.html")
