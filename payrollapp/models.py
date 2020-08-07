from django.db import models


class Employees(models.Model):
	date = models.DateTimeField('date published')
    first = models.CharField('First', max_length=20)
    last = models.CharField('Last', max_length=20)
    hourly_rate = models.DecimalField('Hourly Rate', max_digits = 5, decimal_places = 2)
    hours_worked = models.DecimalField('Hours Worked', max_digits = 5, decimal_places = 2)
    gross = models.models.DecimalField('Gross', max_digits = 9, decimal_places = 2)
    ytd_hours = models.DecimalField('YTD Hours', max_digits = 5, decimal_places = 2)
    ytd_gross = models.DecimalField('YTD Gross', max_digits = 9, decimal_places = 2)
    fed_income_tax = models.DecimalField('Fed. Income Tax', max_digits = 9, decimal_places = 2)
    social_security = models.DecimalField('Social Security', max_digits = 9, decimal_places = 2)
    medicare = models.DecimalField('Medicare', max_digits = 9, decimal_places = 2)
    labor_industry= models.DecimalField('L & I', max_digits = 9, decimal_places = 2)
    paid_family_medical_leave = models.DecimalField('PFML', max_digits = 9, decimal_places = 2)



class Taxes(models.Model):
	date = models.DateTimeField('date published')
    gross = models.ForeignKey(Employees, on_delete=models.CASCADE)
    fed_income_tax = models.DecimalField('Fed. Income Tax', max_digits = 9, decimal_places = 2)
    social_security = models.DecimalField('Social Security', max_digits = 9, decimal_places = 2)
    medicare = models.DecimalField('Medicare', max_digits = 9, decimal_places = 2)
    labor_industry= models.DecimalField('L & I', max_digits = 9, decimal_places = 2)
    paid_family_medical_leave = models.DecimalField('PFML', max_digits = 9, decimal_places = 2)
	futa_tax = models.DecimalField('FUTA', max_digits = 9, decimal_places = 2)
    suta_tax = models.DecimalField('SUTA', max_digits = 9, decimal_places = 2)
    