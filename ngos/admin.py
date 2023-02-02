from django.contrib import admin
from .models import School


# Register your models here.

#admin.site.register(School)
@admin.register(School)

class SchoolAdmin(admin.ModelAdmin):
	list_display = ('name', 'address')
	ordering = ('name', ) # comma because it needs to be a tuple, -name will sort in reverse order
	search_fields = ("name", "address")