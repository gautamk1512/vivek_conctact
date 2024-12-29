from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, default='0000000000')  # Set default value

    def __str__(self):
        return self.name
