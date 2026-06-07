from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Abaya, Inquiry, ContactInfo
from .forms import AbayaForm, ContactInfoForm

def intro_view(request):
    featured_abayas = Abaya.objects.filter(is_featured=True)[:3]
    return render(request, 'store/intro.html', {'featured_abayas': featured_abayas})

def catalog_view(request):
    abayas = Abaya.objects.all().order_by('-created_at')
    categories = Abaya.CATEGORY_CHOICES
    context = {
        'abayas': abayas,
        'categories': categories,
    }
    return render(request, 'store/catalog.html', context)

def detail_view(request, slug):
    abaya = get_object_or_404(Abaya, slug=slug)
    related_abayas = Abaya.objects.filter(category=abaya.category).exclude(id=abaya.id)[:3]
    context = {
        'abaya': abaya,
        'related_abayas': related_abayas,
    }
    return render(request, 'store/detail.html', context)

def submit_inquiry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message')
        abaya_id = request.POST.get('abaya_id')
        
        abaya = None
        if abaya_id:
            try:
                abaya = Abaya.objects.get(id=abaya_id)
            except Abaya.DoesNotExist:
                pass
                
        Inquiry.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message,
            abaya=abaya
        )
        
        messages.success(request, "Your inquiry has been submitted successfully! We will get back to you shortly.")
        if abaya:
            return redirect('detail_view', slug=abaya.slug)
        return redirect('catalog_view')
    return redirect('catalog_view')

def story_view(request):
    return render(request, 'store/story.html')

def contact_view(request):
    return render(request, 'store/contact.html')

# --- Custom Admin Dashboard Views ---

def dashboard_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('dashboard_view')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_staff:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('dashboard_view')
        else:
            messages.error(request, "Invalid credentials or unauthorized access.")
            
    return render(request, 'store/dashboard/login.html')

def dashboard_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect('intro_view')

def dashboard_view(request):
    if not (request.user.is_authenticated and request.user.is_staff):
        return redirect('dashboard_login')
        
    inquiries = Inquiry.objects.all().order_by('-created_at')
    abayas = Abaya.objects.all().order_by('-created_at')
    
    context = {
        'inquiries': inquiries,
        'abayas': abayas,
        'total_inquiries': inquiries.count(),
        'total_products': abayas.count(),
    }
    return render(request, 'store/dashboard/index.html', context)

def abaya_create_view(request):
    if not (request.user.is_authenticated and request.user.is_staff):
        return redirect('dashboard_login')
        
    if request.method == 'POST':
        form = AbayaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "New Abaya successfully added to collection.")
            return redirect('dashboard_view')
    else:
        form = AbayaForm()
        
    return render(request, 'store/dashboard/abaya_form.html', {
        'form': form,
        'title': 'Add New Abaya',
        'button_text': 'Add Abaya'
    })

def abaya_update_view(request, pk):
    if not (request.user.is_authenticated and request.user.is_staff):
        return redirect('dashboard_login')
        
    abaya = get_object_or_404(Abaya, pk=pk)
    if request.method == 'POST':
        form = AbayaForm(request.POST, request.FILES, instance=abaya)
        if form.is_valid():
            form.save()
            messages.success(request, f"'{abaya.name}' successfully updated.")
            return redirect('dashboard_view')
    else:
        form = AbayaForm(instance=abaya)
        
    return render(request, 'store/dashboard/abaya_form.html', {
        'form': form,
        'abaya': abaya,
        'title': f"Edit Abaya: {abaya.name}",
        'button_text': 'Save Changes'
    })

def abaya_delete_view(request, pk):
    if not (request.user.is_authenticated and request.user.is_staff):
        return redirect('dashboard_login')
        
    abaya = get_object_or_404(Abaya, pk=pk)
    name = abaya.name
    abaya.delete()
    messages.success(request, f"'{name}' has been deleted from collection.")
    return redirect('dashboard_view')

def update_contact_view(request):
    if not (request.user.is_authenticated and request.user.is_staff):
        return redirect('dashboard_login')
        
    contact_info = ContactInfo.objects.first()
    if not contact_info:
        contact_info = ContactInfo.objects.create()
        
    if request.method == 'POST':
        form = ContactInfoForm(request.POST, instance=contact_info)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact details successfully updated.")
            return redirect('dashboard_view')
    else:
        form = ContactInfoForm(instance=contact_info)
        
    return render(request, 'store/dashboard/contact_form.html', {
        'form': form,
    })

