from django.contrib import admin

# Register your models here.
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
   list_display = ('title', 'category', 'url', 'views')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'views', 'likes', 'slug')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)