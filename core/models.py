from django.db import models
from django.utils import timezone

# Create your models here.
class Xodim(models.Model):
    name = models.CharField()
    age = models.IntegerField()
    position = models.CharField()
    salary = models.DecimalField(max_digits=7, decimal_places=2)
    join_date = models.DateField(default=timezone.now(), blank=True)
    city = models.CharField()
    department = models.CharField(choices=[
        ('IT', 'IT Department'),
        ('HR', 'HR Department'),
        ('Stuudy', 'Study Department'),
        ('Sales', 'Sales Deparment')
    ])

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = "Xodim"
        verbose_name_plural = "Xodimlar"