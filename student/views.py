from django.shortcuts import render
from django.http import HttpResponseRedirect

students = {
    101: {'name': 'Alice', 'roll_number': 101, 'department': 'Computer Science', 'year': 1},
    102: {'name': 'Bob', 'roll_number': 102, 'department': 'IT', 'year': 2},
    103:{'name': 'Ram', 'roll_number': 103, 'department': 'ECE', 'year': 3},
    104:{'name': 'Rohit', 'roll_number': 104, 'department': 'Mechanical', 'year': 4}
}

def student_profile(request, roll_number):
    student = students.get(roll_number)
    if not student:
        return render(request, '404.html', status=404)
    return render(request, 'student_profile.html', {'student': student})

def subjects_list(request):
    subjects = ['AI', 'DBMS', 'Networking']
    return render(request, 'subjects.html', {'subjects': subjects})

def feedback_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Normally save to DB, we'll just print/log for now
        print(f'Feedback from {name}: {message}')
        return render(request, 'thank_you.html', {'name': name})
    return render(request, 'feedback_form.html')
