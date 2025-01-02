import datetime
from gettext import translation
from urllib import request
from venv import logger
from django.shortcuts import render
from django.shortcuts import render
from .models import Event
from .models import Task
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from django.shortcuts import render
from django.db import connection
from datetime import datetime

from django.core.mail import send_mail
from django.http import JsonResponse
from .models import VolunteerTask, Volunteer


from django.core.mail import send_mail
from django.http import JsonResponse
from .models import VolunteerTask, Volunteer
from django.core.mail import send_mail
from django.http import JsonResponse
from .models import Volunteer
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.http import JsonResponse


from django.shortcuts import render
from django.http import JsonResponse
from .models import VolunteerTask, Volunteer, Task
from django.http import JsonResponse
from .models import VolunteerTask
from django.http import JsonResponse
from .models import VolunteerTask
from django.shortcuts import render
from django.shortcuts import render
from .models import VolunteerTask, Task, Volunteer  # Import relevant models
from django.shortcuts import render
from django.shortcuts import render
from .models import VolunteerTask, Task, Event, Organization, Verification, Volunteer
from django.shortcuts import render
from django.db import connection
from datetime import datetime
from django.shortcuts import render
from django.utils import timezone
from .models import Task, Event
from django.shortcuts import render
from django.utils import timezone
from .models import Task, Event

from django.db.models import Q
from django.shortcuts import render
from .models import Event 
from django.shortcuts import render
from .models import Event
from datetime import datetime
from django.shortcuts import render
from django.db import connection
from django.shortcuts import render
from django.db import connection
from django.db import connection
from django.shortcuts import render
from django.shortcuts import render
from django.db.models import Avg
from .models import Feedback, Event
from django.shortcuts import render
from django.db import connection
from django.shortcuts import render
from django.db import connection
from django.db import connection
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Verification, Organization, Event, Task  # Import necessary models   
import json
from django.http import JsonResponse
from django.shortcuts import render

import json
from django.http import JsonResponse
from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Task, Verification, Event
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Task, Verification, Event
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Task, Verification, Event
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Task, Verification, Event
from django.http import JsonResponse
from .models import Task, Verification, Event
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Event, Verification
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Task, Verification, Event
from django.http import JsonResponse
from .models import Task, Verification, Event
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Task, Verification, Event
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Task, Event, Verification
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Task, Event, Verification
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Task, Verification, Event
from django.http import JsonResponse
from django.db import connection
from django.db.utils import OperationalError

import json
import traceback
from django.http import JsonResponse
from django.shortcuts import render
from .models import TaskSubmission, VolunteerTask, Task, Volunteer
from django.http import JsonResponse
from django.db import transaction  # Correct import for transaction management
import json
import traceback
from .models import Task, Volunteer, VolunteerTask
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import AssignTaskForm
from .models import Task, Volunteer, VolunteerTask
from django.db import transaction
from django.shortcuts import render
from django.http import JsonResponse
from django.db import transaction
from .forms import AssignTaskForm
from .models import TaskSubmission, Task, Volunteer, VolunteerTask

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from .models import Verification
from .forms import EventForm, LoginForm, OrganizationForm, VerificationForm, VolunteerForm
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm, VerificationForm, VolunteerForm # type: ignore
from .models import Verification

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Verification, Organization, Event, Task
from datetime import datetime
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from .models import Verification
from .forms import LoginForm, VerificationForm, VolunteerForm # type: ignore
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm, VerificationForm, VolunteerForm # type: ignore
from .models import Verification

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm, VerificationForm, VolunteerForm # type: ignore
from .models import Verification
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from .forms import VerificationForm, VolunteerForm, LoginForm

from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from .forms import LoginForm, VerificationForm, VolunteerForm
from .models import Verification, Volunteer
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm, VerificationForm, VolunteerForm # type: ignore
from .models import Verification
from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from .models import Task, Event

from django.shortcuts import get_object_or_404, render
from .models import Task, Event


from django.db.models import Count

# View for Admin View Organizations
from django.shortcuts import render
from django.db import connection
from django.db import connection
from django.shortcuts import render
from django.db import connection
from django.shortcuts import render
from .models import Event
from .models import Task
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# View for Volunteer Login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AdminForm, VerificationForm, LoginForm  # Importing relevant forms
from .models import Verification, Admin  # Assuming Admin model is created
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AdminForm, VerificationForm, LoginForm  # Importing relevant forms
from .models import Verification, Admin  # Assuming Admin model is created

from django.shortcuts import get_object_or_404, render
from .models import Task, Event

from django.shortcuts import get_object_or_404, render
from .models import Task, Event

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages


from django.shortcuts import render, get_object_or_404
from .models import Task, Event
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import connection
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event, Task

# View for Volunteer Feedback
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feedback, Event, Volunteer
from django.utils import timezone
from django.shortcuts import render
from .models import Feedback  # Make sure to import the Feedback model
from django.http import HttpResponseRedirect
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.http import JsonResponse


from django.shortcuts import render
from django.http import JsonResponse
from .models import VolunteerTask, Task, Volunteer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import TaskSubmission
from django.http import JsonResponse
from django.shortcuts import render

from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render
from .models import Feedback  # Assuming Feedback model is imported
from django.utils import timezone
from django.utils import timezone
from django.shortcuts import render, redirect
from .models import Feedback, Volunteer, Event
from django import forms
from django.utils import timezone

from django import forms
from .models import Feedback

from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import FeedbackForm
from .models import Feedback
# views.py
from django.shortcuts import render, redirect
from .forms import FeedbackForm  # Import the form
from django.utils import timezone
from .models import Feedback
from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.utils import timezone
from django.contrib import messages

from django.db import connection
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone

# View for About Page
def about_page(request):
    return render(request, 'volunteers/VMS-aboutPage.html')


def admin_dashboard(request):
    # Retrieve the username from the session
    username = request.session.get('username', 'Guest')  # Default to 'Guest' if not logged in
    
    # Get the search query from the request
    search_query = request.GET.get('search', '').strip()
    
    # Raw SQL query to fetch filtered events based on search query
    with connection.cursor() as cursor:
        if search_query:
            cursor.execute("""
                SELECT event_id, org_id, event_name, description, event_date, location
                FROM Event
                WHERE event_name LIKE %s OR location LIKE %s OR description LIKE %s
            """, [f"%{search_query}%", f"%{search_query}%", f"%{search_query}%"])
        else:
            cursor.execute("""
                SELECT event_id, org_id, event_name, description, event_date, location
                FROM Event
            """)
        rows = cursor.fetchall()
    
    # Transform rows into a list of dictionaries for easier use in the template
    events = [
        {
            "event_id": row[0],
            "org_id": row[1],
            "event_name": row[2],
            "description": row[3],
            "event_date": row[4],
            "location": row[5],
        }
        for row in rows
    ]

    # Pass events and search query to the template
    return render(request, 'volunteers/VMS-adminDashboard.html', {'username': username, 'events': events, 'search_query': search_query})



def admin_view_feedbacks(request):
    """
    View to retrieve and display feedback records using raw SQL queries with a search option.
    """
    # Retrieve the username from the session
    username = request.session.get('username', 'Guest')  # Default to 'Guest' if not logged in

    # Get the search term from the request (default to empty string if not provided)
    search_term = request.GET.get('search', '')

    # Raw SQL query to fetch feedback data, filtered by the search term if provided
    feedback_query = """
        SELECT 
            f.feedback_id,
            v.full_name AS volunteer_name,
            v.email AS volunteer_email,
            e.event_name,
            o.org_name AS organization_name,
            f.rating,
            f.comments,
            f.date_submitted
        FROM Feedback f
        INNER JOIN Volunteer v ON f.volunteer_id = v.volunteer_id
        INNER JOIN Event e ON f.event_id = e.event_id
        INNER JOIN Organization o ON e.org_id = o.org_id
        WHERE v.full_name LIKE %s 
           OR v.email LIKE %s 
           OR e.event_name LIKE %s 
           OR o.org_name LIKE %s
    """

    # Fetch feedback data with the search term
    with connection.cursor() as cursor:
        cursor.execute(feedback_query, [f'%{search_term}%', f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'])
        feedbacks = cursor.fetchall()

    feedback_data = []
    for feedback in feedbacks:
        feedback_data.append({
            'feedback_id': feedback[0],
            'volunteer_name': feedback[1],
            'volunteer_email': feedback[2],
            'event_name': feedback[3],
            'organization_name': feedback[4],
            'rating': feedback[5],
            'comments': feedback[6],
            'date_submitted': feedback[7].strftime('%Y-%m-%d %H:%M:%S') if feedback[7] else "N/A"
        })

    # Fetch event data
    event_query = """
        SELECT DISTINCT o.org_name
        FROM Event e
        INNER JOIN Organization o ON e.org_id = o.org_id
    """
    with connection.cursor() as cursor:
        cursor.execute(event_query)
        events = cursor.fetchall()

    event_data = [{'organization_name': event[0]} for event in events]

    # Fetch leaderboard data
    leaderboard_query = """
        SELECT 
            o.org_name AS organization_name,
            ROUND(AVG(f.rating), 2) AS avg_rating
        FROM Feedback f
        INNER JOIN Event e ON f.event_id = e.event_id
        INNER JOIN Organization o ON e.org_id = o.org_id
        GROUP BY o.org_name
        ORDER BY avg_rating DESC
        LIMIT 3
    """
    with connection.cursor() as cursor:
        cursor.execute(leaderboard_query)
        leaderboard = cursor.fetchall()

    leaderboard_data = []
    for rank, entry in enumerate(leaderboard, start=1):
        leaderboard_data.append({
            'rank': rank,
            'organization_name': entry[0],
            'avg_rating': entry[1]
        })

    # Render the data to the HTML template
    return render(request, 'volunteers/VMS-adminViewFeedbacks.html', {
        'feedbacks': feedback_data,
        'events': event_data,
        'leaderboard': leaderboard_data,
        'username': username,
        'search_term': search_term  # Pass the search term back to the template
    })


def admin_view_vol(request):
    """
    View to retrieve and display all volunteers using raw SQL queries with a search option.
    """
    # Retrieve the username from the session
    username = request.session.get('username', 'Guest')  # Default to 'Guest' if not logged in

    # Get the search term from the request (default to empty string if not provided)
    search_term = request.GET.get('search', '')

    # Raw SQL query to fetch volunteer data, filtered by the search term if provided
    volunteer_query = """
        SELECT 
            volunteer_id, 
            full_name, 
            contact_number, 
            age, 
            skills, 
            CNIC, 
            email, 
            city
        FROM Volunteer
        WHERE full_name LIKE %s OR city LIKE %s OR skills LIKE %s
    """

    # Fetch volunteer data
    with connection.cursor() as cursor:
        cursor.execute(volunteer_query, [f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'])
        volunteers = cursor.fetchall()

    # Process volunteer data into a dictionary
    volunteer_data = []
    for volunteer in volunteers:
        volunteer_data.append({
            'volunteer_id': volunteer[0],
            'full_name': volunteer[1],
            'contact_number': volunteer[2],
            'age': volunteer[3],
            'skills': volunteer[4],
            'CNIC': volunteer[5],
            'email': volunteer[6],
            'city': volunteer[7],
        })

    # Render the data to the HTML template
    return render(request, 'volunteers/VMS-adminViewVol.html', {
        'username': username,
        'volunteers': volunteer_data,
        'search_term': search_term,  # Pass the search term to the template
    })



# View for deleting volunteer
def delete_volunteer(request, volunteer_id):
    # Get the volunteer object or return 404 if not found
    volunteer = get_object_or_404(Volunteer, volunteer_id=volunteer_id)
    
    # Retrieve the corresponding Verification user
    verification_user = Verification.objects.get(user_id=volunteer.volunteer_id)
    
    # Delete the Verification record (which cascades to the Volunteer table)
    verification_user.delete()

    # Redirect back to the volunteers list (or wherever you want)
    return redirect('admin-view-volunteers')  # Adjust the redirect URL as needed
# View for Contact Page
def contact_page(request):
    return render(request, 'volunteers/VMS-contactPage.html')

# View for Join Button Options
def join_button_options(request):
    return render(request, 'volunteers/VMS-joinButtonOptions.html')

# View for Landing Page
def landing_page(request):
    return render(request, 'volunteers/VMS-landingPage.html')

# View for Login
def login_page(request):
    return render(request, 'volunteers/VMS-login.html')
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm, VerificationForm, OrganizationForm
from .models import Verification, Organization

def login_org(request):
    # Initialize the forms for login, verification, and organization
    login_form = LoginForm()
    verification_form = VerificationForm()
    organization_form = OrganizationForm()

    if request.method == 'POST':
        if 'login' in request.POST:  # Login button pressed
            # Reinitialize login form with POST data
            login_form = LoginForm(request.POST)

            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']

                try:
                    # Check if the user exists in the Verification table
                    user = Verification.objects.get(username=username)

                    # Check if the user is associated with an organization
                    try:
                        organization = Organization.objects.get(org=user)
                        if user.password == password:  # Directly compare password (no hashing)
                            # Save the username in the session
                            request.session['username'] = username  # Only save the username

                            # Redirect to the organization dashboard
                            return redirect('organization-dashboard')
                        else:
                            messages.error(request, "Invalid password.")
                    except Organization.DoesNotExist:
                        messages.error(request, "This user is not associated with any organization.")
                
                except Verification.DoesNotExist:
                    messages.error(request, "Invalid username.")
            else:
                messages.error(request, "Please fill in the form correctly.")

        elif 'signup' in request.POST:  # Signup button pressed
            # Reinitialize the forms with POST data
            verification_form = VerificationForm(request.POST)
            organization_form = OrganizationForm(request.POST)

            if verification_form.is_valid() and organization_form.is_valid():
                # Save the user to the Verification model
                verification_instance = verification_form.save(commit=False)
                verification_instance.save()

                # Save the user to the Organization model
                organization_instance = organization_form.save(commit=False)
                organization_instance.org = verification_instance  # Associate with the Verification instance
                organization_instance.save()

                messages.success(request, "Signup successful! Please log in.")
                return redirect('login')  # Redirect to the login page after signup

            else:
                messages.error(request, "Signup failed. Please check your details.")

    return render(request, 'volunteers/VMS-loginOrg.html', {
        'login_form': login_form,
        'verification_form': verification_form,
        'organization_form': organization_form
    })

# View for Volunteer Feedback
def volunteer_feedback(request):
    return render(request, 'volunteers/VMS-volunteerFeedback.html')

# View for Volunteer Past Experience
def volunteer_past_experience(request):
    return render(request, 'volunteers/VMS-volunteerPastExperience.html')


@login_required
def volunteer_take_tasks(request, event_name):
    # Fetch the event
    event = get_object_or_404(Event, event_name=event_name)

    # Directly get the logged-in user's username
    username = request.user.username  # This returns the username of the currently logged-in user

    # Fetch tasks related to the event
    tasks = Task.objects.filter(event=event)

    # Render the template with tasks and username
    return render(request, 'volunteers/VMS-volunteerTakeTasks.html', {
        'tasks': tasks,
        'event': event,
        'username': username,  # Pass the username to the template
    })





# View for About Page
def about_page(request):
    return render(request, 'volunteers/VMS-aboutPage.html')




# View for Contact Page
def contact_page(request):
    return render(request, 'volunteers/VMS-contactPage.html')

# View for Join Button Options
def join_button_options(request):
    return render(request, 'volunteers/VMS-joinButtonOptions.html')

# View for Landing Page
def landing_page(request):
    return render(request, 'volunteers/VMS-landingPage.html')

# View for Login
def login_page(request):
    return render(request, 'volunteers/VMS-login.html')



def login_admin(request):
    # Initialize forms to avoid UnboundLocalError
    login_form = LoginForm()
    admin_form = AdminForm()
    verification_form = VerificationForm()

    if request.method == 'POST':
        if 'login' in request.POST:  # Login button pressed
            login_form = LoginForm(request.POST)  # Reinitialize with POST data
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                try:
                    # Check if user exists in Verification table
                    user = Verification.objects.get(username=username)
                    if user.password == password:  # Directly compare password (no hashing)
                        # Save username in session
                        request.session['username'] = username  # Only save the username

                        # Redirect to admin dashboard
                        return redirect('admin-dashboard')
                    else:
                        messages.error(request, "Invalid password.")
                except Verification.DoesNotExist:
                    messages.error(request, "Invalid username.")
            else:
                messages.error(request, "Please fill in the form correctly.")

        elif 'signup' in request.POST:  # Signup button pressed
            verification_form = VerificationForm(request.POST)
            admin_form = AdminForm(request.POST)

            if verification_form.is_valid() and admin_form.is_valid():
                try:
                    # Save the verification form first
                    verification_instance = verification_form.save()

                    # Save the admin form with reference to verification
                    admin_instance = admin_form.save(commit=False)
                    admin_instance.admin_id = verification_instance.user_id
                    admin_instance.save()

                    # Manually create a session for the logged-in user
                    # Save the username and other session details after successful signup
                    request.session['username'] = verification_instance.username

                    # Redirect to the admin-dashboard after successful signup
                    return redirect('admin-dashboard')

                except Exception as e:
                    print("Error saving admin record:", e)
                    messages.error(request, "An error occurred during signup. Please try again.")
            else:
                print("Verification Form Errors:", verification_form.errors)
                print("Admin Form Errors:", admin_form.errors)
                messages.error(request, "Signup failed. Please check your details.")
        
        
    # Render the template with all forms (initialized or updated)
    return render(request, 'volunteers/VMS-loginAdmin.html', {
        'login_form': login_form,
        'admin_form': admin_form,
        'verification_form': verification_form
    })





def volunteer_dashboard(request):
    # Retrieve the username from the session
    username = request.session.get('username', 'Guest')  # Default to 'Guest' if not logged in
    
    # Fetch tasks with a deadline greater than or equal to the current time
    tasks = Task.objects.filter(deadline__gte=timezone.now())

    # Get the search term from the GET request
    search_term = request.GET.get('search_term', '')

    # Fetch events, filter by search term if provided
    if search_term:
        events = Event.objects.filter(
            Q(event_name__icontains=search_term) | 
            Q(location__icontains=search_term) | 
            Q(description__icontains=search_term)
        )
    else:
        events = Event.objects.all()

    # Pass the username, tasks, and events to the template
    return render(request, 'volunteers/VMS-volunteerDashboard.html', {
        'username': username, 
        'tasks': tasks, 
        'events': events,
        'search_term': search_term  # Pass the search term to the template for persistence in the search bar
    })



def volunteer_feedback(request):
    username = request.session.get('username', 'Guest')
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.date_submitted = timezone.now()
            feedback.save()
            messages.success(request, 'Your feedback has been submitted successfully!')
            return redirect('volunteer-feedback')  # Redirect to the same page or a dashboard
    else:
        form = FeedbackForm()

    return render(request, 'volunteers/VMS-volunteerFeedback.html', {'form': form,'username': username})




def volunteer_past_experience(request):
    username = request.session.get('username', 'Guest')

    # Fetch the Verification object based on username
    try:
        verification = Verification.objects.get(username=username)
    except Verification.DoesNotExist:
        verification = None

    if verification:
        # Fetch the Volunteer object related to the Verification object
        volunteer = Volunteer.objects.filter(volunteer_id=verification.user_id).first()

        if volunteer:
            # Fetch all past experiences associated with the volunteer
            volunteer_tasks = VolunteerTask.objects.filter(volunteer=volunteer).select_related('task', 'task__org')

            experience_data = []
            for vt in volunteer_tasks:
                event_name = vt.task.event.event_name if vt.task.event else "No event name"
                organization_name = vt.task.org.org_name if vt.task.org else "No organization name"
                event_date = vt.task.event.event_date if vt.task.event else "No event date"

                experience_data.append({
                    'event_name': event_name,
                    'task_name': vt.task.title,  # Assuming task title is available
                    'organization_name': organization_name,
                    'date': event_date,
                    'status': vt.status,
                })

            return render(request, 'volunteers/VMS-volunteerPastExperience.html', {
                'username': username,
                'experiences': experience_data,
            })
        else:
            # If no volunteer found, render with empty experiences list
            return render(request, 'volunteers/VMS-volunteerPastExperience.html', {
                'username': username,
                'experiences': []
            })
    else:
        # If no Verification object found, render with empty experiences list
        return render(request, 'volunteers/VMS-volunteerPastExperience.html', {
            'username': username,
            'experiences': []
        })




def admin_view_org(request):
    """
    View to retrieve and display organization data using raw SQL queries with a search option.
    """
    # Get the username from the session or default to 'Guest'
    username = request.session.get('username', 'Guest')

    # Get the search term from the request (default to empty string if not provided)
    search_term = request.GET.get('search', '')

    # Raw SQL query to fetch all organizations, filtered by the search term if provided
    organization_query = f"""
        SELECT 
            org_id, 
            org_name, 
            ceo_name, 
            contact_email, 
            contact_number, 
            headOffice_address, 
            org_type
        FROM Organization
        WHERE org_name LIKE %s OR ceo_name LIKE %s
    """

    # Raw SQL query to fetch head office address data grouped by count
    location_query = """
        SELECT 
            headOffice_address, 
            COUNT(*) AS address_count
        FROM Organization
        GROUP BY headOffice_address
        ORDER BY address_count DESC
    """

    # Fetch organization data
    with connection.cursor() as cursor:
        cursor.execute(organization_query, [f'%{search_term}%', f'%{search_term}%'])
        organizations = cursor.fetchall()

        cursor.execute(location_query)
        location_data = cursor.fetchall()

    # Process organization data into a dictionary
    organization_data = []
    for org in organizations:
        organization_data.append({
            'org_id': org[0],
            'org_name': org[1],
            'ceo_name': org[2],
            'contact_email': org[3],
            'contact_number': org[4],
            'headOffice_address': org[5],
            'org_type': org[6],
        })

    # Process location data into a dictionary for Chart.js
    location_dict = {entry[0]: entry[1] for entry in location_data}

    # Prepare data for the pie chart
    chart_labels = list(location_dict.keys())  # Extract labels (head office addresses)
    chart_values = list(location_dict.values())  # Extract values (address counts)

    # Render the template with the required context
    return render(request, 'volunteers/VMS.adminViewOrg.html', {
        'username': username,
        'organizations': organization_data,
        'location_data': location_dict,
        'chart_labels': chart_labels,  # Pass chart labels
        'chart_values': chart_values,  # Pass chart values
        'search_term': search_term,  # Pass the search term to the template
    })

from django.shortcuts import render, get_object_or_404, redirect
from .models import Organization, Verification

from django.shortcuts import get_object_or_404, redirect
from .models import Organization, Verification, TaskSubmission

def delete_organization(request, org_id):
    # Get the organization object or return 404 if not found
    organization = get_object_or_404(Organization, org_id=org_id)
    
    # Retrieve the corresponding Verification user
    verification_user = Verification.objects.get(user_id=organization.org_id)
    
    # Get all related Task instances that belong to this organization
    tasks = organization.task_set.all()
    
    # Delete task submissions that belong to any of the tasks related to the organization
    TaskSubmission.objects.filter(task__in=tasks).delete()
    
    # Now delete the Verification record (which cascades to the Organization table)
    verification_user.delete()

    # Redirect back to the organizations list
    return redirect('admin-view-org')  # Adjust the redirect URL as needed



def login_volunteer(request):
    # Initialize forms to avoid errors
    login_form = LoginForm()
    verification_form = VerificationForm()
    volunteer_form = VolunteerForm()

    if request.method == 'POST':
        if 'login' in request.POST:  # Login button pressed
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']

                try:
                    # Verify user credentials using Django ORM
                    user = Verification.objects.filter(username=username).first()
                    if user:
                        if user.password == password:  # Simple password comparison (use hashing in production)
                            request.session['username'] = username  # Save username in session
                            return redirect('volunteer-dashboard')  # Redirect after successful login
                        else:
                            messages.error(request, "Incorrect password.")
                    else:
                        messages.error(request, "User does not exist.")
                except Exception as e:
                    messages.error(request, f"An error occurred: {e}")
            else:
                messages.error(request, "Please fill out the login form correctly.")

        elif 'signup' in request.POST:  # Signup button pressed
            verification_form = VerificationForm(request.POST)
            volunteer_form = VolunteerForm(request.POST)

            if verification_form.is_valid() and volunteer_form.is_valid():
                try:
                    # Save the Verification model instance
                    verification_data = verification_form.save()

                    # Fetch the username used during signup
                    username_used = verification_data.username

                    # Create the Volunteer instance and associate it with the Verification instance
                    volunteer_data = volunteer_form.save(commit=False)
                    volunteer_data.volunteer = verification_data  # Set the foreign key to the Verification instance
                    volunteer_data.save()  # Save the volunteer data

                    # Save the username in the session to use on the dashboard
                    request.session['username'] = username_used

                    messages.success(request, "Signup successful! Please log in.")
                    return redirect('volunteer-dashboard')
                except IntegrityError as e:
                    messages.error(request, f"Signup failed due to database integrity error: {e}")
                except Exception as e:
                    messages.error(request, f"Signup failed. Error: {e}")
            else:
                messages.error(request, "Please fill out the signup form correctly.")

    return render(request, 'volunteers/VMS-loginVolunteer.html', {
        'login_form': login_form,
        'verification_form': verification_form,
        'volunteer_form': volunteer_form
    })


from django.http import JsonResponse

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Task, Verification, Event

def volunteer_take_tasks(request, event_name):
    # Fetch the event using event_name
    username = request.session.get('username', 'Guest')  # Get the username from session or default to 'Guest'
    event = get_object_or_404(Event, event_name=event_name)  # Fetching event by its name
    
    # Fetch tasks related to the given event
    tasks = Task.objects.filter(event=event)  # Assuming Task has a ForeignKey to Event

    # Fetch user_id based on the username from the Verification table
    try:
        verification = Verification.objects.get(username=username)  # Match username in the Verification table
        user_id = verification.user_id  # Get the user_id from the Verification table
    except Verification.DoesNotExist:
        user_id = None  # Handle case if the username doesn't exist in Verification table

    # Render the template with tasks, event details, and user_id
    return render(request, 'volunteers/VMS-volunteerTakeTasks.html', {
        'username': username,  # Passing the username to the template
        'tasks': tasks,
        'event': event,  # Passing the event object to the template
        'user_id': user_id  # Pass the user_id (if found) to the template
    })
def check_database_status(request):
    try:
        # Try to query a sample record or just check the table
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1 FROM taskrequests LIMIT 1;")
        return JsonResponse({'success': True, 'message': 'Database is accessible!'})
    except OperationalError as e:
        # If there's an error, it means the database or table is not accessible
        return JsonResponse({'success': False, 'message': 'Database is not accessible.'})
import logging
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Task, Event, Verification
from django.core.exceptions import ObjectDoesNotExist

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
import logging

def login_volunteer(request):
    # Initialize forms to avoid errors
    login_form = LoginForm()
    verification_form = VerificationForm()
    volunteer_form = VolunteerForm()

    if request.method == 'POST':
        if 'login' in request.POST:  # Login button pressed
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']

                try:
                    # Verify user credentials using Django ORM
                    user = Verification.objects.filter(username=username).first()
                    if user:
                        if user.password == password:  # Simple password comparison (use hashing in production)
                            request.session['username'] = username  # Save username in session
                            return redirect('volunteer-dashboard')  # Redirect after successful login
                        else:
                            messages.error(request, "Incorrect password.")
                    else:
                        messages.error(request, "User does not exist.")
                except Exception as e:
                    messages.error(request, f"An error occurred: {e}")
            else:
                messages.error(request, "Please fill out the login form correctly.")

        elif 'signup' in request.POST:  # Signup button pressed
            verification_form = VerificationForm(request.POST)
            volunteer_form = VolunteerForm(request.POST)

            if verification_form.is_valid() and volunteer_form.is_valid():
                try:
                    # Save the Verification model instance
                    verification_data = verification_form.save()

                    # Fetch the username used during signup
                    username_used = verification_data.username

                    # Create the Volunteer instance and associate it with the Verification instance
                    volunteer_data = volunteer_form.save(commit=False)
                    volunteer_data.volunteer = verification_data  # Set the foreign key to the Verification instance
                    volunteer_data.save()  # Save the volunteer data

                    # Save the username in the session to use on the dashboard
                    request.session['username'] = username_used

                    messages.success(request, "Signup successful! Please log in.")
                    return redirect('volunteer-dashboard')
                except IntegrityError as e:
                    messages.error(request, f"Signup failed due to database integrity error: {e}")
                except Exception as e:
                    messages.error(request, f"Signup failed. Error: {e}")
            else:
                messages.error(request, "Please fill out the signup form correctly.")

    return render(request, 'volunteers/VMS-loginVolunteer.html', {
        'login_form': login_form,
        'verification_form': verification_form,
        'volunteer_form': volunteer_form
    })

from django.shortcuts import render
from .models import Verification, Volunteer  # Import your models

from django.shortcuts import render
from .models import Verification
from django.shortcuts import render
from .models import Verification, Volunteer

def volunteer_leaderboard(request):
    # Get all volunteers and their scores from the Volunteer table
    volunteers = Volunteer.objects.all().order_by('-score')  # Sort by score descending

    # Generate leaderboard data with rank
    leaderboard_data = []
    rank = 1
    for volunteer in volunteers:
        leaderboard_data.append({
            'username': volunteer.full_name,  # Assuming full_name is stored in the Volunteer table
            'score': volunteer.score,
            'rank': rank
        })
        rank += 1  # Increment rank

    return render(request, 'volunteers/VMS-volunteerLeaderBoard.html', {'leaderboard': leaderboard_data})
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
import logging
from .models import Task, Event, Verification, TaskSubmission
from django.db import IntegrityError

# Logger setup (you may have it elsewhere in your project)
logger = logging.getLogger(__name__)

def submit_task(request):
    if request.method == 'POST':
        # Ensure the user is authenticated (check session or authentication status)
        username = request.session.get('username', None)
        if not username:
            return JsonResponse({'success': False, 'message': 'User is not logged in.'})

        task_title = request.POST.get('task_title')
        event_name = request.POST.get('event_name')

        if not task_title or not event_name:
            return JsonResponse({'success': False, 'message': 'Task title and event name are required.'})

        try:
            # Fetch the event by event_name
            event = get_object_or_404(Event, event_name=event_name)
            event_id = event.event_id  # Event ID

            # Log the event details using the correct attribute (event_name)
            logger.info(f"Event Name: {event.event_name}, Event ID: {event_id}")

            # Retrieve the organization (org_id) based on the event
            org_id = event.org.org_id  # Access org_id from the related Organization

            # Retrieve user_id from Verification model based on username
            verification = Verification.objects.get(username=username)
            user_id = verification.user_id  # User ID from Verification model

            # Fetch the task based on task_title and event
            task = get_object_or_404(Task, title=task_title, event=event)
            task_id = task.task_id  # Task ID

            # Debugging log for verification
            logger.info(f"Task Title: {task_title}, Task ID: {task_id}, Event ID: {event_id}, Org ID: {org_id}, User ID: {user_id}")

            # Create a TaskSubmission object and save it to the database
            task_submission = TaskSubmission(
                task_id=task_id,
                event_id=event_id,
                organization_id=org_id,
                user_id=user_id
            )

            task_submission.save()  # Save the task submission to the database

            # Return a JSON response with task details
            return JsonResponse({
                'success': True,
                'message': 'Task submission received!',
                'task_id': task_id,
                'event_id': event_id,  # Include event_id in response
                'org_id': org_id,      # Include org_id in response
                'user_id': user_id,    # Include user_id in response
            })

        except ObjectDoesNotExist as e:
            logger.error(f"Error occurred: {str(e)}")
            return JsonResponse({'success': False, 'message': 'Requested task or event does not exist.'})

        except IntegrityError as e:
            logger.error(f"Integrity error: {str(e)}")
            return JsonResponse({'success': False, 'message': 'A database integrity error occurred.'})

        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return JsonResponse({'success': False, 'message': 'An error occurred while processing your request.'})

    return JsonResponse({'success': False, 'message': 'Invalid request method. Use POST instead.'})



def organization_dashboard(request):
    # Retrieve the username from the session
    username = request.session.get('username', 'Guest')  # Default to 'Guest' if not logged in

    # Get the search query from the request
    search_query = request.GET.get('search', '')

    # Filter events based on the search query
    if search_query:
        events = Event.objects.filter(event_name__icontains=search_query)
    else:
        events = Event.objects.all()

    # Render the dashboard template
    return render(request, 'volunteers/VMS-organizationDashboard.html', {
        'username': username,
        'events': events,
        'search_query': search_query,
    })

from django.core.mail import send_mail
from volunteers.models import EmailQueue, Volunteer

def send_assigned_task_email():
    # Get all unprocessed email queue entries
    email_queue_entries = EmailQueue.objects.filter(email_sent=False)

    for entry in email_queue_entries:
        volunteer = Volunteer.objects.get(id=entry.volunteer_id)
        
        # Construct the email content
        subject = 'Hello, You have been assigned a new task!'
        message = f"Dear {volunteer.full_name},\n\nYou have been assigned a new task (Task ID: {entry.task_id}).\n\nRegards,\nYour Organization"
        from_email = 'no-reply@yourorganization.com'
        recipient_list = [volunteer.email]

        # Send the email
        send_mail(subject, message, from_email, recipient_list)

        # Mark this entry as processed
        entry.email_sent = True
        entry.save()




def org_create_event(request):
    # Get the username from the session (using session.get directly)
    username = request.session.get('username')

    if not username:
        messages.error(request, 'User not found in the session.')
        return redirect('login')  # Redirect to the login page if username is not in session

    if request.method == 'POST':
        try:
            # Fetch the Verification record by username (exact match)
            verification_record = Verification.objects.get(username=username)
            user_id = verification_record.user_id  # Retrieve the user_id from the Verification table
        except Verification.DoesNotExist:
            # If the user is not found in the Verification table
            messages.error(request, 'User not found in the verification table.')
            return redirect('org-create-event')

        # Check if the organization exists for this user_id (considering user_id as org_id)
        try:
            organization = Organization.objects.get(org_id=user_id)
        except Organization.DoesNotExist:
            # If no organization exists for the given user_id
            messages.error(request, 'Organization not found for this user.')
            return redirect('org-create-event')

        # Data for the Event
        event_name = request.POST.get('event_name')
        description = request.POST.get('description')
        event_date = request.POST.get('event_date')
        location = request.POST.get('location')

        # Create the event with org_id (user_id)
        event = Event.objects.create(
            org_id=user_id,  # Setting the org_id from user_id
            event_name=event_name,
            description=description,
            event_date=event_date,
            location=location
        )

        # Retrieve tasks data from the form
        task_titles = request.POST.getlist('task_titles[]')  # Retrieve all task titles as a list
        task_descriptions = request.POST.getlist('tasks[]')  # Retrieve all task descriptions as a list
        task_deadlines = request.POST.getlist('task_deadlines[]')  # Retrieve all task deadlines as a list

        # Get the current time
        current_time = timezone.now()

        # Ensure the tasks have the same length
        for i in range(len(task_titles)):
            task_name = task_titles[i]
            task_description = task_descriptions[i]
            task_deadline = task_deadlines[i]

            # Create tasks for the event
            Task.objects.create(
                org_id=user_id,  # The org_id is set from user_id (as per your request)
                event=event,
                title=task_name,  # Set title from form input
                description=task_description,  # Set description from form input
                deadline=task_deadline,  # Set deadline from form input
                date_created=current_time  # Set the current time as the creation time
            )

        # Success message
        messages.success(request, 'Event and tasks created successfully.')
        return redirect('org-create-event')

    return render(request, 'volunteers/VMS-orgCreateEvent.html', {'username': username})



import json
import logging


logger = logging.getLogger(__name__)
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import TaskSubmission

def org_view_requests(request):
    # Fetch all task submissions and pass them to the template
     org_view_requests = TaskSubmission.objects.all().select_related(
        'task', 'event', 'organization', 'user', 'user__volunteer'  # 'user__volunteer' to get the related Volunteer data
    )
     
     return render(request, 'volunteers/VMS-orgViewRequests.html', {'org_view_requests': org_view_requests})
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import VolunteerTask, Task, Volunteer

@csrf_exempt  # Only use @csrf_exempt if you can't pass CSRF tokens in your request, but try to avoid it.
def assign_task(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            task_id = data.get('task_id')
            volunteer_id = data.get('volunteer_id')

            # Retrieve Task and Volunteer instances
            task = Task.objects.get(task_id=task_id)
            volunteer = Volunteer.objects.get(volunteer=volunteer_id)

            # Create and save the VolunteerTask instance
            volunteer_task = VolunteerTask(task=task, volunteer=volunteer, status='Assigned')
            volunteer_task.save()

            return JsonResponse({'status': 'success', 'message': 'Task assigned successfully'})

        except Task.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Task not found'})

        except Volunteer.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Volunteer not found'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


from django.shortcuts import render
from .models import VolunteerTask, Verification, Volunteer, Task

def show_notifications(request):
    # Get the username from session or default to 'Guest'
    username = request.session.get('username', 'Guest')
    
    try:
        # Ensure the user is logged in
        if username == 'Guest':
            return render(request, 'volunteers/VMS-requestNotifications.html', {'error': 'You need to be logged in to view notifications.'})
        
        # Get the user_id from the Verification table based on the username
        verification = Verification.objects.get(username=username)
        
        # Get the associated volunteer based on the user_id
        volunteer = Volunteer.objects.get(volunteer_id=verification.user_id)

        # Get all assigned tasks for this specific volunteer
        assigned_tasks = VolunteerTask.objects.filter(volunteer=volunteer, status='Assigned')

        notifications = []

        # Create notification messages for the assigned tasks
        for task in assigned_tasks:
            task_info = task.task  # Accessing the task related to the VolunteerTask

            notification_message = {
                'volunteer_name': volunteer.full_name,
                'task_title': task_info.title,
                'task_description': task_info.description,
                'notification': f"Your request for the task '{task_info.title}' has been accepted."
            }

            notifications.append(notification_message)

        # Render the template with the notifications
        return render(request, 'volunteers/VMS-requestNotifications.html', {'notifications': notifications, 'username': username})

    except Verification.DoesNotExist:
        return render(request, 'volunteers/VMS-requestNotifications.html', {'error': 'Verification record not found for this user.', 'username': username})
    except Volunteer.DoesNotExist:
        return render(request, 'volunteers/VMS-requestNotifications.html', {'error': 'Volunteer profile not found for this user.', 'username': username})
    except Exception as e:
        return render(request, 'volunteers/VMS-requestNotifications.html', {'error': str(e), 'username': username})
