from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about_page, name='about'),  # About Page
    path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'),  # Admin Dashboard
    path('admin-view-feedbacks/', views.admin_view_feedbacks, name='admin-view-feedbacks'),  # Admin View Feedbacks
    path('admin-view-volunteers/', views.admin_view_vol, name='admin-view-volunteers'),  # Admin View Volunteers
    path('contact/', views.contact_page, name='contact'),  # Contact Page
    path('join-button-options/', views.join_button_options, name='join-button-options'),  # Join Button Options
    path('landing/', views.landing_page, name='landing'),  # Landing Page
    path('login/', views.login_page, name='login'),  # Login
    path('login-admin/', views.login_admin, name='login-admin'),  # Admin Login
    path('login-org/', views.login_org, name='login-org'),  # Organization Login
    path('login-volunteer/', views.login_volunteer, name='login-volunteer'),  # Volunteer Login
    path('organization-dashboard/', views.organization_dashboard, name='organization-dashboard'),  # Organization Dashboard
    path('org-create-event/', views.org_create_event, name='org-create-event'),  # Create Event in Organization
    path('org-view-requests/', views.org_view_requests, name='org_view_requests'),  # View Requests in Organization
    path('volunteer-dashboard/', views.volunteer_dashboard, name='volunteer-dashboard'),  # Volunteer Dashboard
    path('volunteer-feedback/', views.volunteer_feedback, name='volunteer-feedback'),  # Volunteer Feedback
    path('volunteer-past-experience/', views.volunteer_past_experience, name='volunteer-past-experience'),  # Volunteer Past Experience
   path('volunteer-take-tasks/<str:event_name>/', views.volunteer_take_tasks, name='volunteer-take-tasks'),
 path('admin-view-org/', views.admin_view_org, name='admin-view-org'),  # Admin View Organizations
       path('tasks/<str:event_name>/take/', views.volunteer_take_tasks, name='volunteer-take-tasks'),
      path('submit-task/', views.submit_task, name='submit_task'),
      path('check-database-status/', views.check_database_status, name='check_database_status'),
 path('volunteer-leaderboard/', views.volunteer_leaderboard, name='volunteer-leaderboard'),  # Leaderboard URL
path('delete_organization/<int:org_id>/', views.delete_organization, name='delete_organization'),
    path('delete_volunteer/<int:volunteer_id>/', views.delete_volunteer, name='delete_volunteer'),

  path('assign_task/', views.assign_task, name='assign_task'),
  

path('show_notifications/', views.show_notifications, name='show_notifications')
]

   

