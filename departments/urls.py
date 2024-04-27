from departments import views
from django.urls import path

urlpatterns = [
    path('', views.DepartmentLists, name='departmentlists'),
    # path('create', views.CustomerCreate, name='customercreate'),
    # path('customer/<int:pk>/',views.CustomerView, name='customerview'),
    # path('customer/<int:pk>/edit',views.CustomerEdit, name='customeredit'),
    # path('jsontoexcel', views.JsontoExcel, name='jsontoexcel'),
]