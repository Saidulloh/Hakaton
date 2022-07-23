from django.contrib import admin

from apps.users.models import Developer, Client

admin.site.register(Developer)
admin.site.register(Client)