from django.http import HttpResponse, JsonResponse
from .models import Shop
#Return HTML
from django.shortcuts import render


# Create your views here.
def say_hello(request):
    return HttpResponse("<h1>Hello my friend</>")

def about_my(request,my_name):
    return HttpResponse("<h1>About Screen</> <h2>Here will found info about %s.</>"  %my_name)


# Json Response
def get_all_shop(request):
    all_shop_query = Shop.objects.all()
    shops_as_list = list(all_shop_query)
    return JsonResponse(data=shops_as_list,safe=False)


def get_shop_by_id(request,shop_id):
    Shop.objects.get(shop_id)
    return JsonResponse(data=shop_id,safe=False)
    

def create_shop(request,shop_name):
    shop = Shop(name = shop_name)
    shop.save()
    return JsonResponse(data=shop,safe=False)

# Rerun html

def returnHtmlFile(request):
    title_prueba = "Pass a param title like a param"
    username = "Jorge Luis"
    product = Shop.objects.all()
    
    print(product)
    return render (request=request, template_name= "index.html",context= {
        'title': title_prueba,
        'username': username,
        'product:': product
    })

def returnHtmlFileAbout(request):
    return render (request=request, template_name= "about.html")

        
        

