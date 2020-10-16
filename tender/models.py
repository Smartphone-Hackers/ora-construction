from django.db import models
from masters.models import DepartmentModel
from masters.models import CompanyModel
from masters.models import CustomerModel
from masters.models import WorkCategoryModel

# Create your models here.
class TenderDetails(models.Model):
    company_name = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, related_name='tender')
    customer_name = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)
    work_category = models.ForeignKey(WorkCategoryModel, on_delete=models.CASCADE)
    tender_id = models.CharField(max_length=100)
    project_title = models.CharField(max_length=100)
    project_code = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    tender_value = models.IntegerField()
    tender_fees = models.IntegerField()
    tender_bit_value = models.IntegerField()
    EMD_amount_value = models.IntegerField()
    tender_auction_date = models.DateField()
    tender_publish_date = models.DateField()
    project_description = models.TextField()

