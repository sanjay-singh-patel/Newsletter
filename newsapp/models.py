from django.db import models

# Create your models here.
class Subscribers(models.Model):
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class MailMessage(models.Model):
    title = models.TextField(max_length=255)
    message = models.TextField(null=True)

    def __str__(self):
        return self.title