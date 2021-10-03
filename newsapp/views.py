from django.shortcuts import render,redirect
from .forms import SubscriberForm, MailMessageForm
from django.contrib import messages

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success, you are now a part of our mailing list.')
            return redirect('/')
    else:
        form =  SubscriberForm()
    context = {
        'form':form,
    }
    return render(request,'letter/index.html',context)


def mail_letter(request):
    if request.method == 'POST':    
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Mail has been sent')
            return redirect('mail-letter')
    else:
        form = MailMessageForm()
    context = {
        'form':form,
    }
    return render(request,'letter/mail_letter.html',context)

