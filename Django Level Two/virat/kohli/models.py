from django.db import models

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=264,unique=True)


    def __str__(self):
        return self.company_name


class Webpage(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)


class Money(models.Model):
    currency = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    money = models.IntegerField()

    def __str__(self):
        return str(self.money)
