from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    number =models.CharField(max_length=10)
    subject=models.CharField( max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.email
    
class Job_category(models.Model):
    name=models.CharField( max_length=50)
    
    def __str__(self):
        return self.name
    

  
class Post_job(models.Model):
    company_name=models.CharField( max_length=50,default="")
    # job_category=models.ForeignKey(Job_category, on_delete=models.CASCADE)
    experiance=models.CharField(max_length=10,default="")
    qualification=models.CharField( max_length=50,default="")
    location=models.CharField(max_length=50,default="")
    email=models.EmailField( max_length=254,default="")
    website=models.URLField( max_length=200,default="")
    company_logo=models.ImageField(upload_to='company_logo',default="")
    company_address=models.TextField()
    description=models.TextField()
    post_date=models.DateTimeField(blank=True, null=True)
    
    
    
    
    # def __str__(self):
    #     return self.company_name
    
    



    