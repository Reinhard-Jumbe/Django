from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def pricing(request):
    return render(request,'pricing.html')

def shop(request):
    return render(request,'shop.html')

def services(request):
    return render(request,'services.html')

def AddData(request):
    return render(request,'AddData.html')

def insert_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        image = request.FILES['image']




    return render(request,'AddData.html')