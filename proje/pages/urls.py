from django.urls import path
from . import views
urlpatterns= [
    path('' , views.index , name="index"),
    path('girisyap' , views.girisyap , name="girisyap"),
    path('kayitol' , views.kayitol , name="kayitol"),
    path('muzik' , views.muzik , name="muzik"),
    path('oyun' , views.oyunlar , name="oyunlar"),
    path('uncharted2' , views.uncharted2 , name="uncharted2"),
    path('uncharted3' , views.uncharted3, name="uncharted3"),
    path('uncharted4' , views.uncharted4 , name="uncharted4"),
    path('uncharted5' , views.uncharted5 , name="uncharted5"),
]