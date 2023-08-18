from django.db import models

class Member1(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    

    def __str__(self):
        return f"{self.firstname} {self.lastname} "
