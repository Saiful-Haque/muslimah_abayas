from django.db import models
from django.utils.text import slugify

class Abaya(models.Model):
    CATEGORY_CHOICES = [
        ('classic', 'Classic Black'),
        ('modern', 'Modern Pastels'),
        ('luxury', 'Luxury Embroidery'),
        ('casual', 'Casual Comfort'),
    ]

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='classic')
    description = models.TextField()
    fabric = models.CharField(max_length=100)
    colors = models.CharField(max_length=200, help_text="Comma-separated list, e.g. Onyx Black, Dusty Gold")
    image = models.ImageField(upload_to='abayas/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    abaya = models.ForeignKey(Abaya, on_delete=models.SET_NULL, null=True, blank=True, related_name='inquiries')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.name} for {self.abaya.name if self.abaya else 'General'}"

class ContactInfo(models.Model):
    phone = models.CharField(max_length=50, default="+91-9917041149")
    email = models.EmailField(default="shopmuslimahabayas@gmail.com")
    opening_hours_weekdays = models.CharField(max_length=100, default="Monday - Friday: 9:00 AM - 6:00 PM")
    opening_hours_sat = models.CharField(max_length=100, default="Saturday: 10:00 AM - 4:00 PM")
    opening_hours_sun = models.CharField(max_length=100, default="Sunday: Closed")
    instagram = models.URLField(max_length=300, default="https://instagram.com/_muslimahabayas_")
    facebook = models.URLField(max_length=300, default="https://facebook.com/Muslimah-Abayas")
    instagram_handle = models.CharField(max_length=100, default="_muslimahabayas_")
    facebook_handle = models.CharField(max_length=100, default="Muslimah-Abayas")
    whatsapp = models.CharField(max_length=50, default="+91-9917041149")

    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"

    def clean_whatsapp(self):
        # Keep only numbers
        return "".join([c for c in self.whatsapp if c.isdigit()])

    def __str__(self):
        return "Contact Details"
