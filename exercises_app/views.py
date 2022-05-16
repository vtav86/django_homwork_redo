# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from exercises_app.models import Article, StatusChoices, Band


# Create your views here.
def calculator(request, a, b):
    value = a + b
    return HttpResponse(f"The number is {value}")


def calculatorsub(request, a, b):
    value = a - b
    return HttpResponse(f"The number is {value}")


def calculatormultiply(request, a, b):
    value = a * b
    return HttpResponse(f"The number is {value}")


def calculatordivide(request, a, b):
    value = a / b
    return HttpResponse(f"The number is {value}")


def articles(request):
    context = {
        "articles": Article.objects.filter(status=StatusChoices.IN_WRITING)
    }
    return render(request, "articleview.html", context)

def show_band(request,band_id):
    # This is a solution to work with render request. Need to use objects.filter
    # context = {"band_info": Band.objects.filter(pk=band_id)}
    # return render(request,'bandinfo.html', context)
    # This is a solution to work with httpresponse. Need to use objects.get
    band = Band.objects.get(pk=band_id)
    return HttpResponse(f'Band { band.name } plays genre { band.genre }. They were formed in { band.year }')



