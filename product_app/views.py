from django.http import HttpResponse, JsonResponse
from .models import Shop
#Return HTML
from django.shortcuts import render
#Return a form
from .forms import CreateNewShop

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
    shop =  Shop.objects.get(shop_id)
    return JsonResponse(data=shop,safe=False)
    

def create_shop(request,shop_name):
    shop = Shop(name = shop_name)
    shop.save()
    # Devuelve un JSON serializable con los datos de la tienda creada
    return JsonResponse(data={
        'id': shop.id,
        'name': shop.name,
    }, safe=False)

# Rerun html

def returnHtmlFile(request):
    title_prueba = "Pass a param title like a param"
    username = "Jorge Luis"
    product = Shop.objects.all()
    
    print(product)
    return render (request=request, template_name= "index.html",context= {
        'title': title_prueba,
        'username': username,
        'product': product
    })

def returnHtmlFileAbout(request):
    return render (request=request, template_name= "about.html")

def create_form(request):
    # Uso GET para recibir parámetros en la URL: /create_form?name=tienda1
    name = request.GET.get("name")
    created = False
    created_shop = None

    if name:
        # Guarda la tienda solo cuando venga el name por GET
        created_shop = Shop.objects.create(name=name)
        created = True

    return render(request, "create_shop.html", {
        "form": CreateNewShop(),
        "created": created,
        "created_shop": created_shop,
    })

        
        

