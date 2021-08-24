from django.db import models

# Create your models here.
class Student(models.Model):
    Student_Number = models.IntegerField(verbose_name='Student Number')
    First_Name = models.CharField(max_length=50, verbose_name='First Name')
    Last_Name = models.CharField(max_length=50, verbose_name='Lat Name')
    DOB = models.CharField(max_length=50, verbose_name='Date of Birth')
    Date_Joined = models.DateField(verbose_name='Date Joined')
    Faculty = models.CharField(max_length=50, verbose_name='Faculty')
    Department = models.CharField(max_length=50, verbose_name='Department')
    Course_Name = models.CharField(max_length=50, verbose_name='Course Name')
    Year_Of_Study = models.IntegerField(verbose_name='Year of Study')
    Unit_Name = models.CharField(max_length=50, verbose_name='Unit Name')
    Grade = models.CharField(max_length=50, verbose_name='Grade')

    def __str__(self):
        return self.Student_Number