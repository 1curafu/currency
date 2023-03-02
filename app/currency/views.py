from django.urls import reverse_lazy
from currency.models import Rate, ContactUs, Source
from currency.forms import RateForm, ContactUsForm, SourceForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class RateListView(ListView):
    queryset = Rate.objects.all()
    template_name = 'rates_list.html'


class RateDetailView(DetailView):
    queryset = Rate.objects.all()
    template_name = 'rates_details.html'


class RateCreateView(CreateView):
    queryset = Rate.objects.all()
    template_name = 'rates_create.html'
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')


class RateUpdateView(UpdateView):
    queryset = Rate.objects.all()
    template_name = 'rates_update.html'
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')


class RateDeleteView(DeleteView):
    queryset = Rate.objects.all()
    template_name = 'rates_delete.html'
    success_url = reverse_lazy('currency:rate-list')


class ContactUsListView(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus.html'


class ContactUsDetailView(DetailView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_details.html'


class ContactUsCreateView(CreateView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_create.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('currency:contact-list')


class ContactUsUpdateView(UpdateView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_update.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('currency:contact-list')


class ContactUsDeleteView(DeleteView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_delete.html'
    success_url = reverse_lazy('currency:contact-list')


class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'


class SourceDetailView(DetailView):
    queryset = Source.objects.all()
    template_name = 'source_details.html'


class SourceCreateView(CreateView):
    queryset = Source.objects.all()
    template_name = 'source_create.html'
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')


class SourceUpdateView(UpdateView):
    queryset = Source.objects.all()
    template_name = 'source_update.html'
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')


class SourceDeleteView(DeleteView):
    queryset = Source.objects.all()
    template_name = 'source_delete.html'
    success_url = reverse_lazy('currency:source-list')
