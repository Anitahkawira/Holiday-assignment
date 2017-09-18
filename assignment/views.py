from django.shortcuts import render
from .models import Family

# Create your views here.
def members(request):
    members = Family.objects.all()
    return render(request,'listing_family.html', members)
