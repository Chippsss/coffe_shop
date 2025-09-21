from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("menu/", views.menu, name="menu"),
    path("place_order/", views.place_order, name="place_order"),
    path("cart/<int:order_id>/", views.cart, name="cart"),
    path("orders/", views.order_list, name="order_list"),
    path("orders/<int:order_id>/ready/", views.mark_ready, name="mark_ready"),
    path("ready_orders/", views.ready_orders, name="ready_orders"),
    path("pick/<int:order_id>/", views.pick_order, name="pick_order"),
    path("", views.customer_register, name="customer_register"),
]
