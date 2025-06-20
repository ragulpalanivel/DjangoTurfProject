from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking
from mainapp.models import Turf
from .forms import BookingForm
from datetime import date, datetime
from django.urls import reverse_lazy

@login_required
def book_turf(request, turf_id):
    turf = get_object_or_404(Turf, pk=turf_id)

    # if turf.status != 'available':
    #     messages.error(request, "This turf is currently unavailable.")
    #     return redirect('/')  # Replace with your turf list view name

    if request.method == 'POST':
        print("Post request")
        form = BookingForm(request.POST)
        if form.is_valid():
            past_bookings = Booking.objects.filter(user = request.user)
            past_bookings.delete()
            booking = form.save(commit=False)
            booking.turf = turf
            booking.user = request.user
            print("Form valid")
            # Check if booking_date is not in the past
            if booking.booking_date.date() < date.today():
                form.add_error('booking_date', 'Booking date cannot be in the past.')
            else:
                booking.save()
                messages.success(request, f'Booking "{turf.name}".')
                return redirect(reverse_lazy('create_order'))

    else:
        form = BookingForm()

    return render(request, 'book_turf.html', {'form': form, 'turf': turf})
