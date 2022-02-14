from django.contrib import admin

from .models import Vehicle


class ClientAdmin(admin.ModelAdmin):
    model = Vehicle


admin.site.register(Vehicle, ClientAdmin)
