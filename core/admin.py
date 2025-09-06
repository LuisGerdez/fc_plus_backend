from django.contrib import admin
from .models import User, SoccerField

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(SoccerField)
class SoccerFieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'capacity', 'is_enabled')
    search_fields = ('name', 'address')
    list_filter = ('is_enabled',)