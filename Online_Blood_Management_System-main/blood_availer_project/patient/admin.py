from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'bloodgroup', 'doctorname', 'mobile']
    search_fields = ['user__username', 'mobile', 'doctorname']
    list_filter = ['bloodgroup']