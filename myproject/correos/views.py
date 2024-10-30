from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

# Create your views here.

def contact(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name = name
        contact.last_name = last_name
        contact.email = email
        contact.subject = subject
        contact.save()

        messages.success(request, "Tu mensaje fue enviado correctamente, pronto nos pondremos en contacto contigo. Gracias.")
        return redirect('home')
    return render(request, 'correos/contact.html')
