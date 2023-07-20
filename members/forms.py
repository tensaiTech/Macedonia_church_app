from django import forms
from .models import Member, MARITAL_STATUS, GENDER_CHOICES


class MemberForm(forms.ModelForm):
    gender = forms.CharField(widget=forms.Select(choices=(('', 'Select Your Gender'),) + GENDER_CHOICES))
    marital_status = forms.CharField(
        widget=forms.Select(choices=(('', 'Select Your Marital Status'),) + MARITAL_STATUS))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    year_of_marriage_registered = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Member
        fields = ['full_name', 'gender', 'phone', 'email', 'date_of_birth', 'place_of_birth', 'hometown', 'occupation',
                  'educational_background', 'house_number', 'residental_area', 'residental_street', 'father_name',
                  'father_hometown', 'mother_name', 'mother_hometown', 'former_assembly', 'former_district',
                  'former_region_of_district_assembly', 'place_of_baptism', 'baptismal_officiating_minister', 'zone',
                  'marital_status', 'marital_officiating_minister', 'place_of_marriage', 'year_of_marriage_registered',
                  'name_of_partner', 'name_of_denomination_of_partner', 'partner_hometown']
