from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def analysis(request):
    text = request.POST.get('Text', 'default')
    rp = request.POST.get('removepac', 'off')
    fc = request.POST.get('fullcaps', 'off')
    nl = request.POST.get('newline', 'off')
    sr = request.POST.get('spaceremove', 'off')
    cc = request.POST.get('cc', 'off')
    analyed = ''
    pantuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if rp=="on":
        for x in text:
            if x not in pantuation:
                if x ==" " or x=="\n":
                    analyed +=x
                else:
                    analyed +=x

        params = {'purpose': text, 'analysis_text': analyed}
        text = analyed

    if fc=="on":
        for x in text:
            analyed += x.upper()
        params = {'purpose': text, 'analysis_text': analyed}
        text = analyed

    if nl=="on":
        analyed = ''
        for x in text:
            if x !="\n" and x!="\r":
                analyed += x
        params = {'purpose': text, 'analysis_text': analyed}
        text = analyed

    if sr=="on":
        analyed = ''
        for x in text:
            if x !=" ":
                analyed += x
        params = {'purpose': text, 'analysis_text': analyed}
        text = analyed

    if cc=="on":
        l = {}
        for x in text:
            if x!=" ":
                t = text.count(x)
                l[x] = t
        analyed = l
        params = {'purpose': text, 'analysis_text': analyed}
    if cc != "on" and nl!="on" and fc!="on" and rp!="on":
        return HttpResponse('<h1>NOT SELECTED</h1>')

    return render(request, 'analysis.html', params)
