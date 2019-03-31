import sendgrid
from flask import current_app, flash
from sendgrid.helpers.mail import *



def send_email(_from, to, subject, content, **kwargs):
    sg = sendgrid.SendGridAPIClient(apikey=current_app.config['SENDGRID_API_KEY'])
    from_email = Email(_from)
    to_email = Email(to)
    subject = subject
    content = Content("text/plain", content)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    # print(type(response.status_code))
    if response.status_code == 202:
        flash('Message sent successfully')
