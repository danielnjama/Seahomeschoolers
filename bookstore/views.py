from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def privacy_policy(request):
    return render(request,'privacy-policy.html')



def contacts(request):
    return render(request,'contacts.html')


def store(request):
    return render(request,'store.html')


def bookinfo(request):
    return render(request,'bookinfo.html')



def homeschooling(request):
    return render(request,'homeschooling.html')


def conference(request):
    return render(request,'conference.html')