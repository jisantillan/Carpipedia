from django.contrib import admin
from .models import User, Avatar


@admin.register(User)
class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Avatar)
