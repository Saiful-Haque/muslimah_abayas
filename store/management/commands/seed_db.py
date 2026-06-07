from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from store.models import Abaya, ContactInfo

class Command(BaseCommand):
    help = 'Seeds the database with default Abayas and creates the superuser'

    def handle(self, *args, **options):
        # 1. Create Superuser
        User = get_user_model()
        username = 'admin'
        password = '12345'
        email = 'admin@example.com'

        if not User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f"Creating superuser '{username}'..."))
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created successfully!"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' already exists."))

        # 2. Seed ContactInfo
        self.stdout.write(self.style.WARNING("Checking contact info..."))
        if not ContactInfo.objects.exists():
            ContactInfo.objects.create(
                phone="+91-9917041149",
                email="shopmuslimahabayas@gmail.com",
                opening_hours_weekdays="Monday - Friday: 9:00 AM - 6:00 PM",
                opening_hours_sat="Saturday: 10:00 AM - 4:00 PM",
                opening_hours_sun="Sunday: Closed",
                instagram="https://instagram.com/_muslimahabayas_",
                facebook="https://facebook.com/Muslimah-Abayas",
                instagram_handle="_muslimahabayas_",
                facebook_handle="Muslimah-Abayas",
                whatsapp="+91-9917041149"
            )
            self.stdout.write(self.style.SUCCESS("Default ContactInfo record created."))
        else:
            self.stdout.write(self.style.SUCCESS("ContactInfo record already exists."))

        # 3. Seed Abayas
        abayas_data = [
            {
                'name': 'Classic Onyx Black Abaya',
                'category': 'classic',
                'description': 'Indulge in the luxury of pure Nida silk with our Classic Onyx Black Abaya. Designed with graceful draping, tailored sleeves, and detailed cuffs, it offers a timeless silhouette perfect for formal and everyday settings.',
                'fabric': 'Premium Nida Silk',
                'colors': 'Onyx Black',
                'image': 'abayas/classic_black.png',
                'is_featured': True
            },
            {
                'name': 'Pastel Blue Linen Abaya',
                'category': 'modern',
                'description': 'Designed for the modern woman, this lightweight pastel blue abaya features a breathable linen-mix fabric. Beautifully soft colors bring an air of casual elegance, making it an excellent choice for daytime gatherings.',
                'fabric': 'Organic Linen Blend',
                'colors': 'Pastel Blue, Dove Grey',
                'image': 'abayas/pastel_blue.png',
                'is_featured': True
            },
            {
                'name': 'Emerald Gold Embro Embroidered Abaya',
                'category': 'luxury',
                'description': 'Adorned with intricate gold embroidery along the sleeve borders and front collar, this stunning emerald green abaya is the epitome of luxurious modesty. Crafted from premium velvet-crepe fabric for special occasions.',
                'fabric': 'Velvet Crepe',
                'colors': 'Emerald Green, Gold',
                'image': 'abayas/emerald_gold.png',
                'is_featured': True
            },
            {
                'name': 'Desert Beige Casual Abaya',
                'category': 'casual',
                'description': 'A relaxed, loose-fit design crafted for daily comfort. Made of lightweight organic cotton, this casual desert beige abaya is perfect for warm weather and features convenient side pockets and simple clean lines.',
                'fabric': 'Organic Cotton',
                'colors': 'Desert Beige, Sand',
                'image': 'abayas/beige_casual.png',
                'is_featured': False
            }
        ]

        self.stdout.write(self.style.WARNING("Seeding abayas catalog..."))
        for item in abayas_data:
            abaya, created = Abaya.objects.get_or_create(
                name=item['name'],
                defaults={
                    'category': item['category'],
                    'description': item['description'],
                    'fabric': item['fabric'],
                    'colors': item['colors'],
                    'image': item['image'],
                    'is_featured': item['is_featured']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created: {abaya.name}"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Exists: {abaya.name}"))

        self.stdout.write(self.style.SUCCESS("Database seeding completed!"))
