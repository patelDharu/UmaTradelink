from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

# About Us
def who_we_are(request):
    return render(request, 'pages/who_we_are.html')

def our_journey(request):
    return render(request, 'pages/our_journey.html')

def management_speak(request):
    return render(request, 'pages/management_speak.html')

def mission(request):
    return render(request, 'pages/mission.html')

def csr(request):
    return render(request, 'pages/csr.html')

# Strength
def reach(request):
    return render(request, 'pages/reach.html')

def industries(request):
    return render(request, 'pages/industries.html')

# Services
def sales_marketing(request):
    return render(request, 'pages/sales_marketing.html')

def cargo_consolidation(request):
    return render(request, 'pages/cargo_consolidation.html')

def logistics(request):
    return render(request, 'pages/logistics.html')

def sourcing(request):
    return render(request, 'pages/sourcing.html')

# Career & Contact
def career(request):
    return render(request, 'pages/career.html')

def contact(request):
    return render(request, 'pages/contact.html')
