from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Author

# Create your views here.

def index(request):
    return HttpResponse("Welcome to home")

def greet(request):
    # print(request.GET['docid'])
    # print(request.GET['ln'])
    request.session['visited'] = 'yes'
    return render(request, 'blog/greet.html')

def greet_person(request, name):
    return render(
        request,
        'blog/greet_person.html',
        context={
            'myvar': name + request.session.get('visited', 'no'),
            'myrange': range(5)
        }
    )


def myform(request):
    print(request.method)
    if request.method == 'GET':
        return render(
            request, 
            'blog/my_form.html',
            context={
                'authors': Author.objects.all()
            }
        )
    name = request.POST['name']
    a = Author(name=name)
    a.save()
    return HttpResponse("Author Created Successfully")
