from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

class CustomUserAdmin(UserAdmin):
    readonly_fields = (
        "date_joined",
        "last_login",
         )
       
    fieldsets=(
        (
            "Credentials",
            {
                "fields":("username","password"),
            }
        ),
        ("Personal Infos",
         {
             "fields":("birthdate","bio")
         }
         ),
        
        ("Permissions",
         {
             "fields":( "is_superuser","is_active", "is_staff"," is_critic",)
         }
        ),
          (
            "Important Dates",
            {
                "fields": (
                    "date_joined",
                    "last_login",
                )
            },
        ),
    )
admin.site.register(User,CustomUserAdmin)
    