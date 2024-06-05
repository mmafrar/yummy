from django.views import View
from django.conf import settings
from django.core.mail import EmailMessage, get_connection
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

            subject = form.cleaned_data.get('subject', '')
            message_body = form.cleaned_data.get('message', '')
            name = form.cleaned_data.get('name', '')
            sender_email = form.cleaned_data.get('email', '')
            email_from = settings.YAHOO_EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_HOST_USER]

            message = f"Name: {name}\nEmail: {sender_email}\n\n{message_body}"

            # Configure the connection for Yahoo
            connection = get_connection(
                host=settings.YAHOO_EMAIL_HOST,
                port=settings.YAHOO_EMAIL_PORT,
                username=settings.YAHOO_EMAIL_HOST_USER,
                password=settings.YAHOO_EMAIL_HOST_PASSWORD,
                use_tls=settings.YAHOO_EMAIL_USE_TLS
            )

            # Sending email
            email = EmailMessage(
                subject, message, email_from, recipient_list, connection=connection
            )
            email.send()

            # Debugging email
            print("Email From:", email_from)
            print("Recipient List:", recipient_list)

            return redirect('contacts:contact')

        context = {'form': form}
        return render(request, 'contact-index.html', context)


class ContactAboutView(View):

    def get(self, request):
        return render(request, 'contact-about.html')
