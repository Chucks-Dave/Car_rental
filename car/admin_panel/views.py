import datetime
from operator import index
from django.http import Http404
from django.shortcuts import redirect, render
from admin_panel.forms import AboutUsForm, BranchForm, BrandForm, FaqForm, NewCarForm, VehicleForm
from main_site.models import FAQ, Booking, CustomerQuery, CustomerReview
from . import models
from django.contrib import auth
from user.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


# Dashboard view
@login_required
def dashboard(request):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        bookings = Booking.objects.all()
        users = User.objects.all().filter(is_staff=False)
        new_users = 0

        # Getting the number of newly registered users
        for user in users:
            if user.date_joined.date() == datetime.date.today():
                new_users += 1

        booking_count = 0
        active_bookings = 0
        revenue = 0

        # Getting the total number of bookings and active bookings for today
        for booking in bookings:
            if booking.pick_up_date.date() == datetime.date.today():
                booking_count += 1
                if booking.confirmed and not booking.completed:
                    active_bookings += 1
                revenue += booking.vehicle.price

        vehicles = models.Vehicle.objects.all()
        total_no_of_vehicles = 0

        # Getting the total number of vehicles owned by the company
        for vehicle in vehicles:
            total_no_of_vehicles += vehicle.stock

        queries = CustomerQuery.objects.all()
        pending = queries.filter(resolved=False)

        no_of_days_recorded = 7
        no_of_days_recorded_in_prev_week = 14
        revenue_list = []
        last_week_revenue_list = []
        bookings_this_week = []
        bookings_last_week = []

        # Getting the total bookings and revenue for each day this week.
        for day in range(0, no_of_days_recorded, 1):
            revenue_list.append(0)
            bookings_this_week.append(0)
            for booking in bookings:
                if booking.pick_up_date.date() == datetime.date.today() - datetime.timedelta(days=day):
                    revenue_list[day] += booking.vehicle.price
                    bookings_this_week[day] += 1

        index = 0
        # Getting the total bookings and revenue for each day in the previous week.
        for day in range(7, no_of_days_recorded_in_prev_week, 1):
            last_week_revenue_list.append(0)
            bookings_last_week.append(0)
            for booking in bookings:
                if booking.pick_up_date.date() == datetime.date.today() - datetime.timedelta(days=day):
                    last_week_revenue_list[index] += booking.vehicle.price
                    bookings_last_week[index] += 1
            index += 1

        revenue_list_month = []
        last_month_revenue_list = []
        bookings_this_month = []
        bookings_last_month = []

        no_of_days_in_month_recorded = 31
        no_of_days_recorded_in_prev_month = 62

        # Getting the total bookings and revenue for each day this month.
        for day in range(0, no_of_days_in_month_recorded, 1):
            revenue_list_month.append(0)
            bookings_this_month.append(0)
            for booking in bookings:
                if booking.pick_up_date.date() == datetime.date.today() - datetime.timedelta(days=day):
                    revenue_list_month[day] += booking.vehicle.price
                    bookings_this_month[day] += 1

        index_m = 0
        # Getting the total bookings and revenue for each day in the previous month.
        for day in range(31, no_of_days_recorded_in_prev_month, 1):
            last_month_revenue_list.append(0)
            bookings_last_month.append(0)
            for booking in bookings:
                if booking.pick_up_date.date() == datetime.date.today() - datetime.timedelta(days=day):
                    last_month_revenue_list[index_m] += booking.vehicle.price
                    bookings_last_month[index_m] += 1
            index_m += 1

        context = {
            'bookings': bookings,
            'today': datetime.date.today(),
            'users': users,
            'new_users': new_users,
            'booking_count': booking_count,
            'active_bookings': active_bookings,
            'total_no_of_vehicles': total_no_of_vehicles,
            'available_vehicles': total_no_of_vehicles - active_bookings,
            'queries': queries,
            'pending': pending,
            'revenue': revenue,
            'revenue_list': revenue_list,
            'last_week_revenue_list': last_week_revenue_list,
            'bookings_this_week': bookings_this_week,
            'bookings_last_week': bookings_last_week,
            'revenue_list_month': revenue_list_month,
            'last_month_revenue_list': last_month_revenue_list,
            'bookings_this_month': bookings_this_month,
            'bookings_last_month': bookings_last_month,
        }

        return render(request, 'admin_panel/dashboard.html', context)
    else:
        return redirect('home')


# Manage Vehicles View
@login_required
def vehicles(request):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        brands = models.Brand.objects.all().order_by('brand_name')
        vehicles = models.Vehicle.objects.all().order_by('-id')

        context = {
            "brands": brands,
            "brandForm": BrandForm(),
            "vehicles": vehicles
        }

        return render(request, 'admin_panel/vehicles.html', context)
    else:
        return redirect('home')


# View Vehicle Details
@login_required
def vehicle_details(request, slug):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        vehicle = models.Vehicle.objects.get(slug=slug)

        context = {
            'vehicle': vehicle
        }
        return render(request, 'admin_panel/vehicledetails.html', context)
    else:
        return redirect('home')


# Filter Vehicles By Brand
@login_required
def filter_vehicle(request, slug):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        brands = models.Brand.objects.all().order_by('brand_name')
        try:
            brand = models.Brand.objects.get(slug=slug)
        except:
            raise Http404('Page not found')
        vehicles = models.Vehicle.objects.all().filter(
            brand=brand).order_by('-id')

        context = {
            "brands": brands,
            "brandForm": BrandForm(),
            "vehicles": vehicles
        }

        return render(request, 'admin_panel/vehicles.html', context)
    else:
        return redirect('home')


# Add Brand
@login_required
def add_brand(request):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:

        # Checking if method is a POST method.
        if request.method == "POST":
            addBrandForm = BrandForm(request.POST)

            # Checking if form is valid
            if addBrandForm.is_valid():
                addBrandForm.save()

                return redirect(request.META.get('HTTP_REFERER'))

        else:
            addBrandForm = BrandForm()

    else:
        return redirect('home')


# Edit Brand View
@login_required
def edit_brand(request, slug):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        try:
            brand = models.Brand.objects.get(slug=slug)
        except:
            raise Http404('Page not found')
        # Checking if method is a POST method
        if request.method == 'POST':
            editBrandForm = BrandForm(
                request.POST or None, instance=brand)

            # Checking if form is vaild
            if editBrandForm.is_valid():
                editBrandForm.save()

                return redirect('vehicles')

        else:
            editBrandForm = BrandForm(
                instance=brand)

        context = {
            'brandForm': editBrandForm,
        }
        return render(request, 'admin_panel/editbrand.html', context)

    else:
        return redirect('home')


# Delete brand view
@login_required
def delete_brand(request, slug):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        try:
            brand = models.Brand.objects.get(slug=slug)
        except:
            raise Http404('Page not found')

        brand.delete()

        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('home')


# Branches view
@login_required
def branches(request):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        branches = models.Branch.objects.all()

        no_of_days_recorded = 7
        bookings_this_week = []
        revenues_this_week = []

        index = 0
        # Getting the total number of bookings and revenue in each branch for the week
        for branch in branches:
            bookings_this_week.append(0)
            revenues_this_week.append(0)
            for day in range(0, no_of_days_recorded, 1):
                for booking in branch.bookings.all():
                    if booking.pick_up_date.date() == datetime.date.today() - datetime.timedelta(days=day):
                        bookings_this_week[index] += 1
                        revenues_this_week[index] += booking.vehicle.price
            index += 1

        context = {
            'branches': branches,
            'branchForm': BranchForm(),
            'bookings_this_week': bookings_this_week,
            'revenues_this_week': revenues_this_week,
        }

        return render(request, 'admin_panel/branches.html', context)
    else:
        return redirect('home')


# Add Branch
@login_required
def add_branch(request):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:

        # Checking if method is a POST method.
        if request.method == "POST":
            addBranchForm = BranchForm(request.POST)

            # Checking if form is vaild.
            if addBranchForm.is_valid():
                addBranchForm.save()

                return redirect(request.META.get('HTTP_REFERER'))

        else:
            addBranchForm = BrandForm()

    else:
        return redirect('home')


# Edit branch
@login_required
def edit_branch(request, slug):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        # Checking if method is a POST method
        try:
            branch = models.Branch.objects.get(slug=slug)
        except:
            raise Http404('Page not found')

        if request.method == 'POST':
            editBranchForm = BranchForm(
                request.POST or None, instance=branch)

            # Checking if form is valid
            if editBranchForm.is_valid():
                editBranchForm.save()

                return redirect('branches')

        else:
            editBranchForm = BranchForm(
                instance=branch)

        context = {
            'branchForm': editBranchForm,
        }
        return render(request, 'admin_panel/editbranch.html', context)

    else:
        return redirect('home')


# Delete branch
@login_required
def delete_branch(request, slug):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        try:
            branch = models.Branch.objects.get(slug=slug)
        except:
            raise Http404('Page not found')

        branch.delete()

        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('home')


# Add vehicle
@login_required
def add_vehicle(request):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        # Checking if method is a POST method
        if request.method == 'POST':
            vehicle_form = VehicleForm(request.POST, request.FILES)

            # Checking if form is valid
            if vehicle_form.is_valid():
                vehicle_form.save()

                return redirect('vehicles')

        else:
            vehicle_form = VehicleForm()
        context = {
            "vehicle_form": vehicle_form
        }

        return render(request, 'admin_panel/vehicleform.html', context)
    else:
        return redirect('home')


# Edit vehicle
@login_required
def edit_vehicle(request, slug):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        try:
            vehicle = models.Vehicle.objects.get(slug=slug)
        except:
            raise Http404('Page not found')
        # Checking if method is a POST method
        if request.method == 'POST':
            vehicle_form = VehicleForm(
                request.POST or None, request.FILES or None, instance=vehicle)

            # Checking if form is vaild.
            if vehicle_form.is_valid():
                vehicle_form.save()

                return redirect('vehicles')

        else:
            vehicle_form = VehicleForm(
                instance=vehicle)
        context = {
            "vehicle_form": vehicle_form,
            "vehicle": vehicle
        }

        return render(request, 'admin_panel/vehicleform.html', context)
    else:
        return redirect('home')


# Delete vehicle
@login_required
def delete_vehicle(request, slug):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        try:
            vehicle = models.Vehicle.objects.get(slug=slug)
        except:
            raise Http404('Page not found')

        vehicle.delete()

        return redirect('vehicles')
    else:
        return redirect('home')


# Toggle is_active property of vehicle comment
@login_required
def show_comment_in_website(request, id):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        try:
            comment = models.VehicleComment.objects.get(id=id)
        except:
            raise Http404('Page not found')

        comment.should_show = not comment.should_show
        comment.save()

        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('home')


# Delete user comment or testimonials
@login_required
def delete_comment(request, id):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        try:
            comment = models.VehicleComment.objects.get(id=id)
        except:
            raise Http404('Page not found')

        comment.delete()

        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('home')


# View all registered users that are not staff members
@login_required
def registered_users(request):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        users = User.objects.all().filter(is_staff=False).order_by("-last_login")

        context = {
            'users': users,
        }

        return render(request, 'admin_panel/user_list.html', context)
    else:
        return redirect('home')


# Delete registered user
@login_required
def delete_user(request, id):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        try:
            user = User.objects.get(id=id)
        except:
            raise Http404('Page not found')

        user.delete()

        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('home')


# Manage bookings view
@login_required
def bookings(request):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        bookings = Booking.objects.all().order_by('-id')

        context = {
            'bookings': bookings,
        }

        return render(request, 'admin_panel/bookings.html', context)
    else:
        return redirect('home')


# Confirm booking
@login_required
def confirm_booking(request, id):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        try:
            bookings = Booking.objects.get(id=id)
        except:
            raise Http404('Page not found')

        bookings.confirmed = True
        bookings.save()

        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('home')


# Cancel booking
@login_required
def cancel_booking(request, id):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        try:
            bookings = Booking.objects.get(id=id)
        except:
            raise Http404('Page not found')

        bookings.confirmed = False
        bookings.save()

        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('home')


# Complete booking
@login_required
def complete_booking(request, id):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        try:
            bookings = Booking.objects.get(id=id)
        except:
            raise Http404('Page not found')

        bookings.completed = not bookings.completed
        bookings.save()

        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('home')


# Delete booking
@login_required
def delete_booking(request, id):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        try:
            booking = Booking.objects.get(id=id)
        except:
            raise Http404('Page not found')

        booking.delete()

        return redirect('bookings')
    else:
        return redirect('home')


# View booking details
@login_required
def booking_details(request, id):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        bookings = Booking.objects.all().order_by('-id')
        try:
            booking = Booking.objects.get(id=id)
        except:
            raise Http404('Page not found')

        context = {
            'bookings': bookings,
            'booking': booking,
        }

        return render(request, 'admin_panel/booking_details.html', context)
    else:
        return redirect('home')


# Manage customer queries View
@login_required
def manage_queries(request):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        queries = CustomerQuery.objects.all()
        context = {
            'queries': queries,
        }

        return render(request, 'admin_panel/manage_queries.html', context)
    else:
        return redirect('home')


# Resolve customer queries
@login_required
def resolved_queries(request, id):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        try:
            query = CustomerQuery.objects.get(id=id)
        except:
            raise Http404('Page not found')

        query.resolved = True
        query.save()

        return redirect('manage_queries')
    else:
        return redirect('home')


# Manage website content View
@login_required
def manage_site(request):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        new_cars = models.NewCar.objects.all()
        vehicles = models.Vehicle.objects.all()
        about_details = models.AboutUs.objects.all()
        addAboutUsForm = AboutUsForm()
        editAboutUsForm = AboutUsForm()
        reviews = CustomerReview.objects.all()
        faqs = FAQ.objects.all()
        queries = CustomerQuery.objects.all()

        context = {
            'new_cars': new_cars,
            'vehicles': vehicles,
            'about_details': about_details,
            'addAboutUsForm': addAboutUsForm,
            'editAboutUsForm': editAboutUsForm,
            'reviews': reviews,
            'faqs': faqs,
            'queries': queries,
        }
        return render(request, 'admin_panel/manage_site.html', context)
    else:
        return redirect('home')


# Add new car
@login_required
def add_new_car(request, slug):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        new_car_form = NewCarForm(request.POST)

        try:
            vehicle = models.Vehicle.objects.get(slug=slug)
        except:
            raise Http404('Page not found')

        # Checking if form is vaild.
        if new_car_form.is_valid():
            new_car = new_car_form.save(commit=False)
            new_car.vehicle = vehicle
            new_car.save()

            return redirect('manage_site')

    else:
        return redirect('home')


# Remove new car or Delete new car
@login_required
def remove_new_car(request, id):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        try:
            new_car = models.NewCar.objects.get(id=id)
        except:
            raise Http404('Page not found')

        new_car.delete()

        return redirect('manage_site')
    else:
        return redirect('home')


# Add about us
@login_required
def add_about_us(request):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:

        # Checking if about us already exists in the database.
        # If it does, It can't add another.
        # Else, It would create a new about us item to the AboutUs table.
        if models.AboutUs.objects.all().count() == 0 or None:
            addAboutUsForm = AboutUsForm(request.POST)

            # Checking if form is vaild.
            if addAboutUsForm.is_valid():
                addAboutUsForm.save()

                return redirect('manage_site')

        else:
            return redirect('manage_site')

    else:
        return redirect('home')


# Edit about us
@login_required
def edit_about_us(request, id):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        try:
            aboutus = models.AboutUs.objects.get(id=id)
        except:
            raise Http404('Page not found')
        
        editAboutUsForm = AboutUsForm(
            request.POST or None, instance=aboutus)

        # Checking if form is vaild.
        if editAboutUsForm.is_valid():
            editAboutUsForm.save()

            return redirect('manage_site')

    else:
        return redirect('home')


# Toggle is_active property in the Customer Review model.
@login_required
def show_review(request, id):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        try:
            review = CustomerReview.objects.get(id=id)
        except:
            raise Http404('Page not found')

        review.is_active = not review.is_active
        review.save()
        return redirect('manage_site')
    else:
        return redirect('home')


# Delete Customer Review
@login_required
def delete_review(request, id):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        try:
            review = CustomerReview.objects.get(id=id)
        except:
            raise Http404('Page not found')

        review.delete()

        return redirect('manage_site')
    else:
        return redirect('home')


# Add FAQ
@login_required
def add_faq(request, id):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        try:
            query = CustomerQuery.objects.get(id=id)
        except:
            raise Http404('Page not found')

        # Checking if method is a POST method
        if request.method == 'POST':
            faqForm = FaqForm(request.POST)

            # Checking if form is vaild.
            if faqForm.is_valid():
                faq = faqForm.save(commit=False)
                faq.query = query
                faq.save()
                return redirect('manage_site')
        else:
            faqForm = FaqForm()

        context = {
            'faqForm': faqForm,
            'query': query,
        }
        return render(request, 'admin_panel/faq_form.html', context)
    else:
        return redirect('home')


# Edit FAQ
@login_required
def edit_faq(request, id):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        try:
            faq = FAQ.objects.get(id=id)
        except:
            raise Http404('Page not found')
        
        query = faq.query

        # Checking if method is a POST method
        if request.method == 'POST':
            faqForm = FaqForm(request.POST or None, instance=faq)

            # Checking if form is vaild.
            if faqForm.is_valid():
                faq = faqForm.save(commit=False)
                faq.query = query
                faq.save()
                return redirect('manage_site')
        else:
            faqForm = FaqForm(instance=faq)

        context = {
            'faqForm': faqForm,
            'query': query,
        }
        return render(request, 'admin_panel/faq_form.html', context)
    else:
        return redirect('home')


# Delete FAQ
@login_required
def delete_faq(request, id):
    # Verify that the user is staff to prevent unauthorised users from accessing the page.
    if request.user.is_staff:
        try:
            faq = FAQ.objects.get(id=id)
        except:
            raise Http404('Page not found')
        
        faq.delete()

        return redirect('manage_site')
    else:
        return redirect('home')
