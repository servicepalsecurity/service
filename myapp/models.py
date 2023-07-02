from django.db import models

class User(models.Model):
    email = models.EmailField()
    current_password = models.CharField(max_length=128, default="")
    new_password = models.CharField(max_length=128, default="")

    def __str__(self):
        return self.email