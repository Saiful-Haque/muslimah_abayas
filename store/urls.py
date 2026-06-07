from django.urls import path
from . import views

urlpatterns = [
    path('', views.intro_view, name='intro_view'),
    path('collection/', views.catalog_view, name='catalog_view'),
    path('abaya/<slug:slug>/', views.detail_view, name='detail_view'),
    path('inquiry/submit/', views.submit_inquiry, name='submit_inquiry'),
    path('story/', views.story_view, name='story_view'),
    path('contact/', views.contact_view, name='contact_view'),
    
    # Custom Admin Dashboard
    path('dashboard/', views.dashboard_view, name='dashboard_view'),
    path('dashboard/login/', views.dashboard_login, name='dashboard_login'),
    path('dashboard/logout/', views.dashboard_logout, name='dashboard_logout'),
    path('dashboard/abaya/add/', views.abaya_create_view, name='abaya_create_view'),
    path('dashboard/abaya/<int:pk>/edit/', views.abaya_update_view, name='abaya_update_view'),
    path('dashboard/abaya/<int:pk>/delete/', views.abaya_delete_view, name='abaya_delete_view'),
    path('dashboard/contact/edit/', views.update_contact_view, name='update_contact_view'),
]
