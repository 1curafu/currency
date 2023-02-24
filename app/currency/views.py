
from currency.models import Rate, ContactUs
from django.shortcuts import render


def list_rates(request):
    rates = Rate.objects.all()

    context = {
        "rates": rates
    }

    return render(request, 'rates_list.html', context)


def list_contacts(request):
    contacts = ContactUs.objects.all()

    context = {
        "contacts": contacts
    }

    return render(request, 'contactus.html', context)
