from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def customers(request):
    
    return render(request, 'customers.html')
def orders(request):
    
    return render(request, 'orders.html')
def analytics(request):
    return render(request, 'analytics.html')
def messages(request):
    
    return render(request, 'messages.html')
def products(request):
    
    return render(request, 'products.html')
def reports(request):
    
    return render(request, 'reports.html')
def settings(request):
    
    return render(request, 'settings.html')
def addproducts(request):
    
    return render(request, 'addproducts.html')
def login(request):
    
    return render(request, 'login.html')