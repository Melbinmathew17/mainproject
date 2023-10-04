from django.urls import path
from webapp import views

urlpatterns=[
    path('homepage/', views.homepage, name="homepage"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('servicepage/', views.servicepage, name="servicepage"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('appoinmentpage/', views.appoinmentpage, name="appoinmentpage"),
    path('department_page/', views.department_page, name="department_page"),
    path('doctorspage/<catg>', views.doctorspage, name="doctorspage"),
    path('singledoctor/<int:dataid>/', views.singledoctor, name="singledoctor"),
    path('appoinmentsave/', views.appoinmentsave, name="appoinmentsave"),
    path('messagesave/', views.messagesave, name="messagesave"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('userregister/', views.userregister, name="userregister"),
    path('userloginn/', views.userloginn, name="userloginn"),
    path('userlogout/', views.userlogout, name="userlogout"),
    ]