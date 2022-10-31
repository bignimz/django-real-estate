from django.contrib import admin
from django.urls import path
from listings.views import Listing_List, listing_delete, listing_retrieve, listing_create, listing_update, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path('listings/', Listing_List, name='listings'),
    path('listings/<pk>/', listing_retrieve),
    path('listings/<pk>/edit/', listing_update),
     path('listings/<pk>/delete/', listing_delete),
    path('add-listing/', listing_create),

]
