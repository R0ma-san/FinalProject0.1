from django.contrib import admin

from .models import Category, University, Specialization, Country

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "country", "is_published")
    list_display_links = ("name",)
    list_filter = ("category__name", "price", "country", )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    list_display_links = ("name",)


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    list_display_links = ("name",)

@admin.register(Country)
class CountrynAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    list_display_links = ("name",)
