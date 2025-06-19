from django import forms
from .models import Booking
from django.forms.widgets import DateInput
from datetime import date

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_date', 'booking_time']
        widgets = {
            'booking_date': DateInput(attrs={'type': 'date'}),
            'booking_time': DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        today = date.today().isoformat()
        self.fields['start_date'].widget.attrs['min'] = today
        self.fields['end_date'].widget.attrs['min'] = today

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        today = date.today()

        if start_date and start_date < today:
            self.add_error('start_date', 'Start date cannot be in the past.')

        if start_date and end_date and end_date < start_date:
            self.add_error('end_date', 'End date cannot be before start date.')

        return cleaned_data