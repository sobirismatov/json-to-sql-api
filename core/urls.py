from django.contrib import admin
from django.urls import path
from api.views import add_product, get_all_product, get_product, delete_product, update_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', add_product),
    path('get/', get_all_product),
    path('get/<int:pk>', get_product),
    path('del/<int:pk>', delete_product),
    path('update/<int:pk>', update_product),
]
