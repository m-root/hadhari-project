from django.shortcuts import render

# Create your views here.

def ml_reporting(request):
    # pass
    return render(request, 'reports/report.html', {})
