from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def hello(request):
    t = get_template('hello.html')
    html = t.render(Context())

    return HttpResponse(html)