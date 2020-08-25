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
    path('<int:product_id>/create_comment', create_comment, name="create_comment"),
    path('<int:comment_id>/delete_comment', delete_comment, name="delete_comment"),
]