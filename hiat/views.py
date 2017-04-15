from django.http import HttpResponse
from .models import Job

def sms(request):
    twiml = '<Response><Message>Hello from your Django app!</Message></Response>'
    return HttpResponse(twiml, content_type='text/xml')
