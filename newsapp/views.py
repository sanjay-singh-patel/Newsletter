from django.shortcuts import render,redirect
from .forms import SubscriberForm, MailMessageForm
from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame
from .models import Subscribers
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
        emails = Subscribers.objects.all()
        df = read_frame(emails, fieldnames = ['email'])
        mail_list = df['email'].values.tolist()
        print(mail_list)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            send_mail(title, message,'',mail_list,fail_silently=False)
            messages.success(request,'Mail has been sent')
            return redirect('mail-letter')
    else:
        form = MailMessageForm()
    context = {
        'form':form,
    }
    return render(request,'letter/mail_letter.html',context)

