from django.db import models
from django.conf import settings

# Create your models here.

class Task(models.Model):
    
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.TextField(max_length = 255)
    description = models.TextField()
    
    date_start = models.DateField() #start of task
    date_end = models.DateField()   #deadline
    
    def __str__(self):
        return '[' + str(self.id) + '] ' + self.title 

    