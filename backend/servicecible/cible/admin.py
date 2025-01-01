from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Client, Notification

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'pseudo', 'password', 'telephone', 'email')

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('not_client_id', 'not_bailleur_id', 'message')

admin.site.register(Client, ClientAdmin)
admin.site.register(Notification, NotificationAdmin)

