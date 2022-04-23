from django.urls import path

from management_app import views
urlpatterns = [
    path('',views.home,name='home.html'),
    path('login', views.login_view,name='login'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('worker_register',views.worker_register,name='worker_register'),
    path('worker_home/', views.worker_home, name='worker_home'),
    path('customer_home', views.customer_home, name='customer_home'),
    path('customer_register',views.customer_register,name='customer_register'),
    path('worker_view/',views.worker_view,name='worker_view'),
    path('customer_reg_view/',views.customer_view,name='customer_reg_view'),
    path('complaint_add/',views.complaint_add,name='complaint_add'),
    path('complaint_view/',views.complaint_view,name='complaint_view'),
    path('notification_add/', views.notification_add, name='notification_add'),
    path('notification_view/', views.notification_view, name='notification_view'),
    path('update_view/<int:id>/',views.update_view,name='update_view'),
    path('delete_view/<int:id>/',views.delete_view,name='delete_view')
]

