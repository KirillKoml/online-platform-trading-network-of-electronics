from django.contrib import admin

from staff.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """Админка для сотрудников."""
    list_display = ('id', 'email')