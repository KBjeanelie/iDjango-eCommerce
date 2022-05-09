
from django.db import models


# Create your models here.
class Contact(models.Model):
    sender_name = models.CharField(max_length=60)
    sender_email = models.EmailField(max_length=100)
    sender_subject = models.CharField(max_length=60)
    sender_message = models.TextField()

    def __str__(self):
        return "message from" + str(self.sender_name)

