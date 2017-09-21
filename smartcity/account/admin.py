from django.contrib import admin
from account.models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'email')

    def user_info(self, obj):
        return obj.role

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('email')
        return queryset

        role.short_description = 'User Type'


admin.site.register(UserProfile, UserProfileAdmin)

