from django.views import View
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import ContactForm


class ContactIndexView(View):

    def get(self, request):
        form = ContactForm()
        context = {'form': form}
        return render(request, 'contact-index.html', context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            name = form.cleaned_data.get('name', '')
            email = form.cleaned_data.get('email', '')
            subject = form.cleaned_data.get('subject', '')
            message = form.cleaned_data.get('message', '')

            # Send email to all superusers
            recipient_list = User.objects.filter(
                is_superuser=True).values_list('email', flat=True)

            body = f"Name: {name}\nEmail: {email}\n\n{message}"

            # Sending email
            send_mail(subject, body,
                      settings.EMAIL_HOST_USER, recipient_list)

            # Debugging email
            print("Recipient List:", recipient_list)

            return redirect('contacts:contact')

        context = {'form': form}
        return render(request, 'contact-index.html', context)


class ContactAboutView(View):

    def get(self, request):
        return render(request, 'contact-about.html')
