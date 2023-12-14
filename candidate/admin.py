from django.contrib import admin
from .models import PersonalDetails, EducationDetails

class EducationDetailsInline(admin.StackedInline):
    model = EducationDetails
    extra = 0

class PersonalDetailAdmin(admin.ModelAdmin):
    inlines = [EducationDetailsInline]

admin.site.register(PersonalDetails, PersonalDetailAdmin)
# admin.site.register(EducationDetails)
