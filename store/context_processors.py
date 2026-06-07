from .models import ContactInfo

def contact_info(request):
    try:
        # Get the first record, if it exists
        info = ContactInfo.objects.first()
        if not info:
            # Create a default record if none exists
            info = ContactInfo.objects.create()
    except Exception:
        # Fallback for migrations or db check steps before db initialization
        info = None
    return {
        'contact_info': info
    }
