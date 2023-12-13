from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(UserSessionIds)
class UserSessionIdAdmin(admin.ModelAdmin):
    list_display = ('id', 'session_id')

# @admin.register(StockDetail)
admin.site.register(StockDetail)