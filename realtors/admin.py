from django.contrib import admin
from .models import Realtor
# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display=('id','name', 'phone', 'email', 'is_mvp')
    list_display_links=('id', 'name')
    search_fields=('name',)
    list_per_page=23

admin.site.register(Realtor, RealtorAdmin)
