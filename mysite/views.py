from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunccc','off')
    capalize=request.POST.get('capson','off')
    countchar=request.POST.get('countch','off')
    vowelss=request.POST.get('vowelsss','off')
# ------------------------------------------------------------------------
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyzed.html', params)
# ---------------------------------------------------------------------------------
    if(capalize=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Changed To UpperCase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyzed.html', params)
            
# -----------------------------------------------------------------------------------    
    if(countchar=="on"):
        analyzedd=0
        for char in djtext:
            analyzedd=len(djtext)
        params = {'purpose': 'Here is Your Total Character ', 'analyzed_text': analyzedd}
        
        # return render(request, 'analyzed.html', params)
#--------------------------------------------------------------------------------------       
    if(vowelss=="on"):
        analyzed1=0
        for char in djtext:
            if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A' or char=='E' or char=='I' or char=='O' or char=='U'):
                analyzed1=analyzed1+1
        params = {'purpose': 'Counting the vowels', 'analyzed_text': analyzed1}
        
#--------------------------------------------------------------------------------------
    if(removepunc != "on" and capalize!="on" and countchar!="on" and vowelss!='on'):
        return HttpResponse('''Select Some Toggle Keys😋 <br><br><br> <a href='/'>Back</a></button>''')
    if(countchar=='on' and vowelss=='on'):
        params = {'purpose': 'Counting the Charactrs & vowels','analyzed_text':analyzedd, 'analyzed_textt': analyzed1}
    if(removepunc=='on' and vowelss=='on'):
        params = {'purpose': 'Removed Punctuations and counted vowels','analyzed_text':analyzed, 'analyzed_textt': analyzed1}
    if(capalize=='on' and countchar=='on'):
        params = {'purpose': 'UpperCase and counted characters','analyzed_text':analyzed, 'analyzed_textt': analyzedd}
    if(capalize=='on' and vowelss=='on'):
        params = {'purpose': 'UpperCase and vowels ','analyzed_text':analyzed, 'analyzed_textt': analyzed1}
    if(capalize=='on' and vowelss=='on' and countchar=='on'):
        params = {'purpose': 'UpperCase && vowels && characters','analyzed_text':analyzed, 'analyzed_textt': analyzed1,'analyzed_texttt': analyzedd}
    
    return render(request, 'analyzed.html', params)
    