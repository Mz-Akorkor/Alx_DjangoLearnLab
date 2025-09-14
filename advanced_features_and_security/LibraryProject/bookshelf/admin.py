from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    list_display = ("username", "email", "first_name", "last_name", "is_staff")

admin.site.register(CustomUser, CustomUserAdmin)

# Customize the admin interface for Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # columns shown in list view

    search_fields = ("title", "author")  # search box

    list_filter = ("publication_year",)  # sidebar filter
