from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from account.models import Account
from account.forms import CustomUserCreationForm, CustomUserCreationForm

@admin.register(Account)
class AccountModelAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'is_admin', 'is_staff', 'is_superuser')
    list_filter = ('username', 'date_joined')
    readonly_fields = ('pk', 'date_joined', 'last_login')
    filter_horizontal = ()
    add_form = CustomUserCreationForm
    form = CustomUserCreationForm
    model = Account
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
        ),
    )

