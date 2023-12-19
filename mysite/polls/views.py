from django.http import HttpResponse

def index(requst):
    return HttpResponse("hello my first django code")