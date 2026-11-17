<<<<<<< HEAD
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404

from myapp.models import Book
from myapp.my_forms import BookForm, RegisterForm


# Create your views here.

@login_required
def show_books(request):
    books = Book.objects.all()
    return render(request, 'show_books.html', {'books': books})

@login_required()
@permission_required('myapp.add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Book {request.POST.get('title')} Successfully')
            return redirect('show_books')
            return redirect('show_books')
    else:
        form = BookForm(request.POST)
    return render(request, 'add_book.html', {'form': form})

    # Book.objects.create(title='River and the Source',
    #                     year=2021,
    #                     category='Fiction',
    #                     cost=600,
    #                     isbn= '34567890',
    #                     published=True)
    # Book.objects.create(title='Kidagaa KImemuozea',
    #                     year=2018,
    #                     category='Politics',
    #                     cost=780,
    #                     isbn= '34678998',
    #                     published=True)

@login_required()
@permission_required('myapp.delete_book', raise_exception=True)
def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    messages.error(request, f'{book.title} Deleted Successfully')
    return redirect('show_books')
    return redirect('show_books')

@login_required()
@permission_required('myapp.change_book', raise_exception=True)
def edit_book(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, f'{book.title} Updated Successfully')
            return redirect('show_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})
    return None


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('show_books')
    else:
        form = AuthenticationForm(request)

    return render(request, 'registration/login.html', {'form': form})


def signup(request):
    print("SIGNUP VIEW EXECUTED")

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('signin')

    return render(request, 'registration/signup.html', {'form': form})


@login_required()
def signout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')
=======
from django.shortcuts import render

# Create your views here.
def home(request, is_sunny=None):
    temp = 38.7
    humidity = 12
    wind = 12
    city = "Zanzibar"
    is_sunny = True
    users = ["Jane", "Jack", "Moha"]
    data = {
        'temperature': temp,
        'humidity': humidity,
        'windspeed': wind,
        'city': city,
        'is_sunny': is_sunny,
        'users': users,
    }
    return render(request, 'home.html', data)

def about(request):
    return render(request, template_name='about.html')
def services(request):
    return render(request, template_name='services.html')
def students(request):
    scores = [{"names":"Garth Morton","email":"quam.dignissim.pharetra@outlook.com","score":27,"age":19},{"names":"Emma Short","email":"ipsum.cursus.vestibulum@yahoo.com","score":87,"age":20},{"names":"Kylan Mcpherson","email":"cras@outlook.edu","score":37,"age":25},{"names":"Josephine Roberson","email":"dui.fusce@yahoo.com","score":78,"age":22},{"names":"Urielle Freeman","email":"congue.elit@outlook.net","score":55,"age":25},{"names":"Jasper Perry","email":"dui@icloud.couk","score":28,"age":19},{"names":"Denton Benson","email":"pellentesque.tellus.sem@icloud.ca","score":62,"age":21},{"names":"Quinn Daniels","email":"sed.tortor@protonmail.edu","score":23,"age":23},{"names":"Axel Schwartz","email":"sed@yahoo.net","score":45,"age":24},{"names":"Oprah Landry","email":"faucibus.leo@yahoo.com","score":25,"age":22},{"names":"Keegan Lyons","email":"accumsan.convallis.ante@protonmail.org","score":66,"age":20},{"names":"Cara Shaw","email":"sit.amet@google.couk","score":31,"age":22},{"names":"Olivia Ryan","email":"dictum@icloud.org","score":80,"age":21},{"names":"Lawrence Finley","email":"nunc.sollicitudin.commodo@icloud.net","score":54,"age":22},{"names":"Charles Mccall","email":"nulla@aol.org","score":23,"age":23}]
    data= {"students":scores}
    return render(request, 'students.html', data)

>>>>>>> 354ec5c36c105243fafba5722f18be2f62fbf783
