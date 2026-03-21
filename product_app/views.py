from django.http import HttpResponse, JsonResponse
from .models import Shop, Product

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

def create_shop(request,shop_name):
    shop = Shop(name = shop_name)
    shop.save()
    return JsonResponse(data=shop,safe=False)

def update_shop(request,shop_id,shop_new_name):
    temp_shop = Shop.objects.all.get(shop_id)
    shop = Shop(id =shop_id, name =shop_new_name)
    shop.save()
    return JsonResponse(shop,safe=False)
        
        



