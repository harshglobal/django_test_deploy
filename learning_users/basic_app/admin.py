from django.contrib import admin
from .models import UserProfileInfo, User

# Register your models here.
# admin.site.register(UserProfileInfo)

@admin.register(UserProfileInfo)
class AdminUserForm(admin.ModelAdmin):
    list_display= ['user','portfolio_site','profile_pic']
