
from django.urls import path, include
from apps.bookmodule import views


urlpatterns = [
    #path('arguments in URL', views.function_name, name=???)
    path('', views.index, name='index'), #in views.py we must add the index function
    path('2', views.index2, name='index2'),
    path('book/<val>', views.index3, name='index'),
]


