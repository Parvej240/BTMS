from django.contrib import messages
from account.models import User
from doctor.models import Report
from django.forms import forms
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import send_mail
from blog.models import Blog

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from .models import Build_tank, Newsletter

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


def HomePage(request):
    blog = Blog.objects.filter(status=True).order_by('-id')[0:3]
    context = {
        'blogs': blog
    }
    return render(request, 'index.html', context)


@login_required(login_url='login')
def Calculate(request):
    return render(request, 'calculate.html')


def Contact(request):

    if request.method == 'POST':
        email = request.POST['email']
        message = request.POST['message']
        send_mail('Message From Contact Us', message,
                  email, ['test@gmail.com'], fail_silently=False)
        return render(request, 'contact.html', {'message': "Mail Sent Successfully"})

    return render(request, 'contact.html')


@login_required(login_url='login')
def user_report(request):
    user = User.objects.get(id=request.user.id)
    report = Report.objects.filter(user=user)
    context = {
        'reports': report
    }
    return render(request, 'user_report.html', context)


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


@login_required(login_url='login')
def report(request, id):
    user = User.objects.get(id=request.user.id)
    report = Report.objects.filter(user=user).filter(
        id=id)

    for key in report:
        print(key.user)
        data = {
            'username': key.user,
            'question': key.question,
            'answer': key.answer,
            'doctor': key.doctor
        }

    pdf = render_to_pdf('report_pdf.html', data)
    return HttpResponse(pdf, content_type='application/pdf')


def newsletter(request):
    if request.POST:
        Newsletter.objects.create(email=request.POST['email'])
        messages.success(request, 'Thank you for Subscribe')
    return render(request, 'thankyou.html')


@login_required(login_url='login')
def start_biofloc(request):
    if request.POST:
        tank_type = request.POST['tank_type']
        tanks = request.POST['tanks']
        if tank_type == '1':
            diameter = request.POST['diameter']
            height = request.POST['height']
            diameter = int(diameter) ** 2
            pie = 3.14/4
            cft = pie * diameter * int(height)
            liter = round(cft * 28.7)
            print('Liter:')
            print(round(liter, 2))
        else:
            length = request.POST['length']
            height = request.POST['height']
            width = request.POST['width']
            cft = int(length) * int(height) * int(width)
            liter = round(cft * 28.7)
            print('Liter:')
            print(liter)

        fish = round(liter * 0.6)
        feed = round(0.0417 * fish)
        Build_tank.objects.create(
            tanks=tanks, water=liter, fish=fish, food=feed, created_by=request.user)

        return redirect('builder')

    return render(request, 'startbuild.html')


@login_required(login_url='login')
def builder_page(request):
    build = Build_tank.objects.filter(created_by=request.user)
    context = {
        'build': build
    }
    return render(request, 'builder_report.html', context)


@login_required(login_url='login')
def builder_download(request, id):
    build = Build_tank.objects.filter(id=id)

    for key in build:

        data = {
            'username': request.user.username,
            'tanks': key.tanks,
            'water': key.water,
            'fish': key.fish,
            'food': key.food
        }

    pdf = render_to_pdf('report_tank.html', data)
    return HttpResponse(pdf, content_type='application/pdf')


def about(request):
    return render(request, 'about.html')


def policy(request):
    return render(request, 'policy.html')


def terms(request):
    return render(request, 'terms.html')

def userreport(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica', 14)
    lines = []

    user = User.objects.get(id=request.user.id)
    reports = Report.objects.filter(user=user)

    for report in reports:
        lines.append(report.question)
        lines.append(report.answer)
        lines.append("------------------------")
    
    
    for line in lines:
        textob.textLine(line)

    c.drawString(250, 50, "Biofloc User Report")
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='user_report.pdf')
