from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from .models import Port
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
import json
from django.shortcuts import redirect
# Create your views here.
def homepage(request):
    template = get_template('index.html')
    now = datetime.now()
    p = Port.objects.all()
    html = template.render(locals())
    return HttpResponse(html)

def showpage(request,slug):
    template = get_template('port.html')
    try:
        port = Port.objects.get(slug=slug)
        if port != None:
            html = template.render(locals())
            return HttpResponse(html)

    except:
        return redirect('/index')





