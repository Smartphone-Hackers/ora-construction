from django.urls import path
from tender_api import views

urlpatterns = [
    path('tender-json-lists', views.tender_lists, name="tender-json-lists"),
    path('tender-json-list/<str:pk>', views.tender_list, name="tender-json-list"),
]
