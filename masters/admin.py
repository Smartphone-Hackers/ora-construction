from django.contrib import admin
from masters import models

# Register your models here.
class ShowCompanyModel(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'phone_number', 'address')

class ShowWorkRoleModel(admin.ModelAdmin):
    list_display = ('workrole',)

class ShowWorkCategoryModel(admin.ModelAdmin):
    list_display = ('category',)

class ShowWorkSpecializationModel(admin.ModelAdmin):
    list_display = ('workspecialization',)

class ShowWorkNameModel(admin.ModelAdmin):
    list_display = ('workname', 'workrole', 'workspecialization')

admin.site.register(models.CompanyModel, ShowCompanyModel)
admin.site.register(models.WorkRoleModel, ShowWorkRoleModel)
admin.site.register(models.WorkCategoryModel, ShowWorkCategoryModel)
admin.site.register(models.WorkSpecializationModel, ShowWorkSpecializationModel)
admin.site.register(models.WorkNameModel, ShowWorkNameModel)