from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from currency.models import Rate, ContactUs, Source
from currency.forms import RateForm, ContactUsForm, SourceForm


def list_rates(request):
    rates = Rate.objects.all()

    context = {
        "rates": rates
    }

    return render(request, 'rates_list.html', context)


def rates_details(request, pk):
    rate = get_object_or_404(Rate, pk=pk)

    context = {
        "rate": rate
    }

    return render(request, 'rates_details.html', context)


def rates_create(request):
    if request.method == "POST":
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == "GET":
        form = RateForm()

    context = {
        'form': form
    }
    return render(request, 'rates_create.html', context)


def rates_update(request, pk):
    rate = get_object_or_404(Rate, pk=pk)

    if request.method == "POST":
        form = RateForm(request.POST, instance=rate)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == "GET":
        form = RateForm(instance=rate)

    context = {
        'form': form,
    }
    return render(request, 'rates_update.html', context)


def rates_delete(request, pk):
    rate = get_object_or_404(Rate, pk=pk)

    if request.method == "POST":
        rate.delete()
        return HttpResponseRedirect('/rate/list/')
    elif request.method == "GET":
        context = {
            'rate': rate,
        }
        return render(request, 'rates_delete.html', context)


def list_contacts(request):
    contacts = ContactUs.objects.all()

    context = {
        "contacts": contacts
    }

    return render(request, 'contactus.html', context)


def contact_details(request, pk):
    contact = get_object_or_404(ContactUs, pk=pk)

    context = {
        "contact": contact
    }

    return render(request, 'contact_details.html', context)


def contact_create(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact/list/')
    elif request.method == "GET":
        form = ContactUsForm()

    context = {
        'form': form
    }
    return render(request, 'contact_create.html', context)


def contact_update(request, pk):
    contact = get_object_or_404(ContactUs, pk=pk)

    if request.method == "POST":
        form = ContactUsForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact/list/')
    elif request.method == "GET":
        form = ContactUsForm(instance=contact)

    context = {
        'form': form,
    }
    return render(request, 'contact_update.html', context)


def contact_delete(request, pk):
    contact = get_object_or_404(ContactUs, pk=pk)

    if request.method == "POST":
        contact.delete()
        return HttpResponseRedirect('/contact/list/')
    elif request.method == "GET":
        context = {
            'contact': contact,
        }
        return render(request, 'contact_delete.html', context)


def list_sources(request):
    sources = Source.objects.all()

    context = {
        "sources": sources
    }

    return render(request, 'sources_list.html', context)


def source_details(request, pk):
    source = get_object_or_404(Source, pk=pk)

    context = {
        "source": source
    }

    return render(request, 'source_details.html', context)


def source_create(request):
    if request.method == "POST":
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/list/')
    elif request.method == "GET":
        form = SourceForm()

    context = {
        'form': form
    }
    return render(request, 'source_create.html', context)


def source_update(request, pk):
    source = get_object_or_404(Source, pk=pk)

    if request.method == "POST":
        form = SourceForm(request.POST, instance=source)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/list/')
    elif request.method == "GET":
        form = SourceForm(instance=source)

    context = {
        'form': form,
    }
    return render(request, 'source_update.html', context)


def source_delete(request, pk):
    source = get_object_or_404(Source, pk=pk)

    if request.method == "POST":
        source.delete()
        return HttpResponseRedirect('/source/list/')
    elif request.method == "GET":
        context = {
            'source': source,
        }
        return render(request, 'source_delete.html', context)
