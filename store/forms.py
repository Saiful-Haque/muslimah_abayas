from django import forms
from .models import Abaya, ContactInfo

class AbayaForm(forms.ModelForm):
    class Meta:
        model = Abaya
        fields = ['name', 'category', 'description', 'fabric', 'colors', 'image', 'is_featured']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g. Classic Silk Abaya'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe the abaya, styling, etc.'}),
            'fabric': forms.TextInput(attrs={'placeholder': 'e.g. Premium Crepe, Nidha'}),
            'colors': forms.TextInput(attrs={'placeholder': 'e.g. Midnight Black, Pearl Gray'}),
        }

class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['phone', 'email', 'opening_hours_weekdays', 'opening_hours_sat', 'opening_hours_sun', 'instagram', 'facebook', 'instagram_handle', 'facebook_handle', 'whatsapp']
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': '+91-9917041149'}),
            'email': forms.EmailInput(attrs={'placeholder': 'shopmuslimahabayas@gmail.com'}),
            'opening_hours_weekdays': forms.TextInput(attrs={'placeholder': 'Monday - Friday: 9:00 AM - 6:00 PM'}),
            'opening_hours_sat': forms.TextInput(attrs={'placeholder': 'Saturday: 10:00 AM - 4:00 PM'}),
            'opening_hours_sun': forms.TextInput(attrs={'placeholder': 'Sunday: Closed'}),
            'instagram': forms.URLInput(attrs={'placeholder': 'https://instagram.com/_muslimahabayas_'}),
            'facebook': forms.URLInput(attrs={'placeholder': 'https://facebook.com/Muslimah-Abayas'}),
            'instagram_handle': forms.TextInput(attrs={'placeholder': '_muslimahabayas_'}),
            'facebook_handle': forms.TextInput(attrs={'placeholder': 'Muslimah-Abayas'}),
            'whatsapp': forms.TextInput(attrs={'placeholder': '+91-9917041149'}),
        }
