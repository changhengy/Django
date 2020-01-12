# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render

def search_form(request):    
    return render_to_response('search_form.html')

def search(request):
    context = {}

    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        # return render(request, 'child.html', context)
        # message = '你搜索的内容为: ' + request.GET['q']
        message = 2
    else:
        message = '你提交了空表单'
    # return HttpResponse(message)
    context ['key_2'] = message
    return render(request, 'child.html', context)