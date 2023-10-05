from django.urls import path
from MainApp import views


urlpatterns = [
    path('', views.index,),
    path('about', views.about),
    path('item/<int:id>', views.get_item),
    path('items', views.items_list),
    path('countries', views.countrie_list),
    path('Australia', views.Australia),
    path('Austria', views.Austria),
    path('Bahamas', views.Bahamas),
]