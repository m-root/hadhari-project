from django.contrib import admin
from .models import *
# Register your models here.


class BoxGirlAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BoxGirl._meta.fields]

admin.site.register(BoxGirl,BoxGirlAdmin)


class AccountAdmin(admin.ModelAdmin):
    # todo account_profile should return fk model __str__
    list_display = ['email','full_name','account_type','account_profile','is_superuser','is_staff','is_active']
    list_filter = ('account_type',)

admin.site.register(Account,AccountAdmin)


class SchoolAdmin(admin.ModelAdmin):
    list_display = [f.name for f in School._meta.fields]

admin.site.register(School,SchoolAdmin)
