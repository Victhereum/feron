from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Enquiry
from queue import PriorityQueue as q

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", 'last_name', 'phone_no', "email",)}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    "phone_no_vefified",
                    "email_verified",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["first_name", 'last_name',
                    "phone_no", 'phone_no_verified', 'email_verified']
    search_fields = ["first_name", 'phone_no', 'email']


admin.site.register(Enquiry)
