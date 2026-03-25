from rest_framework import routers
from .api import ProjectViewSet

routers = routers.DefaultRouter()

# This router will automatically generate the URL patterns for the ProjectViewSet
# Give to me the methods (GET,POST,PUT,PATCH,DELETE)
routers.register(
    prefix='projects',
    viewset=ProjectViewSet,
    basename='projects'
    )

#This sed  urlpatterns received all urls created by the router
urlpatterns = routers.urls
