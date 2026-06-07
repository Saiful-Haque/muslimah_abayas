from django.contrib import admin
from .models import Abaya, Inquiry, ContactInfo

@admin.register(Abaya)
class AbayaAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'fabric', 'is_featured', 'created_at')
    list_filter = ('category', 'is_featured', 'created_at')
    search_fields = ('name', 'description', 'fabric')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-created_at',)

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'abaya', 'created_at')
    list_filter = ('created_at', 'abaya')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'phone', 'email')
