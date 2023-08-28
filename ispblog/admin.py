from django.contrib import admin
from .models import services, c_request ,suport
# Register your models here.
@admin.register(services)
class blogpost(admin.ModelAdmin):
    list_display = ('title','price','speed', )

@admin.register(c_request)
class request_for_connection  (admin.ModelAdmin):
    list_display  = ( 'Date','package', 'phone',)