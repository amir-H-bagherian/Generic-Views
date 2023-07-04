from django.db import models
from django.urls import reverse_lazy

# Create your models here.
class Student(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    
    class Meta:
        verbose_name_plural = 'students'
        
    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name
    def get_absolute_url(self):
        return reverse_lazy("detail", kwargs={"my_slug": self.first_name})
    