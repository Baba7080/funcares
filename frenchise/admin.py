from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(frenchise_register_model)
class frenchise_admin(admin.ModelAdmin):
    list_display = ['id','frenchise_name','DOB','gender','city','Pin_code','Work_Type','Address_Type',
    ]


# @admin.register(frenchise_employee_register_model)
# class employee_admin(admin.ModelAdmin):
#     list_display = ['employee_id','employee_name', 'designation'
#     ]
admin.site.register(ProfileFrenchise)
admin.site.register(Revenue)


@admin.register(frenchise_employee_register_model)
class employee_admin(admin.ModelAdmin):
    list_display = ['employee_id','email','username','password']


