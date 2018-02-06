from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from .models import Port,Product
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


def listing(request):
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset = 'utf-8'>
    <title>手机</title>
    </head>
    <body>
    <h2>以下是手机列表</h2>
    <hr>
    <table>
    {}
    </table>
    </body>
    </html>
    '''

    products = Product.objects.all()
    tags = '<tr><td>产品</td><td>售价</td></tr>'
    for p in products:
        tags = tags + '<tr><td>{}</td>'.format(p.name)
        tags = tags + '<tr><td>{}</td></tr>'.format(p.price)

    return HttpResponse(html.format(tags))


def about(request):
    template = get_template('about.html')
    p = Port.objects.get(id=1)
    html = template.render({'port':p})
    return HttpResponse(html)
