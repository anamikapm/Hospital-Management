from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')


def doctors(request):
    person={'Name':'Dr. Preethy MS',
    'Dept':'Physician',
    'Name2':'Dr.Veena',
    'Dept2' : 'Gynecology'}
    return render(request,'doctors.html',person)
def main(request):
    return render(request,'main.html')
def contacts(request):
    return render(request,'contacts.html')
