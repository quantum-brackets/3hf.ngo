from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    list_display = [
        'email', "first_name", 'last_name', 'is_staff',
    ]

    fieldsets = [
        ("Basic User Details", {
            "fields": ['email', 'first_name', 'last_name', "phone_number", 'password',]
        }),

        (
            "User Status (sensitive area, proceed with caution)",
            {
                "fields": [
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ],
                "classes": ["collapse"],
            },),

        (
            'Important Dates',
            {
                "fields": ["date_joined", "last_login"]
            },
        ),

        ("Groups And Permissions",
            {
                "fields": ["groups", "user_permissions"],
                "classes": ["collapse"]
            }
         ),
    ]

    add_fieldsets = (
        (
            "User Personal Details",
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "phone_number",
                    "password1",
                    "password2"
                ),
            },
        ),

        (
            "User status",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "is_active"
                ),
            },
        ),
    )

    ordering = ['email']