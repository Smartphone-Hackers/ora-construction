from django.urls import path
from masters import views

urlpatterns = [
    #Company
    path('company', views.Company.as_view(), name='company'),
    path('add-company', views.AddCompany.as_view(), name='add-company'),
    path('edit-company/<int:pk>', views.EditCompany.as_view(), name='edit-company'),
    path('delete-company/<int:pk>', views.DeleteCompany.as_view(), name='delete-company'),
    # Customers
    path('customer', views.Customer.as_view(), name='customer'),
    path('add-customer', views.AddCustomer.as_view(), name='add-customer'),
    path('edit-customer/<int:pk>', views.EditCustomer.as_view(), name='edit-customer'),
    path('delete-customer/<int:pk>', views.DeleteCustomer.as_view(), name='delete-customer'),
    # Department
    path('department', views.Department.as_view(), name='department'),
    path('add-department', views.AddDepartment.as_view(), name='add-department'),
    path('edit-department/<int:pk>', views.EditDepartment.as_view(), name='edit-department'),
    path('delete-department/<int:pk>', views.DeleteDepartment.as_view(), name='delete-department'),
    # Work Category
    path('work-category', views.WorkCategory.as_view(), name='work-category'),
    path('add-work-category', views.AddWorkCategory.as_view(), name='add-work-category'),
    path('edit-work-category/<int:pk>', views.EditWorkCategory.as_view(), name='edit-work-category'),
    path('delete-work-category/<int:pk>', views.DeleteWorkCategory.as_view(), name='delete-work-category'),
    # work Role
    path('work-role', views.WorkRole.as_view(), name='work-role'),
    path('add-work-role', views.AddWorkRole.as_view(), name='add-work-role'),
    path('edit-work-role/<int:pk>', views.EditWorkRole.as_view(), name='edit-work-role'),
    path('delete-work-role/<int:pk>', views.DeleteWorkRole.as_view(), name='delete-work-role'),
    # Work Specialization
    path('work-specialization', views.WorkSpecialization.as_view(), name='work-specialization'),
    path('add-work-specialization', views.AddWorkSpecialization.as_view(), name='add-work-specialization'),
    path('edit-work-specialization/<int:pk>', views.EditWorkSpecialization.as_view(), name='edit-work-specialization'),
    path('delete-work-specialization/<int:pk>', views.DeleteWorkSpecialization.as_view(), name='delete-work-specialization'),
    # Work Name
    path('work-name', views.WorkName.as_view(), name='work-name'),
    path('add-work-name', views.AddWorkName.as_view(), name='add-work-name'),
    path('edit-work-name/<int:pk>', views.EditWorkName.as_view(), name='edit-work-name'),
    path('delete-work-name/<int:pk>', views.DeleteWorkName.as_view(), name='delete-work-name'),
]