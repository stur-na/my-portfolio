from django.shortcuts import render
from blogpost.models import Post
from portfolio.models import Project_info
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from social import settings


def homepage(request):
    posts = Post.objects.order_by('-timestamp')[:3]
    portfolios = Project_info.objects.all()

    #contact form
    if request.method == 'POST':
        subject = 'You received a mail'
        body = {
            'subject': request.POST['subject'],
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message']
        }
        message = '\n'.join(body.values())
        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
            messages.info(request, 'Your message has been sent. Thank you!')
        except BadHeaderError:
            return HttpResponse('Bad Header Error')
    context = {
        'posts': posts,
        'portfolios': portfolios
        }
    return render(request, 'index.html', context)

def portfolio_home(request):
    return render(request, 'portfolio-home.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')
