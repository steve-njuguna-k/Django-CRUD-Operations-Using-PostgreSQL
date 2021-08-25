from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Student
from .forms import StudentForm

# Create your views here.
def Add_Info(request):
    student = Student.objects.all()
    form = StudentForm()
    if request.method == 'POST':
        context = {'has_error': False}
        Admission_Number = request.POST.get('Admission_Number')
        First_Name = request.POST.get('First_Name')
        Last_Name = request.POST.get('Last_Name')
        Date_Of_Birth = request.POST.get('Date_Of_Birth')
        Date_Joined = request.POST.get('Date_Joined')
        Faculty = request.POST.get('Faculty')
        Department = request.POST.get('Department')
        Course_Name = request.POST.get('Course_Name')
        Year_Of_Study = request.POST.get('Year_Of_Study')
        Unit_Name = request.POST.get('Unit_Name')
        Grade = request.POST.get('Grade')

        student = Student.objects.create(Admission_Number=Admission_Number, First_Name=First_Name, Last_Name=Last_Name,
        Date_Of_Birth=Date_Of_Birth, Date_Joined=Date_Joined, Faculty=Faculty, Department=Department, 
        Course_Name=Course_Name, Year_Of_Study=Year_Of_Study, Unit_Name=Unit_Name, Grade=Grade).save()

        if not context['has_error']:
            messages.success(request, '✅ Student Info Successfully Added!')
            return redirect('Index')
        
        else:
            messages.error(request, '⚠️ Student Info Unsuccessfully Added!')
            return redirect('Index')
    
    context = {'student': student, 'form': form}  
    return render(request, 'Index.html', context)
