from django.shortcuts import render, redirect, get_object_or_404
from .models import MenuItem, Order
from django.contrib.auth.decorators import login_required
from .decorators import group_required
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .forms import CustomerSignUpForm

def customer_register(request):
    if request.method == "POST":
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            # Add to Customer group
            customer_group, created = Group.objects.get_or_create(name="Customer")
            user.groups.add(customer_group)

            # Auto login after registration
            login(request, user)
            return redirect("orders:menu")
    else:
        form = CustomerSignUpForm()
    return render(request, "orders/register.html", {"form": form})

# Customer: View menu
@group_required("Customer")
def menu(request):
    items = MenuItem.objects.all()
    return render(request, "orders/menu.html", {"items": items})

# Customer: Place an order
@login_required
@group_required("Customer")
def place_order(request):
    if request.method == "POST":
        item_ids = request.POST.getlist("items")
        if not item_ids:
            return redirect("orders:menu")  # or show a message
        order = Order.objects.create(customer=request.user)
        order.items.set(MenuItem.objects.filter(id__in=item_ids))
        order.save()
        return redirect("orders:cart", order_id=order.id)

# Customer: View cart/order summary
@login_required
@group_required("Customer")
def cart(request, order_id):
    order = get_object_or_404(Order, id=order_id, customer=request.user)
    return render(request, "orders/cart.html", {"order": order})

# Staff: View all orders
@login_required
@group_required("Staff")
def order_list(request):
    orders = Order.objects.filter(status="pending")
    return render(request, "orders/order_list.html", {"orders": orders})

# Staff: Mark as ready
@login_required
@group_required("Staff")
def mark_ready(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = "ready"
    order.save()
    return redirect("orders:order_list")

# Delivery: View ready orders
@login_required
@group_required("Delivery")
def ready_orders(request):
    orders = Order.objects.filter(status="ready")
    return render(request, "orders/ready_orders.html", {"orders": orders})

# Delivery: Pick an order
@login_required
@group_required("Delivery")
def pick_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = "delivering"
    order.save()
    return redirect("orders:ready_orders")
