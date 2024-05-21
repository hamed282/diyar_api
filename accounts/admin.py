from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import UserCreationForm, UserChangeForm
from .models import User, NewsletterSubscriptionModel


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['first_name', 'last_name', 'phone_number', 'national_code', 'email', 'city', 'is_admin', 'is_superuser']
    list_filter = ['is_active']

    readonly_fields = ['last_login']

    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'phone_number', 'national_code', 'city', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'is_superuser', 'last_login', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'phone_number', 'national_code', 'city', 'email', 'password')}),
    )

    search_fields = ['phone_number', 'first_name', 'last_name', 'national_code', 'city', 'email']
    ordering = ['first_name', 'last_name']

    filter_horizontal = ('groups', 'user_permissions')


class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['email']


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(NewsletterSubscriptionModel, NewsletterSubscriptionAdmin)
