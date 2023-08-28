from django.db import models

# Create your models here.

class services (models.Model):
    title = models.CharField(max_length =200)
    price = models.CharField(max_length= 100)
    speed  =models.CharField(max_length= 100)
    ftp = models.CharField(max_length= 100)
    description = models.TextField(null=True, blank=True)

    class Meta : 
        db_table = "services "
        ordering = ("id",)



class c_request (models.Model):
    Date = models.DateTimeField( auto_now=False, auto_now_add=False)
    package = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50, blank = "True", null = "True")
    
    class Meta : 
        db_table = 'c_request'
        ordering = ("-id",)
        verbose_name_plural = 'connection request'

    def __str__(self):
        return self.phone

class suport (models.Model):
    question = models.CharField(max_length=50,blank = "True", null = "True")
    active_package = models.CharField(max_length=50 ,blank = "True", null = "True")
    phone = models.CharField(max_length=50,blank = "True", null = "True")
    address = models.CharField(max_length=50, blank = "True", null = "True")
    
    class Meta : 
        db_table = 'support'
        ordering = ("-id",)
        verbose_name_plural = 'support request'

    def __str__(self):
        return self.question

