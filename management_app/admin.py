
from django.contrib import admin
from management_app import models

admin.site.register(models.Login)
admin.site.register(models.Worker)
admin.site.register(models.Customer)
admin.site.register(models.Notifications)