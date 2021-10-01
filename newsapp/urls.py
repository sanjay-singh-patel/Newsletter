from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = "newsletter-index"),
    path('mail/',views.mail_letter,name="mail-letter")
]