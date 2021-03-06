#__author__ = 'yangliu'
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template import RequestContext
from django.http import HttpResponseRedirect
from contact.form import ContactForms


def contact(request):
    if request.method == 'POST':
        form = ContactForms(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            send_mail(data['subject'],
                      data['content'],
                      data['email'],
                      ['lj_6262@163.com'])

            return HttpResponseRedirect('/contact/thanks')
    else:
        form = ContactForms(initial={'subject': 'this is a inital status'})

    return render_to_response('contact.html', {'form': form}, context_instance=RequestContext(request))


def thank(request):
    return render_to_response('thanks.html')