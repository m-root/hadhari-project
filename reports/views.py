from django.shortcuts import render
from core.models import Account
# Create your views here.

def ml_reporting(request):
    # pass
    return render(request, 'reports/report.html', {})


def anything(request):
   x =  Account.SUPER_ADMIN