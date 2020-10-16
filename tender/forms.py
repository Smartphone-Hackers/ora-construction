from django import forms
from masters.models import DepartmentModel, CompanyModel, CustomerModel, DepartmentModel, WorkCategoryModel
from tender import models

class DateInput(forms.DateInput):
    input_type = "date"

class TenderSearchForm(forms.Form):
    project_code = forms.CharField(max_length=50, required=False, widget=forms.TextInput(
                    attrs={"class": "form-control", "placeholder": "Enter Project Code"}))
    project_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(
                    attrs={"class": "form-control", "placeholder": "Enter Project Name"}))
    department_name = forms.ModelChoiceField(empty_label="------", queryset=DepartmentModel.objects.all(), 
            widget=forms.Select(attrs={'class': 'js-example-basic-single w-100'}), required=False)

class TenderDetailsForm(forms.ModelForm):
    class Meta:
        model = models.TenderDetails
        fields = "__all__"

        widgets = {
            "company_name": forms.Select(choices=CompanyModel.objects.all(), attrs={"class": "form-control"}),
            "customer_name": forms.Select(choices=CustomerModel.objects.all(), attrs={"class": "form-control"}),
            "department": forms.Select(choices=DepartmentModel.objects.all(), attrs={"class": "form-control"}),
            "work_category": forms.Select(choices=WorkCategoryModel.objects.all(), attrs={"class": "form-control"}),
            "tender_id": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Tender ID"}),
            "project_title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Project Title"}),
            "project_code": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Proect Code"}),
            "state": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter State"}),
            "city": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter City"}),
            "area": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Area"}),
            "tender_value": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter Tender Value"}),
            "tender_fees": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter Tender Fees"}),
            "tender_bit_value": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter Tender Bit Value"}),
            "EMD_amount_value": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter EMD Amount Value"}),
            "tender_auction_date": DateInput(attrs={"class": "form-control",}),
            "tender_publish_date": DateInput(attrs={"class": "form-control",}),
            "project_description": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Enter Project Description"}),
        }