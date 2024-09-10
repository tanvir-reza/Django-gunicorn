from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
# import sent mail
from django.core.mail import send_mail
from weasyprint import HTML
from django.core.files.base import ContentFile
# 


# mail send using threading
from threading import Thread

# import pdf from media folder
from .models import MyModel



# Create your views here.
def home(request):
    try:
        subject = 'Hello, World!'
        email_from = settings.DEFAULT_FROM_EMAIL
        email_to = 'dev@tanvirreza.me'
        # import html template from templates folder
        context = {"message": "Hello, World! FROM SMTP2GO"}
        html_content = get_template('email.html').render(context)
        pdf = HTML(string=html_content).write_pdf()
        pdf_name = f"monthly_statement.pdf"
        obj = MyModel.objects.create(user="Tanvir Reza")
        obj.my_pdf.save(pdf_name, ContentFile(pdf), save=True)
        obj.save()

        
        msg = EmailMultiAlternatives(subject, "Text Content", email_from, [email_to])
        msg.attach_alternative(html_content, "text/html")
        msg.attach(obj.my_pdf.name, obj.my_pdf.read(), 'application/pdf')
        Thread(target=msg.send).start()
        return HttpResponse("Email Sent!")
    except Exception as e:
        return HttpResponse(str(e))
    
    # try:
    #     subject = 'Hello, World!'
    #     email_from = settings.DEFAULT_FROM_EMAIL
    #     email_to = 'dev@tanvirreza.me'
    #     text_content = 'This is an important message.'
    #     html_content = '<p>This is an <strong>important</strong> message.</p>'
    #     msg = send_mail(subject, text_content, email_from, [email_to], html_message=html_content)
    #     if msg:
    #         return HttpResponse("Email Sent!222222")
    #     else:
    #         return HttpResponse("Email not Sent!")
    # except Exception as e:
    
        return HttpResponse(str(e))
