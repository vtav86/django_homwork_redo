from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def converter(request):
    if request.method == "GET":
        return render(request, 'conversion_form.html')
    if request.method == "POST":
        degrees = float(request.POST.get('degrees'))
        conversion_type = request.POST.get('conversionType')
        if conversion_type == "FahrToCelc":
            value = (degrees - 32) * (5 / 9)
            return HttpResponse(f"{degrees} degrees Fahrenheit is equal to {value} degrees Celsius")
        elif conversion_type == "celcToFahr":
            value = (degrees * (9 / 5)) + 32
            return HttpResponse(f"{degrees} degrees Celsius is equal to {value} degrees Farenheit")


@csrf_exempt
def login(request):
    if request.method == "GET" and request.session.get('loggedUser') is None:
        return render(request, 'login.html')
    elif request.method == "POST":
        request.session['loggedUser'] = request.POST.get('name')
        return HttpResponse(f'User {request.session["loggedUser"]} now logged in!')
    elif request.method == "GET" and request.session['loggedUser']:
        return HttpResponse(f'Welcome {request.session["loggedUser"]}')


def del_session(request):
    del request.session['loggedUser']
    return HttpResponse('Logged User Deleted')


@csrf_exempt
def add_to_session(request):
    if request.method == "GET":
        return render(request, "add_to_session.html")
    elif request.method == "POST":
        key = request.POST.get('key')
        value = request.POST.get('value')
        request.session[key] = value
        return HttpResponse(f'Key {key} and value {value} has been set')


@csrf_exempt
def show_all_session(request):
    key = [key for key in request.session.keys()]
    values = [value for value in request.session.values()]
    session_info = {'temp_keys': key, 'temp_values': values}
    return render(request, 'show_all_sessions.html', context=session_info)


def set_cookie(request):
    response = HttpResponse("Cookie 'user' has just been set in your browser!")
    response.set_cookie("user", "Vatche")
    return response


def show_cookie(request):
    user_cookie = request.COOKIES.get("user")
    if user_cookie is None:
        return HttpResponse("Cookie 'user' is not set!")
    return HttpResponse(f"Cookie 'user' = {user_cookie}")


def delete_cookie(request):
    user_cookie = request.COOKIES.get("user")
    if user_cookie is None:
        return HttpResponse("There was no cookie 'user'.")
    response = HttpResponse("Cookie 'user' has just been deleted from your browser!")
    response.delete_cookie("user")
    return response


@csrf_exempt
def add_to_cookie(request):
    if request.method == "GET":
        return render(request, 'add_to_cookie.html')
    if request.method == "POST":
        key = request.POST.get('key')
        value = request.POST.get('value')
        response = HttpResponse(f"Cookie with key {key} and value {value} has been set!")
        response.set_cookie(key, value)
        return response


@csrf_exempt
def show_all_cookies(request):
    pairs = request.COOKIES.items()
    return render(request, 'show_all_cookies.html', context={'pairs': pairs})
