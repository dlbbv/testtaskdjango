from django.db import models


class Employee(models.Model):
    branch = models.CharField(max_length=255)
    employee = models.CharField(max_length=255)
    accrued = models.FloatField()
    deductions = models.FloatField()
    tax = models.FloatField()
    calculated = models.IntegerField()
    withheld = models.IntegerField()

    def __str__(self):
        return self.employee