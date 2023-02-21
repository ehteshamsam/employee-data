from django.http import HttpResponse
from django.shortcuts import render
import faker
fake = faker.Faker()
from .models import EmployeData

def employedataView(request):
    for i in range(100):
        EmployeData(
        first_name = fake.first_name(),
        last_name = fake.last_name(),
        email = fake.email(),
        sallary = fake.random_element(elements=(10000,20000,30000,40000)),
        company = fake.random_element(elements = ('TCS', 'WIPRO', 'INFOSYS', 'HCL')),
        location = fake.random_element(elements= ('Hydrabad', 'Banglore', 'Chennai', 'Pune')),
        address = fake.address()
        ).save()
    return HttpResponse("Data Saved")

def fetchingalldata(request):
    employes = EmployeData.objects.all()   #['---','---','----'.....'----']
    return render(request, 'employealldata.html',{'data':employes})


def mainpage(request):
    return render(request,'mainpage.html')

def hydrabaddata(request):
    if request.method == 'GET':
       hydData = EmployeData.objects.filter(location='Hydrabad')
       return render(request,'hydData.html',{'data':hydData})
    else:
       company = request.POST.get('company')
       hydData = EmployeData.objects.filter(location='Hydrabad') & EmployeData.objects.filter(company=company)
       return render(request,'hydData.html',{'data':hydData})


def bangloredata(request):
    if request.method == 'GET':
       bangData = EmployeData.objects.filter(location='Banglore')
       return render(request,'bangData.html',{'data':bangData})
    else:
       company = request.POST.get('company')
       bangData = EmployeData.objects.filter(location='Banglore') & EmployeData.objects.filter(company=company)
       return render(request,'bangData.html',{'data':bangData})


def chennaidata(request):
    if request.method == 'GET':
       cheData = EmployeData.objects.filter(location='Chennai')
       return render(request,'cheData.html',{'data':cheData})
    else:
       company = request.POST.get('company')
       cheData = EmployeData.objects.filter(location='Chennai') & EmployeData.objects.filter(company=company)
       return render(request,'cheData.html',{'data':cheData})


def punedata(request):
    if request.method == 'GET':
       puneData = EmployeData.objects.filter(location='Pune')
       return render(request,'puneData.html',{'data':puneData})
    else:
       company = request.POST.get('company')
       puneData = EmployeData.objects.filter(location='Pune') & EmployeData.objects.filter(company=company)
       return render(request,'puneData.html',{'data':puneData})
