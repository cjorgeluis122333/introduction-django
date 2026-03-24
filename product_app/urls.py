from django.urls import  path
from . import views

urlpatterns = [
    # Return a text 
    path("", views.say_hello),
    path("about/<str:my_name>", views.about_my),
    #Json Crud
    path("crud/", views.get_all_shop),
    path("crud/create/<str:shop_name>",views.create_shop),
    #Return a html
    path("html/",views.returnHtmlFile),
    path("html/about",views.returnHtmlFileAbout)
]
