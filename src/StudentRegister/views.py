from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Student
from .forms import StudentForm

# Create your views here.
def Index(request):
    student = Student.objects.all()
    form = StudentForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save()

            messages.success(request, '✅ Student Info Successfully Added!')
            return redirect('Index')
        
        else:
            messages.error(request, '⚠️ Student Info Unsuccessfully Added!')
            return redirect('Index')

    context = {'student': student, 'form': form}
    return render(request, 'Index.html', context)
