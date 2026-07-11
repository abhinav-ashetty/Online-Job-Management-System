import time
from django.core.mail import send_mail
from django.conf import settings

def send_email_to_client():
    subject = f"new job posted: {job.title}"
    message = f"A new job has been posted: {job.type} , {job.descripton}"
    from_email = settings.EMAIL_HOST_USER
    recepient_list = ["xyz@gmail.com"] # here you can add the email addresses of the clients you want to send the email to
    send_mail(subject,message,from_email,recepient_list)
    