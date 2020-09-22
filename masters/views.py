from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import UpdateView, DeleteView
from masters import forms
from masters import models
from django.contrib import messages

# Create your views here.
class Dashboard(View):
    template_name = 'index.html'
    def get(self, request):
        return render(request, template_name=self.template_name)

class Company(View):
    template_name = "company.html"
    def get(self, request):
        company = models.CompanyModel.objects.all()
        datas = {
            "company": company
        }
        return render(request, template_name=self.template_name, context=datas)

class AddCompany(View):
    template_name = "add-company.html"
    def get(self, request):
        form = forms.CompanyForm()
        datas = {
            "form": form,
        }
        return render(request, template_name=self.template_name, context=datas)
    
    def post(self, request):
        company = forms.CompanyForm(request.POST)
        if company.is_valid():
            company.save()
        return redirect('/masters/company')

class EditCompany(UpdateView):
    template_name = "add-company.html"
    model = models.CompanyModel
    form_class = forms.CompanyForm
    success_url = "/masters/company"
    
class DeleteCompany(View):
    def get(self, request, pk):
        company = models.CompanyModel.objects.get(id=pk)
        company.delete()
        messages.info(request, 'Company Deleted.')
        return redirect("/masters/company")

class Customer(View):
    template_name = "customer.html"
    def get(self, request):
        customer = models.CustomerModel.objects.all()
        datas = {
            "customers": customer,
        }
        return render(request, template_name=self.template_name, context=datas)

class AddCustomer(View):
    template_name = "add-customer.html"
    def get(self, request):
        form = forms.CustomerForm()
        datas = {
            "form": form,
        }
        return render(request, template_name=self.template_name, context=datas)
    
    def post(self, request):
        customer = forms.CustomerForm(request.POST)
        if customer.is_valid():
            customer.save()
        return redirect('/masters/customer')

class EditCustomer(UpdateView):
    template_name = "add-customer.html"
    model = models.CustomerModel
    form_class = forms.CustomerForm
    success_url = "/masters/customer"
    
class DeleteCustomer(View):
    def get(self, request, pk):
        customer = models.CustomerModel.objects.get(id=pk)
        customer.delete()
        messages.info(request, 'Customer Deleted.')
        return redirect("/masters/customer")

class Department(View):
    template_name = "department.html"
    def get(self, request):
        department = models.DepartmentModel.objects.all()
        datas = {
            "departments": department,
        }
        return render(request, template_name=self.template_name, context=datas)

class AddDepartment(View):
    template_name = "add-department.html"
    def get(self, request):
        form = forms.DepartmentForm()
        datas = {
            "form": form,
        }
        return render(request, template_name=self.template_name, context=datas)
    
    def post(self, request):
        customer = forms.DepartmentForm(request.POST)
        if customer.is_valid():
            customer.save()
        return redirect('/masters/department')

class EditDepartment(UpdateView):
    template_name = "add-department.html"
    model = models.DepartmentModel
    form_class = forms.DepartmentForm
    success_url = "/masters/department"
    
class DeleteDepartment(View):
    def get(self, request, pk):
        customer = models.DepartmentModel.objects.get(id=pk)
        customer.delete()
        messages.info(request, 'Department Deleted.')
        return redirect("/masters/department")

class WorkCategory(View):
    template_name = "work-category.html"
    def get(self, request):
        workcategory = models.WorkCategoryModel.objects.all()
        datas = {
            "workcategory": workcategory,
        }
        return render(request, template_name=self.template_name, context=datas)

class AddWorkCategory(View):
    template_name = "add-work-category.html"
    def get(self, request):
        form = forms.WorkCategoryForm()
        datas = {
            "form": form,
        }
        return render(request, template_name=self.template_name, context=datas)
    
    def post(self, request):
        customer = forms.WorkCategoryForm(request.POST)
        if customer.is_valid():
            customer.save()
        return redirect('/masters/work-category')

class EditWorkCategory(UpdateView):
    template_name = "add-work-category.html"
    model = models.WorkCategoryModel
    form_class = forms.WorkCategoryForm
    success_url = "/masters/work-category"
    
class DeleteWorkCategory(View):
    def get(self, request, pk):
        customer = models.WorkCategoryModel.objects.get(id=pk)
        customer.delete()
        messages.info(request, 'Work Category Deleted.')
        return redirect("/masters/work-category")

class WorkRole(View):
    template_name = "work-role.html"
    def get(self, request):
        workrole = models.WorkRoleModel.objects.all()
        datas = {
            "workrole": workrole,
        }
        return render(request, template_name=self.template_name, context=datas)

class AddWorkRole(View):
    template_name = "add-work-role.html"
    def get(self, request):
        form = forms.WorkRoleForm()
        datas = {
            "form": form,
        }
        return render(request, template_name=self.template_name, context=datas)
    
    def post(self, request):
        workrole = forms.WorkRoleForm(request.POST)
        if workrole.is_valid():
            workrole.save()
        return redirect('/masters/work-role')

class EditWorkRole(UpdateView):
    template_name = "add-work-role.html"
    model = models.WorkRoleModel
    form_class = forms.WorkRoleForm
    success_url = "/masters/work-role"
    
class DeleteWorkRole(View):
    def get(self, request, pk):
        customer = models.WorkRoleModel.objects.get(id=pk)
        customer.delete()
        messages.info(request, 'Work Role Deleted.')
        return redirect("/masters/work-role")

class WorkSpecialization(View):
    template_name = "work-specialization.html"
    def get(self, request):
        workspecialization = models.WorkSpecializationModel.objects.all()
        datas = {
            "workspecialization": workspecialization,
        }
        return render(request, template_name=self.template_name, context=datas)

class AddWorkSpecialization(View):
    template_name = "add-work-specialization.html"
    def get(self, request):
        form = forms.WorkSpecializationForm()
        datas = {
            "form": form,
        }
        return render(request, template_name=self.template_name, context=datas)
    
    def post(self, request):
        workspecialization = forms.WorkSpecializationForm(request.POST)
        if workspecialization.is_valid():
            workspecialization.save()
        return redirect('/masters/work-specialization')

class EditWorkSpecialization(UpdateView):
    template_name = "add-work-specialization.html"
    model = models.WorkSpecializationModel
    form_class = forms.WorkSpecializationForm
    success_url = "/masters/work-specialization"
    
class DeleteWorkSpecialization(View):
    def get(self, request, pk):
        customer = models.WorkSpecializationModel.objects.get(id=pk)
        customer.delete()
        messages.info(request, 'Work Specialization Deleted.')
        return redirect("/masters/work-specialization")

class WorkName(View):
    template_name = "work-name.html"
    def get(self, request):
        workname = models.WorkNameModel.objects.all()
        datas = {
            "workname": workname,
        }
        return render(request, template_name=self.template_name, context=datas)

class AddWorkName(View):
    template_name = "add-work-name.html"
    def get(self, request):
        form = forms.WorkNameForm()
        datas = {
            "form": form,
        }
        return render(request, template_name=self.template_name, context=datas)
    
    def post(self, request):
        workname = forms.WorkNameForm(request.POST)
        if workname.is_valid():
            workname.save()
        return redirect('/masters/work-name')

class EditWorkName(UpdateView):
    template_name = "add-work-name.html"
    model = models.WorkNameModel
    form_class = forms.WorkNameForm
    success_url = "/masters/work-name"
    
class DeleteWorkName(View):
    def get(self, request, pk):
        customer = models.WorkNameModel.objects.get(id=pk)
        customer.delete()
        messages.info(request, 'Work Name Deleted.')
        return redirect("/masters/work-name")
