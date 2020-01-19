from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

worddictionary={}

def count(request):
    data = request.GET['TextBox']
    wordlist = data.split()

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word]=1

    finaldictionary = sorted(worddictionary.items(), key=operator.itemgetter(1) , reverse = True)

    return render(request, 'count.html',{'worddictionary': worddictionary, 'number':len(wordlist),'data':data,'finaldictionary':finaldictionary})

def about(request):
    return render(request, 'about.html') 
