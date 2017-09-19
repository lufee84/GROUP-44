from django.contrib import admin
from account.models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'email')

    def type(self, obj):
        return obj.type

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('email')
        return queryset


    type.short_description = 'User Type'


admin.site.register(UserProfile, UserProfileAdmin)

