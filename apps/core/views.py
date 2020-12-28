from django.shortcuts import render

# Cre ate your views here.
def frontpage(request):
    return render(request, 'frontpage.html')

def contact(request):
    return render(request, 'contact.html')    