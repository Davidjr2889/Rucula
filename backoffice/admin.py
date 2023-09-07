from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import GroupAdmin


from .models import UserProfile
from .models import TipoUser

import nested_admin


admin.site.register(TipoUser)
admin.site.unregister(User)


class ProfileInline(nested_admin.NestedStackedInline):
    model = UserProfile


@admin.register(User)
class UserAdmin(nested_admin.NestedModelAdmin, UserAdmin):
    inlines = [ProfileInline]

    list_display = ("username", "email", "first_name", "last_name", "get_tipo", "is_staff", "is_active")

    def get_tipo(self, obj):
        return obj.profile.tipo_usuario

    get_tipo.short_description = 'Tipo Usuario'
    get_tipo.admin_order_field = 'profile__tipo_usuario'

    class Media:
        css = {
            "all": ("css/admin_per.css",)
        }


admin.site.unregister(Group)


class GroupAdmin(GroupAdmin):

    class Media:
        css = {
            "all": ("css/admin_per.css",)
        }


admin.site.register(Group, GroupAdmin)
