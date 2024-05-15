from django.shortcuts import render, redirect
from django.views import View
from .form import ContactForm

from django.core.mail import send_mail
from django.conf import settings


class ViewContactView(View):

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            subject = form.cleaned_data.get('subject', '')
            message = form.cleaned_data.get('message', '')
            email_from = settings.NOREPLY_EMAIL
            recipient_list = [settings.EMAIL_HOST_USER]  # Send email to yourself or any other recipient

            # Sending email
            send_mail(subject, message, email_from, recipient_list)

            return redirect('contacts:view-contact')
        context = {'form': form}
        return render(request, 'contact.html', context)

    def get(self, request):
        form = ContactForm()
        context = {'form': form}
        return render(request, 'contact.html', context)


class ViewAbouttView(View):

    def get(self, request):
        return render(request, "about.html")

