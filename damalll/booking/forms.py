from django import forms
from .models import Booking
from django.forms.widgets import DateInput
from datetime import date

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['booking_date', 'time_slot']
        widgets = {
            'booking_date': DateInput(attrs={'type': 'date'}),
            # Remove custom widget for 'time_slot' to use model's TIME_SLOTS choices
        }

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        today = date.today().isoformat()
        self.fields['booking_date'].widget.attrs['min'] = today

def clean(self):
    cleaned_data = super().clean()
    booking_date = cleaned_data.get('booking_date')
    time_slot = cleaned_data.get('time_slot')
    today = date.today()

    if booking_date and booking_date.date() < date.today():
        self.add_error('booking_date', 'Booking date cannot be in the past.')

    return cleaned_data
