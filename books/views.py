from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from books.models import Book


def hello(request):
    t = get_template('hello.html')
    html = t.render(Context())

    return HttpResponse(html)


def display_meta(request):
    values = request.META.items()
    values.sort()

    t = get_template('meta.html')
    html = t.render(Context({'info': values}))

    return HttpResponse(html)


def search_info(request):
    return render_to_response('search.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        books = Book.objects.filter(title__icontains='p')
        q = request.GET['q']

        return render_to_response('search_result.html', {'books': books, 'query': q})
    else:
        return render_to_response('search.html', {'error':True})
