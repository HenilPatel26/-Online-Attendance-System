from django.shortcuts import render, redirect
from .models import Student, Attendance

def students(request):
    if request.method == 'POST':
        name = request.POST['name']
        Student.objects.create(name=name)
        return redirect('students')

    data = Student.objects.all()
    return render(request, 'students.html', {'students': data})


def mark_attendance(request):
    students = Student.objects.all()

    if request.method == 'POST':
        for student in students:
            status = request.POST.get(str(student.id))
            Attendance.objects.create(
                student=student,
                status=True if status == 'on' else False
            )
        return redirect('records')

    return render(request, 'attendance.html', {'students': students})


def records(request):
    data = Attendance.objects.all().order_by('-date')
    return render(request, 'records.html', {'records': data})

def mark_attendance(request):
    students = Student.objects.all()

    if request.method == 'POST':
        selected_date = request.POST.get('date')

        for student in students:
            status = request.POST.get(str(student.id))
            Attendance.objects.create(
                student=student,
                date=selected_date,  
                status=True if status == 'on' else False
            )

        return redirect('records')

    return render(request, 'attendance.html', {'students': students})