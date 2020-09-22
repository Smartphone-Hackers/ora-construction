from django import forms
from masters import models

class CompanyForm(forms.ModelForm):
    class Meta:
        model = models.CompanyModel
        fields = "__all__"
        widgets = {
            "company_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Company name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter E-mail"}),
            "phone_number": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter Phone Number"}),
            "address": forms.Textarea(attrs={"class": "form-control", "rows": "5", "placeholder": "Enter Address.."})
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.CustomerModel
        fields = "__all__"
        widgets = {
            "customer_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Customer name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter E-mail"}),
            "phone_number": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter Phone Number"}),
            "address": forms.Textarea(attrs={"class": "form-control", "rows": "5", "placeholder": "Enter Address.."})
        }

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = models.DepartmentModel
        fields = "__all__"
        widgets = {
            "department": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Department name"}),
            }

class WorkCategoryForm(forms.ModelForm):
    class Meta:
        model = models.WorkCategoryModel
        fields = "__all__"
        widgets = {
            "category": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Work Category"}),
            }

class WorkRoleForm(forms.ModelForm):
    class Meta:
        model = models.WorkRoleModel
        fields = "__all__"
        widgets = {
            "workrole": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Work Role"}),
            }

class WorkSpecializationForm(forms.ModelForm):
    class Meta:
        model = models.WorkSpecializationModel
        fields = "__all__"
        widgets = {
            "workspecialization": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Work Role"}),
            }

workroles = models.WorkRoleModel.objects.all()
workspecialization = models.WorkSpecializationModel.objects.all() 

class WorkNameForm(forms.ModelForm):
    class Meta:
        model = models.WorkNameModel
        fields = "__all__"
        widgets = {
            "workname": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Work Role"}),
            "workrole": forms.Select(choices=workroles, attrs={
                "class": "form-control",
            }),
            "workspecialization": forms.Select(choices=workspecialization, attrs={
                "class": "form-control",
            })
            }