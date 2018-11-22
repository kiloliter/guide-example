# -*- coding: utf-8 -*-
#some difference
from __future__ import unicode_literals

from django.shortcuts import render

from news.models import Guide
from django.shortcuts import redirect

def index(request):
    if ('page1' in request.POST):
        pages = request.POST['page1']
        for i in range(2, 100):
            if ('page' + str(i) in request.POST):
                pages += "NEXT" + request.POST['page' + str(i)]
            else:
                break
        newGuide = Guide()
        newGuide.text = pages
        newGuide.save()
        return redirect('/' + str(newGuide.pk))
    return render(request, 'news/index.html')

def guide(request, guide_id):
    guide_text = Guide.objects.get(pk=guide_id)
    pageTexts = guide_text.text.split("NEXT") 
    pages = []
    for i in range(0, len(pageTexts)):
        newObject = {'text': pageTexts[i],
                'number': i + 1,
            'imageWidth': (i + 1) * 16,
            'imageHeight': (i + 1) * 9
                }
        pages.append(newObject)
    context = {'totalPages': len(pageTexts),
            'pages': pages}
    return render(request, 'news/guide.html', context)
