# I have create this file
from django.http import HttpResponse
from django.shortcuts import render
"""def index(request):
    #return HttpResponse("hellobhai")
    return render(request,'index.html')

def about(request):
    return HttpResponse(" about hellobhai")

def navigation(request):
    s = '''<h2>Navigation Bar<br></h2>
                <a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django with Harry Bhai</a><br> 
                <a href="https://www.facebook.com/">Facebook</a><br>
                <a href="https://www.flipkart.com/">Flipkart</a><br>
                <a href="https://www.hindustantimes.com">News</a><br>
                <a href="https://www.google.com/">Google</a>'''
    return HttpResponse(s)"""

def index(request):
    #return HttpResponse("hello")
    return render(request,'index.html')

def analyze(request):
    djtext=request.GET.get('text','default')
    print(djtext)
    removepunc=request.GET.get('removepunc','off')
    uppercase=request.GET.get('uppercase','off')
    newlineremover=request.GET.get('newlineremover','off')
    charcount=request.GET.get('charcount','off')
    print(removepunc)
    print(uppercase)
    print(newlineremover)
    print(charcount)
    if removepunc=="on":
        punctuations = '''/[-[\]{}()*+?.;,\\^$|#\]/g,"\\$&"'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={'purpose':'Removed punctuations','analyzed_text':analyzed}
        djtext = analyzed
    #return render(request,'analyze.html',params)
    if uppercase=="on":
        analyzed=''
        for char in djtext:
            analyzed = analyzed +char.upper()
        params = {'purpose': 'Lower to Upper', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if newlineremover=="on":
        analyzed=''
        for char in djtext:
            analyzed = analyzed +char
        params = {'purpose': 'newlineremover', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if charcount=="on":
        analyzed=0
        for char in djtext:
            analyzed= analyzed+len(char)
        params={'purpose':'charcount','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)

    return render(request, 'analyze.html', params)



"""def capfirst(request):
    return HttpResponse("capitalizefirst <a href='/'>back</a>")

def newlineremove(request):
    return HttpResponse("newlineremove <a href='/'>back</a>")

def spaceremove(request):
    return HttpResponse("space remover <a href='/'>back</a>")

def charcount(request):
    return HttpResponse("charcount <a href='/'>back</a>")"""

