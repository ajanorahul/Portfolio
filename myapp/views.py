from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.conf import settings
from .models import About, CategoryName,portfolio,Services

# Create your views here.
def contact(request):
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    message = request.POST.get('message', '')
    if name and email and message:
        try:
            send_mail(name, email, message, ['rahul.ajano@yahoo.com'])
        except BadHeaderError:
            return render(request, 'contact.html')

        return redirect("/")


    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return render(request, 'contact.html')




def index(request):
    port = portfolio.objects.all()
    about = About.objects.all()
    serve = Services.objects.all()

    context = {
    'port':port,
    'about':about,
    'serve':serve,
    }

    return render(request, 'index.html',context)
