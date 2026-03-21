from django.urls import  path
from . import views

urlpatterns = [
    # just html
    path("", views.say_hello),
    path("about/<str:my_name>", views.about_my),
    #Json Crud
    path("crud/", views.get_all_shop),
    path("crud/create/<str:shop_name>",views.create_shop),
    path("crud/update/<str:shop_id>/<str:shop_new_name>",views.update_shop),
    
    
]
