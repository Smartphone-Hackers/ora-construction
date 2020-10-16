from django.db import models

# Create your models here.
class CompanyModel(models.Model):
    company_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    address = models.TextField()
    
    def __str__(self):
        return f'{self.company_name}'
        
class CustomerModel(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return f'{self.name}'
    
    def __repr__(self):
        return """{0}(customer_name={1}, email={2}, phone_number={3}, address={4})""".format(
            self.__class__.__name__, self.customer_name, self.email, self.phone_number, self.address)
        
class DepartmentModel(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.department}'
        
class WorkCategoryModel(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.category}'

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
