import datetime
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from admin_panel.models import AboutUs, Branch, Brand, NewCar, Vehicle
from main_site.models import FAQ, Booking, CustomerReview
from .forms import BookingForm, CustomerQueryForm, CustomerReviewForm, VehicleCommentForm

# Create your views here.


# Home View
def home(request):
    new_cars = NewCar.objects.all().order_by('-id')
    about_details = AboutUs.objects.all()
    vehicles = Paginator(Vehicle.objects.all().order_by(
        '-id'), 9).get_page(request.GET.get('page'))
    pages = 'a' * vehicles.paginator.num_pages
    reviews = CustomerReview.objects.all().filter(is_active=True)

    context = {
        'new_cars': new_cars,
        'about_details': about_details,
        'vehicles': vehicles,
        'pages': pages,
        'reviews': reviews,
    }

    return render(request, 'main_site/home.html', context)


# Fleet View
def cars(request):
    vehicles = Paginator(Vehicle.objects.all().order_by(
        '-id'), 30).get_page(request.GET.get('page'))
    pages = 'a' * vehicles.paginator.num_pages
    brands = Brand.objects.all().order_by('brand_name')

    context = {
        'vehicles': vehicles,
        'pages': pages,
        'brands': brands
    }

    return render(request, 'main_site/cars.html', context)


# Filter Fleet By Brand View
def cars_by_brand(request, slug):
    try:
        brand = Brand.objects.get(slug=slug)
    except:
        raise Http404('Page not found')

    vehicles = Paginator(Vehicle.objects.all().filter(brand=brand).order_by(
        '-id'), 30).get_page(request.GET.get('page'))
    pages = 'a' * vehicles.paginator.num_pages
    brands = Brand.objects.all().order_by('brand_name')

    context = {
        'vehicles': vehicles,
        'pages': pages,
        'brands': brands,
        'brand': brand
    }

    return render(request, 'main_site/cars.html', context)


# Car Details View
def car_details(request, slug):
    try:
        vehicle = Vehicle.objects.get(slug=slug)
    except:
        raise Http404('Page not found')

    can_be_booked = True

    active_bookings = 0

    # Getting the number of active bookings on a particular vehicle
    for booking in vehicle.bookings.all():
        if booking.pick_up_date.date() == datetime.date.today():
            if booking.confirmed and not booking.completed:
                active_bookings += 1

    # Comparing the number of active bookings with the stock of that vehicle.
    if active_bookings == vehicle.stock:
        can_be_booked = False

    # Checking if method is POST method.
    if request.method == 'POST':
        # Verifying that the current user is authenticated
        if request.user.is_authenticated:
            vehicle_comment_form = VehicleCommentForm(request.POST)
            rating = request.POST['rating']

            # If vehicle comment form is valid, add a comment with the information provided.
            if vehicle_comment_form.is_valid():
                comment = vehicle_comment_form.save(commit=False)
                comment.rating = rating
                comment.vehicle = vehicle
                comment.user = request.user
                comment.should_show = False
                comment.save()
                messages.success(request, "Thank you for adding your comment.")
                return redirect('car_details', vehicle.slug)
        else:
            messages.error(
                request, "Sorry. Only registered users are allowed to add comments.")
            return redirect('car_details', vehicle.slug)

    else:
        vehicle_comment_form = VehicleCommentForm()
        booking_form = BookingForm()

    context = {
        'vehicle': vehicle,
        'vehicle_comment_form': vehicle_comment_form,
        'booking_form': booking_form,
        'can_be_booked': can_be_booked,
    }

    return render(request, 'main_site/car_details.html', context)


# Book Vehicle
@login_required
def book_car(request, slug):
    try:
        vehicle = Vehicle.objects.get(slug=slug)
    except:
        raise Http404('Page not found')

    booking_form = BookingForm(request.POST)

    # Checking if booking form is valid.
    if booking_form.is_valid():
        booking = booking_form.save(commit=False)
        booking.user = request.user
        booking.vehicle = vehicle
        booking.branch = vehicle.branch
        booking.save()

        return redirect('booking_history')


# Car Booking History
@login_required
def booking_history(request):
    bookings = Booking.objects.all().filter(
        user=request.user).order_by('-pick_up_date')

    context = {
        'bookings': bookings
    }
    return render(request, 'main_site/booking_history.html', context)


# FAQ View
def faqs(request):
    faqs = FAQ.objects.all()

    context = {
        'faqs': faqs,
    }
    return render(request, 'main_site/faq.html', context)


# Contact Us View
def contact(request):
    branches = Branch.objects.all()
    customerQueryForm = CustomerQueryForm()
    customerReviewForm = CustomerReviewForm()

    context = {
        'branches': branches,
        'customerQueryForm': customerQueryForm,
        'customerReviewForm': customerReviewForm,
    }

    return render(request, 'main_site/contact.html', context)


# Add Query View
def add_query(request):
    customerQueryForm = CustomerQueryForm(request.POST)

    # Checking if customerQueryForm is valid.
    if customerQueryForm.is_valid():
        customerQueryForm.save()

        return redirect('contact')


# Add Customer Review on Company
@login_required
def add_customer_review(request):
    customerReviewForm = CustomerReviewForm(request.POST)

    # Checking to see if customerReviewForm is valid.
    if customerReviewForm.is_valid():
        review = customerReviewForm.save(commit=False)
        review.user = request.user
        review.save()

        return redirect('contact')
