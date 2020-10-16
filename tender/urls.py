from django.urls import path
from tender import views

urlpatterns = [
    # Tender
    path('tender', views.TenderDetailsView.as_view(), name='tender'),
    path('new-tender', views.NewTenderView.as_view(), name='new-tender'),
    path('tender-excel-report', views.export_tender_xls, name='tender-excel-report'),
    path('edit-tender-detail/<int:pk>', views.EditTenderDetail.as_view(), name='edit-tender-detail'),
    path('delete-tender-detail/<int:pk>', views.DeleteTenderDetail.as_view(), name='delete-tender-detail'),
    # Tender Approval
    path('tender-approval', views.TenderApproval.as_view(), name='tender-approval'),
]