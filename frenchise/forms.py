from django import forms
from django.contrib.auth.models import User
from .models import frenchise_register_model, frenchise_employee_register_model
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField,  PasswordChangeForm, PasswordResetForm, SetPasswordForm


COUNTRY_CHOICES = (
    ('Indian', 'Indian'),
    ('Other', 'Other')
)
EducationSelect = (
    ('Graduate', 'Graduate'),
    ('Post Graduate', 'Post Graduate'),
    ('Undergraduate', 'Undergraduate'),
    ('Other', 'Other'),
)
OccupationSelect = (
    ('Job', 'Job'),
    ('Seeker', 'Seeker'),
    ('Self Employed', 'Self Employed'),
    ('Freelancer', 'Freelancer'),
    ('Other', 'Other'),
)

CITY_CHOICE = (
    ('Agra', 'Agra'),
    ('Aligarh', 'Aligarh'),
    ('Allahabad', 'Allahabad'),
    ('Ambedkar Nagar', 'Ambedkar Nagar'),
    ('Amethi', 'Amethi'),
    ('Amroha', 'Amroha'),
    ('Auraiya', 'Auraiya'),
    ('Azamgarh', 'Azamgarh'),
    ('Baghpat', 'Baghpat'),
    ('Bahraich', 'Bahraich'),
    ('Ballia', 'Ballia'),
    ('Balrampur', 'Balrampur'),
    ('Banda', 'Banda'),
    ('Barabanki', 'Barabanki'),
    ('Bareilly', 'Bareilly'),
    ('Basti', 'Basti'),
    ('Bhadohi', 'Bhadohi'),
    ('Bijnor', 'Bijnor'),
    ('Budaun', 'Budaun'),
    ('Bulandshahr', 'Bulandshahr'),
    ('Chandauli', 'Chitrakoot'),
    ('Deoria', 'Deoria'),
    ('Etah', 'Etah'),
    ('Etawah', 'Etawah'),
    ('Faizabad', 'Faizabad'),
    ('Farrukhabad', 'Farrukhabad'),
    ('Fatehpur', 'Fatehpur'),
    ('Firozabad', 'Firozabad'),
    ('Gautam Buddha Nagar', 'Gautam Buddha Nagar'),
    ('Ghaziabad', 'Ghaziabad'),
    ('Ghazipur', 'Ghazipur'),
    ('Gonda', 'Gonda'),
    ('Gorakhpur', 'Gorakhpur'),
    ('Hamirpur', 'Hamirpur'),
    ('Hapur', 'Hapur'),
    ('Hardoi', 'Hardoi'),
    ('Hathras', 'Hathras'),
    ('Jalaun', 'Jalaun'),
    ('Jaunpur', 'Jaunpur'),
    ('Jhansi', 'Jhansi'),
    ('Kannauj', 'Kannauj'),
    ('Kanpur Dehat', 'Kanpur Dehat'),
    ('Kanpur Nagar', 'Kanpur Nagar'),
    ('Kanshiram Nagar', 'Kanshiram Nagar'),
    ('Kaushambi', 'Kaushambi'),
    ('Kushinagar', 'Kushinagar'),
    ('Lakhimpur ', 'Lakhimpur '),
    ('Lalitpur', 'Lalitpur'),
    ('Lucknow', 'Lucknow'),
    ('Maharajganj', 'Maharajganj'),
    ('Mahoba', 'Mahoba'),
    ('Mainpuri', 'Mainpuri'),
    ('Mathura', 'Mathura'),
    ('Mau', 'Mau'),
    ('Meerut', 'Meerut'),
    ('Mirzapur', 'Mirzapur'),
    ('Moradabad', 'Moradabad'),
    ('Muzaffarnagar', 'Muzaffarnagar'),
    ('Pilibhit', 'Pilibhit'),
    ('Pratapgarh', 'Pratapgarh'),
    ('RaeBareli', 'RaeBareli'),
    ('Rampur', 'Rampur'),
    ('Saharanpur', 'Saharanpur'),
    ('Sambhal ', 'Sambhal '),
    ('Sant Kabir Nagar', 'Sant Kabir Nagar'),
    ('Shahjahanpur', 'Shahjahanpur'),
    ('Shamali ', 'Shamali '),
    ('Shravasti', 'Shravasti'),
    ('Siddharth Nagar', 'Siddharth Nagar'),
    ('Sitapur', 'Sitapur'),
    ('Sonbhadra', 'Sonbhadra'),
    ('Sultanpur', 'Sultanpur'),
    ('Unnao', 'Unnao'),
    ('Varanasi', 'Varanasi')
               
)
#Agent Registration Form
class FrenchiseRegistrationForm(UserCreationForm):
    number = forms.IntegerField()
    State = forms.CharField(label='State',max_length="100")
    Occupation = forms.ChoiceField(
        label="Select Your Occupation",
        choices=OccupationSelect,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    city = forms.CharField(label='City',max_length="100")
    Education = forms.ChoiceField(label="Select Your Education", choices=EducationSelect, required=True,widget=forms.Select(attrs={'class':"form-control"}))
    DOB = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date'}),)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':"form-control"}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':"form-control"}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':"form-control"}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2','number','State','city','Education','Occupation','DOB']
        label = {'email':'Email'}
        widget = {'username':forms.TextInput(attrs={'class':'form-control'})}






#Login Form
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs=
        {'autocomplete':'current-password', 'class':'form-control'}))
    

#customer personal information
class frenchise_application_form(forms.ModelForm):
    class Meta:
        model = frenchise_register_model
        fields = ['frenchise_name','DOB','gender','city','Pin_code','Work_Type','Address_Type']

   
        widgets = { 'frenchise_name':forms.TextInput(attrs={'class':'form-control'}),
                'DOB':forms.TextInput(attrs={'class':'form-control'}),
                'gender':forms.TextInput(attrs={'class':'form-control'}),
                'Age':forms.TextInput(attrs={'class':'form-control'}),
                'Pin_code':forms.TextInput(attrs={'class':'form-control'}),
                'Work_Type':forms.Select(attrs={'class':'form-control'}),
                'Address_Type':forms.Select(attrs={'class':'form-control'}),


            }
        

#Employee Forms

class Employee_application_form(forms.ModelForm):
    class Meta:
        model = frenchise_employee_register_model
        fields = ['employee_id', 'email', 'username','password']

   
        widgets = { 'username':forms.TextInput(attrs={'class':'form-control'}),
                'password':forms.TextInput(attrs={'class':'form-control'}),
              
            }


#Change Password Form
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=('Old Password'),strip=False, widget=forms.PasswordInput
        (attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))

    new_password1 = forms.CharField(label=('New Password'),strip=False, widget=forms.PasswordInput
        (attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.
        password_validators_help_text_html())

    new_password2 = forms.CharField(label=('Confirm New Password'),strip=False, widget=forms.PasswordInput
        (attrs={'autocomplete':'new-password','class':'form-control'}))


# Reset Password Form
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=('Email'),max_length=255, widget=forms.EmailInput
        (attrs={'autocomplete':'email','class':'form-control'}))



#Confirm Reset Password Form
class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=('New Password'),strip=False, widget=forms.PasswordInput
        (attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.
        password_validators_help_text_html())
    new_password2 = forms.CharField(label=('Confirm New Password'),strip=False, widget=forms.PasswordInput
        (attrs={'autocomplete':'new-password','class':'form-control'}))
