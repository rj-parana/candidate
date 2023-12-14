from django.db import models
import uuid

honorific = [('Mr', 'Mr'), ('Ms', 'Ms'), ('Mrs', 'Mrs')]
gender = [('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender'), ('Other', 'Other')]
level = [('School', 'School'), ('College', 'College'), ('University', 'University'), ('Institute', 'Institute')]
status = [('Active', 'Active'), ('Inactive', 'Inactive'), ('Delete', 'Delete')]


class PersonalDetails(models.Model):
    # uid = models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    id = models.AutoField(primary_key=True, editable=False)
    honorific = models.CharField(max_length=8, choices=honorific, default='Mr')
    f_name = models.CharField(max_length=40, null=False)
    l_name = models.CharField(max_length=40, null=True)
    gender = models.CharField(max_length=20, choices=gender, default='Male')
    dob = models.DateField(null=True)
    email = models.EmailField(null=False, unique=True)
    country_code = models.CharField(max_length=5, null=True)
    mobile = models.CharField(max_length=15, null=True)
    country = models.CharField(max_length=40, null=True)
    state = models.CharField(max_length=40, null=True)
    city = models.CharField(max_length=40, null=True)
    address = models.CharField(max_length=200, null=True)
    pin_code = models.CharField(max_length=10, null=True)
    skills = models.CharField(max_length=400, null=True)
    hobbies = models.CharField(max_length=400, null=True)
    interests = models.CharField(max_length=400, null=True)
    image = models.ImageField(upload_to = 'Candidate', null=True)

    class Meta:
        verbose_name_plural = "Personal Details"

    def __str__(self):
        return self.email

class EducationDetails(models.Model):
    personal_detail = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE, blank=True)
    level= models.CharField(max_length=40, choices=level, default='School')
    school_name = models.CharField(max_length=400, null=True)
    course = models.CharField(max_length=100, null=True)
    year_of_passing = models.CharField(max_length=20, null=True)
    complited = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Education Details"

    def __str__(self):
        return self.school_name