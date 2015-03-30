#__author__ = 'yangliu'
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template import RequestContext
from django.http import HttpResponseRedirect


def contact(request):
    error = []

    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            error.append('subject is empty')
        elif not request.POST.get('email', ''):
            error.append("email is empty")
        elif not request.POST.get('content', ''):
            error.append('textarea is empty')

        if not error:
            send_mail(request.POST['subject'],
                      request.POST['content'],
                      request.POST['email'],
                      ['497384230@qq.com'])

            return HttpResponseRedirect('/contact/thanks')

    return render_to_response('contact.html', {'errors': error, 'subject': request.POST.get('subject', ''),
                                               'email': request.POST.get('email', ''),
                                               'textarea': request.POST.get('content', ''),
                                               }, context_instance=RequestContext(request))


def thank(request):
    return render_to_response('thanks.html')