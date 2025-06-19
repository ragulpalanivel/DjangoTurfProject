from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Turf, Booking
from .forms import BookingForm
from datetime import date
from django.urls import reverse_lazy

@login_required
def book_turf(request, turf_id):
    turf = get_object_or_404(Turf, pk=turf_id)

    if turf.status != 'available':
        messages.error(request, "This turf is currently unavailable.")
        return redirect('/')  # Replace with your turf list view name

    if request.method == 'POST':
        print("Post request")
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.turf = turf
            booking.user = request.user
            print("Form valid")
            # Check if end_date > start_date and not in the past
            if booking.start_date < date.today():
                form.add_error('start_date', 'Start date cannot be in the past.')
            elif booking.end_date < booking.start_date:
                form.add_error('end_date', 'End date cannot be before start date.')
            else:
                booking.save()
                # turf.status = 'unavailable'  # Optionally mark as unavailable
                # turf.save()
                messages.success(request, f'Booking "{turf.name}".')
                # return redirect('/', booking.id)  # Replace with actual view
                return redirect(reverse_lazy('create_order'))

    else:
        form = BookingForm()

    return render(request, 'book_turf.html', {'form': form, 'turf': turf})
