from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django_filters.views import FilterView

from currency.models import Rate, ContactUs, Source, RequestResponseLog
from currency.forms import RateForm, ContactUsForm, SourceForm
from currency.filters import RateFilter, SourceFilter, ContactUsFilter, RequestResponseLogFilter


class RateListView(FilterView):
    queryset = Rate.objects.all().select_related('source')
    template_name = 'rates_list.html'
    paginate_by = 10
    filterset_class = RateFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_pagination'] = '&'.join(
            f'{key}={value}' for key, value in self.request.GET.items() if key != 'page'
        )
        return context


class RateDetailView(LoginRequiredMixin, DetailView):
    queryset = Rate.objects.all()
    template_name = 'rates_details.html'


class RateCreateView(CreateView):
    queryset = Rate.objects.all()
    template_name = 'rates_create.html'
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')


class RateUpdateView(UserPassesTestMixin, UpdateView):
    queryset = Rate.objects.all()
    template_name = 'rates_update.html'
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')

    def test_func(self):
        return self.request.user.is_superuser


class RateDeleteView(UserPassesTestMixin, DeleteView):
    queryset = Rate.objects.all()
    template_name = 'rates_delete.html'
    success_url = reverse_lazy('currency:rate-list')

    def test_func(self):
        return self.request.user.is_superuser


class ContactUsListView(FilterView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus.html'
    paginate_by = 10
    filterset_class = ContactUsFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_pagination'] = '&'.join(
            f'{key}={value}' for key, value in self.request.GET.items() if key != 'page'
        )
        return context


class ContactUsDetailView(DetailView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_details.html'


class ContactUsCreateView(CreateView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_create.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('currency:contact-list')

    def _send_mail(self):
        subject = 'User ContactUs'
        message = f'''
            Request from: {self.object.name}.
            Reply to email: {self.object.email}.
            Subject: {self.object.subject}.
            Message: {self.object.message}.
        '''
        from currency.tasks import send_mail
        send_mail.apply_async(
            kwargs={'subject': subject, 'message': message},
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_mail()
        return redirect


class ContactUsUpdateView(UpdateView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_update.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('currency:contact-list')


class ContactUsDeleteView(DeleteView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_delete.html'
    success_url = reverse_lazy('currency:contact-list')


class SourceListView(FilterView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'
    paginate_by = 10
    filterset_class = SourceFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_pagination'] = '&'.join(
            f'{key}={value}' for key, value in self.request.GET.items() if key != 'page'
        )
        return context


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


class RequestResponseLogListView(FilterView):
    queryset = RequestResponseLog.objects.all()
    template_name = 'request_response_log_list.html'
    paginate_by = 10
    filterset_class = RequestResponseLogFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_pagination'] = '&'.join(
            f'{key}={value}' for key, value in self.request.GET.items() if key != 'page'
        )
        return context


class RequestResponseLogDeleteView(DeleteView):
    template_name = 'request_response_log_delete.html'
    success_url = reverse_lazy('currency:req-list')
    queryset = RequestResponseLog.objects.all()
