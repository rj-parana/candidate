from django import forms
from .models import PersonalDetails, EducationDetails

class PersonalDetailsForm(forms.Form):

    class Meta:
        model = PersonalDetails
        fields: '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            if visible.field.required:
                visible.field.widget.attrs['class'] = 'form-control required-cls'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

class EducationDetailsForm(forms.Form):

    class Meta:
        model = EducationDetails
        fields: '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            if visible.field.required:
                visible.field.widget.attrs['class'] = 'form-control required-cls'
            else:
                visible.field.widget.attrs['class'] = 'form-control'
