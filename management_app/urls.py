from django.urls import path

from management_app import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login/', views.login_view,name='login'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('worker_register',views.worker_register,name='worker_register'),
    path('worker_home/', views.worker_home, name='worker_home'),
    path('customer_home', views.customer_home, name='customer_home'),
    path('customer_register',views.customer_register,name='customer_register'),
    path('worker_view/',views.worker_view,name='worker_view'),
    path('customer_view/', views.customer_view, name='customer_view'),
    path('complaint_add/',views.complaint_add,name='complaint_add'),
    path('complaint_view/',views.complaint_view,name='complaint_view'),
    path('notification_add/', views.notification_add, name='notification_add'),
    path('notification_view/', views.notification_view, name='notification_view'),
    path('delete_worker/<int:id>/',views.delete_worker,name='delete_worker'),
    path('delete_customer/<int:id>/',views.delete_customer,name='delete_customer'),
    path('update_worker/<int:id>/',views.update_worker,name='update_worker'),
    path('update_customer/<int:id>/',views.update_customer,name='update_customer'),
]

