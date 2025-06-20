from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.contrib import messages

from booking.models import Booking
from .models import Order, Address
from .forms import AddressForm, OrderForm

@login_required
def create_order(request):
    """Create an order from the user's cart items and redirect to the Select Address view."""
    user = request.user
    booking = Booking.objects.get(user = request.user)


    # Calculate the total amount of the cart
    total_amount = 1000

    # Create an order record
    order = Order.objects.create(
        user=user,
        total_amount=total_amount,
        order_date=now(),
        status='PENDING',
        booking = booking,
        turf = booking.turf
    )
    print(order)
    order.save()
    # rental_bike.delete()
    # Clear the cart after creating the order

    # Redirect to the Select Address view
    # return redirect('select_address_for_order', order_id=order.id)
    return redirect('payment:create_razorpay_order', order_id = order.id)

@login_required
def order_history(request):
    """Display the order history of the user."""
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'order_history.html', {'orders': orders})

# the below view is just another version of the previous view to try out a different appearance
@login_required
def order_history_2(request):
    """Display the order history of the user."""
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'order_history_2.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    """Display details of a specific order."""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'order_detail.html', {'order': order})

@login_required
def add_address(request):
    """Allow the user to add a new address."""
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            # Set default address if it's the first one
            if not Address.objects.filter(user=request.user).exists():
                address.is_default = True
            address.save()
            # Redirect to the referring page
            next_url = request.GET.get('next', 'homepage')
            return redirect(next_url)  # Redirect to the referring page (e.g., select_address)
    else:
        form = AddressForm()
    return render(request, 'add_address.html', {'form': form})

@login_required
def select_address_for_order(request, order_id):
    """Allow the user to select an address for the order and proceed to payment."""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    addresses = request.user.addresses.all()

    if request.method == 'POST':
        # Get the selected address ID from the form
        address_id = request.POST.get('address')

        # redirect back to the same page if no address is selected
        if not address_id:
            return redirect('select_address_for_order', order_id=order.id)

        address = get_object_or_404(Address, id=address_id, user=request.user)
        
        # Associate the selected address with the order
        order.address = address
        order.save()
        
        # Redirect to the Razorpay order creation and payment page
        return redirect('payment:create_razorpay_order', order_id=order.id)

    return render(request, 'select_address.html', {'order': order, 'addresses': addresses})

@login_required
def update_order(request, order_id):
    """Allow the user to update order details."""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_detail', order_id=order.id)
    else:
        form = OrderForm(instance=order)
    return render(request, 'update_order.html', {'form': form})


@login_required
def cancel_order(request, order_id):
    """Cancel an order and redirect the user."""
    order = get_object_or_404(Order, id=order_id, user=request.user)

    # Check if the order is still pending
    if order.status == "PENDING":
        order.status = "CANCELLED"
        order.save()
        messages.success(request, "Your order has been cancelled.")
    else:
        messages.error(request, "This order cannot be cancelled.")

    return redirect("homepage") 