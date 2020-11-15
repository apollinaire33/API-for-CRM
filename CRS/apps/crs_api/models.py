from django.db import models
from django.db.models import F
from django.http import HttpResponseServerError
from django.contrib.postgres.fields import JSONField


class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)
    emp_num = models.IntegerField(default=0)
    adress = models.CharField(max_length=50)
 
    def __str__(self):
        return self.name 

class Employee(models.Model):
    POSITION_CHOICES = (
        ('1', 'general manager'), 
        ('2', 'manager'), 
        ('3', 'department head'), 
        ('4', 'employee'), 
    )
    
    username = models.CharField(max_length=50)
    age = models.IntegerField()
    position = models.CharField(max_length=50, choices = POSITION_CHOICES, default='-') 
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.SET('-'), blank=True, null=True, to_field='name')

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.pk:
            Company.objects.filter(name=self.company_id).update(emp_num=F('emp_num')+1)   
        elif self.pk:
            prev_comp = Employee.objects.get(pk=self.pk)
            Company.objects.filter(name=prev_comp.company_id).update(emp_num=F('emp_num')-1) 
            Company.objects.filter(name=self.company_id).update(emp_num=F('emp_num')+1)  
        super().save(*args, **kwargs) 


class Partnership(models.Model):
    name = models.CharField(max_length=50, unique=True, default='-')
    com_1 = models.ForeignKey(Company, related_name='first_partner', on_delete=models.CASCADE, blank=True, null=True, to_field='name')
    com_1_employees = models.ForeignKey(Company, related_name='first_partner_employees', on_delete=models.CASCADE, blank=True, null=True, to_field='name')
    com_2 = models.ForeignKey(Company, related_name='second_partner', on_delete=models.CASCADE, blank=True, null=True, to_field='name')
    com_2_employees = models.ForeignKey(Company, related_name='second_partner_employees', on_delete=models.CASCADE, blank=True, null=True, to_field='name')

    def __str__(self):
        return self.name
