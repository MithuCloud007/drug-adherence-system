from django.shortcuts import render

def doctorpanel(request):
    return render(request, 'doctorPanel/docpanel.html')