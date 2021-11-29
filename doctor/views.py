from django.contrib import messages
from django.http import response
from django.http.response import HttpResponse
from .models import Booking, Report
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from account.models import Profile, User
from .forms import BookingForm
from django.urls import reverse_lazy

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
# Create your views here.


class doctorView(ListView):
    model = User
    context_object_name = 'doctors'
    template_name = 'doctor/doctor_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctors'] = context['doctors'].filter(
            user_type=self.request.user.IS_DOCTOR)
        return context


class BookingFormView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'doctor/booking_form.html'

    def form_valid(self, form):
        form.instance.booker = Profile.objects.get(
            id=self.request.user.profile.id)
        form.instance.fisheries = User.objects.get(id=self.kwargs['id'])
        return super(BookingFormView, self).form_valid(form)

    success_url = reverse_lazy('profile')


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def report(request):

    user = User.objects.filter(user_type='USER').filter(is_staff=False)
    constant = {
        'users': user
    }

    if request.method == 'POST':
        username = request.POST['username']
        question = request.POST['question']
        message = request.POST['message']
        doctor = request.user.id
        user = User.objects.get(id=username)
        doctor = User.objects.get(id=doctor)
        report = Report(user=user, question=question,
                        answer=message, doctor=doctor)
        report.save()
        messages.success(
            request, 'Report Created Successfully.' + user.username)
        # data = {
        #     'username': request.POST['username'],
        #     'question': request.POST['question'],
        #     'message': request.POST['message'],
        #     'doctor': request.user.username
        # }

        # pdf = render_to_pdf('report_pdf.html', data)
        # return HttpResponse(pdf, content_type='application/pdf')

    return render(request, 'doctor/report.html', constant)
