from asyncio import Task
from django import forms
from .models import Verification, Volunteer
from .models import Organization

class VerificationForm(forms.ModelForm):
    class Meta:
        model = Verification
        fields = ['username', 'password', 'position']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'class': 'input', 'id': 'signup-email', 'required': True}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'input', 'id': 'signup-password', 'required': True}),
            'position': forms.TextInput(attrs={'placeholder': 'Position', 'class': 'input', 'id': 'signup-position', 'required': True}),
        }

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['full_name', 'contact_number', 'age', 'skills', 'cnic', 'email', 'city']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'input', 'id': 'signup-name', 'required': True}),
            'contact_number': forms.TextInput(attrs={'placeholder': 'Contact Number', 'class': 'input', 'id': 'signup-contact', 'required': True}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age', 'class': 'input', 'id': 'signup-age', 'required': True}),
            'skills': forms.Textarea(attrs={'placeholder': 'List your skills here...', 'class': 'input', 'id': 'signup-skills', 'required': True}),
            'cnic': forms.TextInput(attrs={'placeholder': '12345-1234567-1', 'class': 'input', 'id': 'signup-cnic', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'input', 'id': 'signup-email', 'required': True}),
            'city': forms.TextInput(attrs={'placeholder': 'City', 'class': 'input', 'id': 'signup-city', 'required': True}),
        }
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))




from django import forms
from .models import Feedback
from django import forms
from .models import Feedback, Volunteer, Event
from django import forms
from .models import Feedback, Volunteer, Event
from django import forms
from .models import Feedback, Volunteer, Event
from django import forms
from .models import Feedback, Volunteer, Event
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [ 'event', 'rating', 'comments']
    
    # Ask for the volunteer's username instead of choosing from a list
    volunteer_username = forms.CharField(max_length=255, required=True, label="Enter Volunteer Username")
    
    # Event field with the dropdown to choose event
    event = forms.ModelChoiceField(queryset=Event.objects.all(), empty_label="Choose an Event")
    
    # Rating field (1-5 scale)
    rating = forms.IntegerField(min_value=1, max_value=5, required=True)
    
    # Optional comments field (text area)
    comments = forms.CharField(widget=forms.Textarea, required=False)

    # Override label_from_instance to display event_name in the dropdown
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['event'].label_from_instance = lambda obj: obj.event_name

    # Custom validation for the volunteer username
    def clean_volunteer_username(self):
        username = self.cleaned_data.get('volunteer_username')
        try:
            # Retrieve the Volunteer object via the Verification model
            verification = Verification.objects.get(username=username)
            volunteer = Volunteer.objects.get(volunteer=verification)
        except Verification.DoesNotExist:
            raise forms.ValidationError("No user found with this username.")
        except Volunteer.DoesNotExist:
            raise forms.ValidationError("This user is not registered as a volunteer.")
        
        return volunteer

    def save(self, commit=True):
        # Set the volunteer field to the volunteer object based on the username
        volunteer = self.cleaned_data.get('volunteer_username')
        self.instance.volunteer = volunteer
        return super().save(commit)


from django import forms

class TaskRequestForm(forms.Form):
    task_id = forms.IntegerField(widget=forms.HiddenInput())
    organization_id = forms.IntegerField(widget=forms.HiddenInput())



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Task, Verification
from django.views.decorators.csrf import csrf_exempt


from django import forms
from .models import Admin  # Make sure you have an Admin model or adjust the model name accordingly

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin  # Replace with your actual Admin model
        fields = ['admin_name']
        widgets = {
            'admin_name': forms.TextInput(attrs={'placeholder': 'Enter admin name', 'class': 'input', 'id': 'signup-admin-name', 'required': True}),
        }
from django import forms
from .models import Organization

class OrganizationForm(forms.ModelForm):
    # List of organization types as choices
    ORGANIZATION_TYPES = [
        ('corporate', 'Corporate'),
        ('nonprofit', 'Nonprofit'),
        ('educational', 'Educational'),
        ('government', 'Government'),
        ('startup', 'Startup')
    ]

    # Adding password field
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input', 'required': True, 'placeholder': 'Password'}),
        label="Password"
    )

    org_type = forms.ChoiceField(
        choices=ORGANIZATION_TYPES,
        widget=forms.Select(attrs={'class': 'input', 'required': True}),
        label="Organization Type"
    )

    class Meta:
        model = Organization
        fields = [
            'org_name', 'ceo_name', 'contact_email',
            'contact_number', 'headoffice_address', 'org_type', 'password'
        ]
        widgets = {
            'org_name': forms.TextInput(attrs={
                'placeholder': 'Organization Name',
                'class': 'input',
                'required': True
            }),
            'ceo_name': forms.TextInput(attrs={
                'placeholder': 'CEO Name',
                'class': 'input',
                'required': True
            }),
            'contact_email': forms.EmailInput(attrs={
                'placeholder': 'Contact Email',
                'class': 'input',
                'required': True
            }),
            'contact_number': forms.TextInput(attrs={
                'placeholder': 'Contact Number',
                'class': 'input',
                'required': True
            }),
            'headoffice_address': forms.Textarea(attrs={
                'placeholder': 'Head Office Address',
                'class': 'input',
                'required': True
            }),
        }

from django import forms
from .models import Event, Organization  # Assuming the Event and Organization models are in the same directory

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['org', 'event_name', 'description', 'event_date', 'location']
    
    # Organization field
    org = forms.ModelChoiceField(
        queryset=Organization.objects.all(),  # Dynamically fetch all registered organizations
        widget=forms.Select(attrs={'class': 'custom-dropdown', 'required': True}),
        label="Select Organization"
    )
    
    # Event Name field
    event_name = forms.CharField(
        max_length=255, 
        widget=forms.TextInput(attrs={'placeholder': 'Event Name', 'class': 'input', 'required': True}),
        label="Event Name"
    )
    
    # Description field
    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Event Description', 'class': 'input'}),
        required=False,
        label="Description"
    )
    
    # Event Date field
    event_date = forms.DateField(
        widget=forms.DateInput(attrs={'placeholder': 'Event Date (YYYY-MM-DD)', 'class': 'input', 'required': True}),
        label="Event Date"
    )
    
    # Location field
    location = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Event Location', 'class': 'input'}),
        required=False,
        label="Location"
    )

    # forms.py
from django import forms

class AssignTaskForm(forms.Form):
    task_id = forms.IntegerField()
    user_id = forms.IntegerField()
