from django.shortcuts import render
from .forms import SubscriberForm

# Create your views here.


def index(request):
    form = SubscriberForm()
    context = {
        'form':form,
    }
    return render(request,'letter/index.html',context)


def mail_letter(request):
    context = {

    }
    return render(request,'letter/mail_letter.html',context)

