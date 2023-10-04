from django.urls import path

from myapp import views

urlpatterns=[
    path('indexpage/', views.indexpage, name="indexpage"),
    path('departmentpage/', views.departmentpage, name="departmentpage"),
    path('savedepartment/', views.savedepartment, name="savedepartment"),
    path('displaydepartment/', views.displaydepartment, name="displaydepartment"),
    path('updatedepartment/<int:dataid>/', views.updatedepartment, name="updatedepartment"),
    path('editdepartment/<int:dataid>/', views.editdepartment, name="editdepartment"),
    path('deletedepartment/<int:dataid>/', views.deletedepartment, name="deletedepartment"),
    path('doctorspage/', views.doctorspage, name="doctorspage"),
    path('savedoctor/', views.savedoctor, name="savedoctor"),
    path('displaydoctors/', views.displaydoctors, name="displaydoctors"),
    path('updatedoctor/<int:dataid>/', views.updatedoctor, name="updatedoctor"),
    path('editdoctor/<int:dataid>/', views.editdoctor, name="editdoctor"),
    path('deletedoctor/<int:dataid>/', views.deletedoctor, name="deletedoctor"),
    path('adminpage/', views.adminpage, name="adminpage"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),
    path('appoinment_page/', views.appoinment_page, name="appoinment_page"),
    path('messagepage/', views.messagepage, name="messagepage"),
    path('service_page/', views.service_page, name="service_page"),
    path('saveservice/', views.saveservice, name="saveservice"),
    path('displayservice/', views.displayservice, name="displayservice"),


]


