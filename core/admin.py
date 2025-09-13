from django.contrib import admin
from .models import User, SoccerField, Match

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(SoccerField)
class SoccerFieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'capacity', 'is_enabled')
    search_fields = ('name', 'address')
    list_filter = ('is_enabled',)

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'field', 'match_type', 'price', 'status')
    list_filter = ('match_type', 'status', 'field')
    search_fields = ('field__name',)
    date_hierarchy = 'datetime'