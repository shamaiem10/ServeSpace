from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Admin(models.Model):
    admin = models.OneToOneField('Verification', models.DO_NOTHING, primary_key=True)
    admin_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'admin'

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)

class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)

class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)

class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    org = models.ForeignKey('Organization', models.DO_NOTHING)
    event_name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    event_date = models.DateField()
    location = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event'

class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    volunteer = models.ForeignKey('Volunteer', models.DO_NOTHING)
    event = models.ForeignKey(Event, models.DO_NOTHING)
    rating = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    date_submitted = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback'

class Organization(models.Model):
    org = models.OneToOneField('Verification', models.DO_NOTHING, primary_key=True)
    org_name = models.CharField(max_length=150)
    ceo_name = models.CharField(max_length=100)
    contact_email = models.CharField(unique=True, max_length=100)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    headoffice_address = models.TextField(db_column='headOffice_address')  # Field name made lowercase.
    org_type = models.CharField(max_length=11)

    def _str_(self):
        return self.org_name

    class Meta:
        managed = False
        db_table = 'organization'

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    org = models.ForeignKey(Organization, models.DO_NOTHING)
    event = models.ForeignKey(Event, models.DO_NOTHING)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task'

class Verification(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=255)
    position = models.CharField(max_length=17)

    class Meta:
        managed = False
        db_table = 'verification'

class Volunteer(models.Model):
    volunteer = models.OneToOneField(Verification, models.DO_NOTHING, primary_key=True)
    full_name = models.CharField(max_length=150)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    cnic = models.CharField(db_column='CNIC', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    score = models.IntegerField(default=0)  # Add the score field with a default value.

    class Meta:
        managed = True
        db_table = 'volunteer'


class VolunteerTask(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=50, 
        choices=[('Assigned', 'Assigned'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], 
        default='Assigned'
    )

    class Meta:
        db_table = 'volunteertask'



from django.db import models

# Assuming that you have the models for Task, Volunteer, Event, and Organization
from django.db import models

    
from django.db import models



class TaskSubmission(models.Model):
    # Foreign key relationships
    task = models.ForeignKey('Task', on_delete=models.CASCADE, db_column='task_id')
    event = models.ForeignKey('Event', on_delete=models.CASCADE, db_column='event_id')
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, db_column='org_id')
    user = models.ForeignKey('Verification', on_delete=models.CASCADE, db_column='user_id')
    
    # Optional: Timestamp for when the task submission was made
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    # String representation for easier identification
    def __str__(self):
        return f"Task {self.task.title} submitted for Event {self.event.event_name}"
    
    class Meta:
        db_table = 'task_submissions'  # Custom table name to store task submissions
        managed = True  # Allow Django to manage the database schema (create, update, etc.)


# models.py in 'myapp'
from django.db import models

class EmailQueue(models.Model):
    queue_id = models.AutoField(primary_key=True)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, null=True, blank=True)  # Make it optional
    task_id = models.IntegerField()  # Assuming the task_id is just an integer
    email_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"EmailQueue {self.queue_id} for Volunteer {self.volunteer_id if self.volunteer else 'None'}"
