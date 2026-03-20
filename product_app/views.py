from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse("<h1>Hello my friend</>")

def about_my(request):
    return HttpResponse("About Screen")