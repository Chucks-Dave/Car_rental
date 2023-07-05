from django.urls import path

from .views import *


urlpatterns = [
    # Dashboard
    path('dashboard/', dashboard, name='dashboard'),

    # Vehicles URLs
    path('vehicles/', vehicles, name='vehicles'),
    path('vehicles/add_brand/', add_brand, name='add_brand'),
    path('vehicles/edit_brand/<slug:slug>/', edit_brand, name='edit_brand'),
    path('vehicles/delete_brand-<slug:slug>/',
         delete_brand, name='delete_brand'),
    path('vehicles/add_vehicle/', add_vehicle, name="add_vehicle"),
    path('vehicles/<slug:slug>/', vehicle_details, name="vehicle_details"),
    path('vehicles/filter/<slug:slug>/', filter_vehicle, name="filter_vehicle"),
    path('vehicles/edit/<slug:slug>/', edit_vehicle, name="edit_vehicle"),
    path('vehicles/delete_vehicle/<slug:slug>/',
         delete_vehicle, name="delete_vehicle"),

    # Branches URLs
    path('branches/', branches, name='branches'),
    path('branches/add_branch/', add_branch, name='add_branch'),
    path('branches/edit_branch/<slug:slug>/',
         edit_branch, name='edit_branch'),
    path('branches/delete_branch/<slug:slug>/',
         delete_branch, name='delete_branch'),

    # Show Customer Review
    path('show_comment_in_site/<int:id>/',
         show_comment_in_website, name="show_comment_in_site"),
    path('delete_comment/<int:id>/', delete_comment, name="delete_comment"),

    # Manage Users URLs
    path('registered_users/', registered_users, name='registered_users'),
    path('registered_users/delete_user/<int:id>/',
         delete_user, name='delete_user'),

    # Bookings URLs
    path('bookings/', bookings, name="bookings"),
    path('bookings/confirm/<int:id>', confirm_booking, name="confirm_booking"),
    path('bookings/cancel/<int:id>', cancel_booking, name="cancel_booking"),
    path('bookings/complete/<int:id>',
         complete_booking, name="complete_booking"),
    path('bookings/delete/<int:id>', delete_booking, name="delete_booking"),
    path('bookings/details/<int:id>', booking_details, name="booking_details"),

    # Manage Customer Queries URLs
    path('customer_queries/', manage_queries, name="manage_queries"),
    path('customer_queries/resolve/<int:id>',
         resolved_queries, name="resolved_queries"),

    # Manage Site URLs
    path('manage_site/', manage_site, name="manage_site"),
    path('manage_site/add_new_car/<slug:slug>/',
         add_new_car, name="add_new_car"),
    path('manage_site/remove_new_car/<int:id>/',
         remove_new_car, name="remove_new_car"),
    path('manage_site/add_about_us/',
         add_about_us, name="add_about_us"),
    path('manage_site/edit_about_us/<int:id>',
         edit_about_us, name="edit_about_us"),
    path('manage_site/show_review/<int:id>', show_review, name="show_review"),
    path('manage_site/delete_review/<int:id>',
         delete_review, name="delete_review"),
    path('manage_site/add_faq/<int:id>', add_faq, name="add_faq"),
    path('manage_site/edit_faq/<int:id>', edit_faq, name="edit_faq"),
    path('manage_site/delete_faq/<int:id>', delete_faq, name="delete_faq"),
]
