from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from booking.models import Booking
from .models import Payment
import razorpay
import pkg_resources

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

def initiate_payment(request, booking_id):
    print("Initiating Razorpay Payment...")  # ✅ Debug log
    booking = get_object_or_404(Booking, id=booking_id)

    amount = int(booking.turf.price * 100)  # ₹ to paise
    order = client.order.create({
        'amount': amount,
        'currency': 'INR',
        'payment_capture': '1'
    })

    Payment.objects.create(
        booking=booking,
        razorpay_order_id=order['id']
    )

    context = {
        'booking': booking,
        'order_id': order['id'],
        'amount': amount,
        'razorpay_key': settings.RAZORPAY_KEY_ID,
        'callback_url': '/payments/callback/'
    }
    return render(request, 'payments/payment_page.html', context)

@csrf_exempt
def payment_callback(request):
    if request.method == "POST":
        data = request.POST
        try:
            payment = Payment.objects.get(razorpay_order_id=data['razorpay_order_id'])
            payment.razorpay_payment_id = data['razorpay_payment_id']
            payment.razorpay_signature = data['razorpay_signature']
            payment.is_paid = True
            payment.booking.is_paid = True
            payment.booking.save()
            payment.save()
            return render(request, 'payments/success.html')
        except Payment.DoesNotExist:
            return render(request, 'payments/failure.html')