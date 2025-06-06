from django.urls import path

from .views import MyOrderView, CreateOrderProductView

urlpatterns = [
    path('', MyOrderView.as_view(), name="my_order"),
    path("agregar_producto/", CreateOrderProductView.as_view(), name="add_to_cart"),

]

