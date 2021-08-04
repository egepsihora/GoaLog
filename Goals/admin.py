from django.contrib import admin
from .models import Goal, Category, Group


class GoalAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Priority', 'Status', 'Category',
                    'Group', 'Date_create', 'Date_start', 'Date_end')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Item', 'Help_text')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('Item', 'Help_text')


admin.site.register(Goal, GoalAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Group, GroupAdmin)

