from django.contrib import admin

# Register your models here.
from .models import employee
#admin.site.register(employee)

class EmployeeAdmin(admin.ModelAdmin):
	#fields=(('name','address'))
	list_display=('name','address')
	ordering=('name',)
	search_fields = ('name','address')
admin.site.register(employee,EmployeeAdmin)



