from django.db import models


class Employees(models.Model):
	date = models.DateTimeField('date published')
    first = models.CharField('First', max_length=20)
    last = models.CharField('Last', max_length=20)
    hourly_rate = models.DecimalField( max_digits = 5, decimal_places = 2)
    hours_worked = models.DecimalField( max_digits = 5, decimal_places = 2)
    gross = models.models.DecimalField( max_digits = 9, decimal_places = 2)
    ytd_hours = models.DecimalField( max_digits = 5, decimal_places = 2)
    ytd_gross = models.DecimalField( max_digits = 9, decimal_places = 2)
    fed_income_tax = models.DecimalField( max_digits = 9, decimal_places = 2)
    social_security = models.DecimalField( max_digits = 9, decimal_places = 2)
    medicare = models.DecimalField( max_digits = 9, decimal_places = 2)
    labor_industry= models.DecimalField( max_digits = 9, decimal_places = 2)
    paid_family_medical_leave = models.DecimalField( max_digits = 9, decimal_places = 2)



class Taxes(models.Model):
	date = models.DateTimeField('date published')
    gross = models.ForeignKey(Employees, on_delete=models.CASCADE)
    fed_income_tax = models.DecimalField( max_digits = 9, decimal_places = 2)
    social_security = models.DecimalField( max_digits = 9, decimal_places = 2)
    medicare = models.DecimalField( max_digits = 9, decimal_places = 2)
    labor_industry= models.DecimalField( max_digits = 9, decimal_places = 2)
    paid_family_medical_leave = models.DecimalField( max_digits = 9, decimal_places = 2)
    futa_tax = models.DecimalField( max_digits = 9, decimal_places = 2)
    sui_tax = models.DecimalField( max_digits = 9, decimal_places = 2)
    