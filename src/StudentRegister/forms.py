from django import forms
from .models import Student

Grade = [
    ('Grade', ('Grade')),
     ('A', ('A')),
    ('B', ('B')),
    ('C', ('C')),
    ('D', ('D')),
    ('E', ('E')),
    ('F', ('F')),
]

Faculty = [
    ('Faculty', ('Faculty')),
    ('Faculty Of Engineering', ('Faculty Of Engineering')),
]

Department = [
    ('Department', ('Department')),
    ('Department of Electrical & Electronic Engineering', ('Department of Electrical & Electronic Engineering')),
    ('Department of Electrical & Computer Engineering', ('Department of Electrical & Computer Engineering')),
    ('Department of Mechanical Engineering', ('Department of Mechanical Engineering')),
    ('Department of Telecommunications Engineering', ('Department of Telecommunications Engineering')),
    ('Department of Civil & Structural Engineering', ('Department of Civil & Structural Engineering')),
    ('Department of Mechatronics Engineering', ('Department of Mechatronics Engineering')),
    ('Department of Marine Engineering', ('Department of Marine Engineering')),
]

Course = [
    ('Course', ('Course')),
    ('Bsc. Electrical & Electronic Eng.', ('Bsc. Electrical & Electronic Eng.')),
    ('Bsc. Electrical & Computer Eng.', ('Bsc. Electrical & Computer Eng.')),
    ('Bsc. Mech. Eng.', ('Bsc. Mech. Eng.')),
    ('Bsc. Telecom Eng.', ('Bsc. Telecom Eng.')),
    ('Bsc. Civil & Structural Eng.', ('Bsc. Civil & Structural Eng.')),
    ('Bsc. Mechatronics Eng.', ('Bsc. Mechatronics Eng.')),
    ('Bsc. Marine Eng.', ('Bsc. Marine Eng.')),
]

Year = [
    ('Year Of Study', ('Year Of Study')),
    ('1st Year', ('1st Year')),
    ('2nd Year', ('2nd Year')),
    ('3rd Year', ('3rd Year')),
    ('4th Year', ('4th Year')),
    ('5th Year', ('5th Year')),
]

Units = [
    ('Unit', ('Unit')),
    ('Calculus', ('Calculus')),
    ('Complex Analysis', ('Complex Analysis')),
    ('Control Eng.', ('Control Eng.')),
    ('Economics', ('Economics')),
    ('Accounitng & Finance', ('Accounting & Finance')),
    ('Algebra', ('Algebra')),
]

class DateInput(forms.DateInput):
    input_type = 'date'

class StudentForm(forms.ModelForm):
    Admission_Number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Admission Number",
                "class": "form-control",
            }
        )
    )
    First_Name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "First Name",
                "class": "form-control",
            }
        )
    )
    Last_Name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Last Name",
                "class": "form-control",
            }
        )
    )
    Date_Of_Birth = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(
            attrs={
                "placeholder" : "Date Of Birth",
                "class": "form-control",
            }
        )
    )
    Date_Joined = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeholder" : "Date Joined",
                "class": "form-control",
            }
        )
    )
    Faculty = forms.CharField(
        widget=forms.Select(
            choices= Faculty,
            attrs={
                "placeholder" : "Faculty",
                "class": "form-control",
            }
        )
    )
    Department = forms.CharField(
        widget=forms.Select(
            choices= Department,
            attrs={
                "placeholder" : "Department",
                "class": "form-control",
            }
        )
    )
    Course_Name = forms.CharField(
        widget=forms.Select(
            choices= Course,
            attrs={
                "placeholder" : "Course Name",
                "class": "form-control",
            }
        )
    )
    Year_Of_Study = forms.CharField(
        widget=forms.Select(
            choices=Year,
            attrs={
                "placeholder" : "Year Of Study",
                "class": "form-control",
            }
        )
    )
    Unit_Name = forms.CharField(
        widget=forms.Select(
            choices= Units,
            attrs={
                "placeholder" : "Unit Name",
                "class": "form-control",
            }
        )
    )
    Grade = forms.CharField(
        widget=forms.Select(
            choices= Grade,
            attrs={
                "placeholder" : "Grade",
                "class": "form-control",
            }
        )
    )

    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'Date_Of_Birth': DateInput(),
            'Date_Joined': DateInput(),
        }