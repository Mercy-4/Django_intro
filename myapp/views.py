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