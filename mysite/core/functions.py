from mailqueue.models import MailerMessage 
from django.conf import settings


def send_email(to_address,subject,content,bcc_address=settings.DEFAULT_BCC_EMAIL,attachment=None,attachment2=None,attachment3=None):
    new_message = MailerMessage()
    new_message.subject = subject
    new_message.to_address = to_address
    if bcc_address:
        new_message.bcc_address = bcc_address
    new_message.from_address = settings.DEFAULT_FROM_EMAIL
    new_message.content = content
    if attachment:
        new_message.add_attachment(attachment)
    if attachment2:
        new_message.add_attachment(attachment2)
    if attachment3:
        new_message.add_attachment(attachment3)
    new_message.app = "default"
    new_message.save()