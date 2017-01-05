from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Courses, CourseUsers
from ..login_registration.models import User
from django.db import connection
from django.db.models import Count

# Create your views here.
#Courses.objects.create(name='Math', description="Who needs to add!!!")
def index(request):
    # course_users = CourseUsers.objects.all()
    course_users = CourseUsers.objects.all().values('course').annotate(total=Count('user')).order_by('total')
    # print course_users.query
    # for assignments in course_users:
    #     print assignments.course.name

    users = User.objects.all()
    courses = Courses.objects.all()

    context = {
        'courses': courses,
        'users': users,
        'course_users': course_users,
        }
    return render(request, "courses_app/index.html",context)
def add(request):
    errors = False
    if request.POST:
        name = request.POST.get("name")
        description = request.POST.get("description")
        if len(name) < 5:
            messages.warning(request, 'The course name needs to be valid (5 minimum characters)') # recorded
            errors = True
        if len(description) < 15:
            messages.warning(request, 'Please add a valid description (15 minimum characters)') # recorded
            errors = True
        if errors:
            messages.warning(request, 'Course has not been saved, satisfy errors and try again')
        else:
            Courses.objects.create(name=name, description=description)
    return redirect('/courses')
def confirm_destroy(request, id):
    course = Courses.objects.get(id=id)
    context = {
        'course': course
    }
    return render(request, "courses_app/remove.html",context)
def destroy(request, id):
    Courses.objects.filter(id=id).delete()
    return redirect('/courses')
def assign_user(request):
    errors = False
    if request.POST:
        if len(request.POST['course']) < 1 or len(request.POST['user']) < 1:
            errors = True
            messages.warning(request, 'Please select a course and user')
        else:
            course = Courses.objects.get(id=int(request.POST['course']))
            user = User.objects.get(id=int(request.POST['user']))
            check_exists = CourseUsers.objects.filter(course=course).filter(user=user)
            if check_exists:
                messages.warning(request, 'This user is already assigned to this course')
            else:
                CourseUsers.objects.create(course=course, user=user)
                messages.info(request, 'Successfully assigned the user to the course')
    return redirect('/courses')
def course_users(request):

    return redirect('/courses')

# def success(request):
#
#     return redirect('/success')
