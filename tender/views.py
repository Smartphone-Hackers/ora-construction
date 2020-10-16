from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import UpdateView, DeleteView
from tender import forms
from django.http import HttpResponse
from django.contrib import messages
from tender import models
from masters.models import DepartmentModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import xlwt

# Create your views here.
tender_excel_data = {}
class TenderDetailsView(View):
    template_name = 'tender-list.html'
    def get(self, request):
        form = forms.TenderSearchForm()
        tender = models.TenderDetails.objects.all()
        
        project_code = request.GET.get('project_code', '')
        project_name = request.GET.get('project_name', '')
        department_name = request.GET.get('department_name', '')

        try:
            dept = DepartmentModel.objects.get(id=department_name)
        except:
            dept = DepartmentModel.objects.last()

        if project_code != '' and project_name != '' and department_name != '':
            tender = tender.filter(project_code__icontains=project_code, project_title__icontains=project_name, department=dept)
        elif project_name != '' and project_code != '':
            tender = tender.filter(project_code__icontains=project_code, project_title__icontains=project_name)
        elif project_code != '' and department_name != '':
            tender = tender.filter(project_code__icontains=project_code, department=dept)
        elif project_name != '' and department_name != '':
            tender = tender.filter(project_title__icontains=project_name, department=dept)
        elif project_name != '':
            tender = tender.filter(project_title__icontains=project_name)
        elif project_code != '':
            tender = tender.filter(project_code__icontains=project_code)
        elif department_name != '':
            tender = tender.filter(department=dept)

        p = Paginator(tender, 2)
        page_num = request.GET.get("page", 1)

        try:
            page = p.page(page_num)
        except PageNotAnInteger:
            page = p.page(1)
        except EmptyPage:
            page = p.page(p.num_pages)
        
        if self.request.path == self.request.get_full_path():
            current_url = self.request.path + '?'
        else:
            if '?page=' in self.request.get_full_path():
                current_url = self.request.get_full_path().split('?page=')[0] + '?'
            else:
                current_url = self.request.get_full_path().split('&page=')[0] + '&'

        tender_excel_data['datas'] = page.object_list
        
        datas = {
            "form": form,
            "tenders": page,
            "current_url": current_url,
        }

        return render(request, template_name=self.template_name, context=datas)

def generate_excel(excel_name, columns, model_object):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="{}.xls"'.format(excel_name)

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('{}'.format(excel_name))

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = columns

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = model_object

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response    

def export_tender_xls(request):
    columns = ['ProjectTitle', 'TenderAuctionDate', 'CompanyName', 'CustomerName', 'Department',
               'WorkCategory', 'TenderID', 'TenderPublishDate', 'Status', 'GovtProjectStartDate',
               'GovtProjectEndDate',]
    model_object = tender_excel_data['datas'].values_list('project_title', 'tender_auction_date',
    'company_name__company_name', 'customer_name__customer_name', 'department__department', 'work_category__category',
    'tender_id', 'tender_publish_date',)
    return generate_excel('TenderList', columns, model_object)

class EditTenderDetail(UpdateView):
    template_name = "new-tender.html"
    model = models.TenderDetails
    form_class = forms.TenderDetailsForm
    success_url = "/tender/tender"
    
class DeleteTenderDetail(View):
    def get(self, request, pk):
        tender = models.TenderDetails.objects.get(id=pk)
        tender.delete()
        messages.info(request, 'Tender Deleted.')
        return redirect("/tender/tender")

class NewTenderView(View):
    template_name = "new-tender.html"
    def get(self, request):
        form = forms.TenderDetailsForm()
        datas = {
            "form": form,
        }
        return render(request, template_name=self.template_name, context=datas)

    def post(self, request):
        tender = forms.TenderDetailsForm(request.POST)
        if tender.is_valid():
            tender.save()
            messages.info(request, "New Tender Added.")
            return redirect('/tender/new-tender')
        return redirect('/tender/new-tender')

class TenderApproval(View):
    template_name = 'tender-approve.html'
    def get(self, request):
        return render(request, template_name=self.template_name)