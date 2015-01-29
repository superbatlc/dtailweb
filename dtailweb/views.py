from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template.loader import render_to_string
from django.template import RequestContext


def test(request):
    return render_to_response('test.html', RequestContext(request, {}))