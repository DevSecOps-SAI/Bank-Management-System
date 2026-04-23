 
from django.contrib import admin
from .models import Donor, BloodDonate

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ['user', 'bloodgroup', 'mobile']
    search_fields = ['user__username', 'mobile']
    list_filter = ['bloodgroup']

@admin.register(BloodDonate)
class BloodDonateAdmin(admin.ModelAdmin):
    list_display = ['donor', 'bloodgroup', 'unit', 'status', 'date']
    list_filter = ['status', 'bloodgroup']
    search_fields = ['donor__user__username']

