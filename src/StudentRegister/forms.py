from django import forms
from .models import Student

Grade = [
    ('A', ('A')),
    ('B', ('B')),
    ('C', ('C')),
    ('D', ('D')),
    ('E', ('E')),
    ('F', ('F')),
]

Faculty = [
    ('Faculty Of Engineering', ('Faculty Of Engineering')),
]

Department = [
    ('Department of Electrical & Electronic Engineering', ('Department of Electrical & Electronic Engineering')),
    ('Department of Electrical & Computer Engineering', ('Department of Electrical & Computer Engineering')),
    ('Department of Mechanical Engineering', ('Department of Mechanical Engineering')),
    ('Department of Telecommunications Engineering', ('Department of Telecommunications Engineering')),
    ('Department of Civil & Structural Engineering', ('Department of Civil & Structural Engineering')),
    ('Department of Mechatronics Engineering', ('Department of Mechatronics Engineering')),
    ('Department of Marine Engineering', ('Department of Marine Engineering')),
]

Course = [
    ('Bsc. Electrical & Electronic Engineering', ('Bsc. Electrical & Electronic Engineering')),
    ('Bsc. Electrical & Computer Engineering', ('Bsc. Electrical & Computer Engineering')),
    ('Bsc. Mechanical Engineering', ('Bsc. Mechanical Engineering')),
    ('Bsc. Telecommunications Engineering', ('Bsc. Telecommunications Engineering')),
    ('Bsc. Civil & Structural Engineering', ('Bsc. Civil & Structural Engineering')),
    ('Bsc. Mechatronics Engineering', ('Bsc. Mechatronics Engineering')),
    ('Bsc. Marine Engineering', ('Bsc. Marine Engineering')),
]

Year = [
    x for x in range(1900,2021)
]

Units = [
    ('Calculus', ('Calculus')),
    ('Complex Analysis', ('Complex Analysis')),
    ('Control Engineering', ('Control Engineering')),
    ('Economics', ('Economics')),
    ('Accounitng & Finance', ('Accounting & Finance')),
    ('Algebra', ('Algebra')),
]

class StudentForm(forms.Form):
    Admission_Number = forms.IntegerField(
        widget=forms.NumberInput(
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
    DOB = forms.DateField(
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
    Year_Of_Study = forms.DateField(
        widget=forms.SelectDateWidget(
            years= Year,
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
                "class": "form-cotrol",
            }
        )
    )

    class Meta:
        model = Student
        fields = '__all__'