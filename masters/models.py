from django.db import models

# Create your models here.
class CompanyModel(models.Model):
    company_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    address = models.TextField()

class CustomerModel(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    address = models.TextField()

class DepartmentModel(models.Model):
    department = models.CharField(max_length=100)

class WorkCategoryModel(models.Model):
    category = models.CharField(max_length=100)

class WorkRoleModel(models.Model):
    workrole = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.workrole}'

class WorkSpecializationModel(models.Model):
    workspecialization = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.workspecialization}'

class WorkNameModel(models.Model):
    workname = models.CharField(max_length=100)
    workrole = models.ForeignKey(WorkRoleModel, on_delete=models.CASCADE)
    workspecialization = models.ForeignKey(WorkSpecializationModel, on_delete=models.CASCADE)
