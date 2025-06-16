from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name= models.CharField(max_length=60)
    last_name=models.CharField(max_length=60)
    phone=models.CharField(max_length=15)
    email=models.CharField(max_length=80)
    address=models.CharField(max_length=180)
    city=models.CharField(max_length=60)
    state=models.CharField(max_length=40)
    zipcode=models.CharField(max_length=15)

    def __self__(self):
        return(f"{self.first_name} {self.last_name}")
    