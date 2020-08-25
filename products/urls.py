from django.urls import path
from .views import *

app_name="products"
urlpatterns = [
    path('new/', new, name='new'),
    path('create/', create, name="create"),
    path('', main, name="main"),
    path('<int:id>/', show, name="show"),
    path('<int:id>/edit/', update, name="update"),
    path('<int:product_id>/delete/', delete, name="delete"),
]