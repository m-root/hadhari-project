from django.contrib import admin
from core.models import Daycare,Image,Category,Service,Location,Contact,Owner,Organisation,Admin

# Register your models here.
admin.site.register([Daycare,Image,Category,Service,Location,Contact,Owner,Organisation,Admin])
