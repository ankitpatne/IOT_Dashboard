from django.shortcuts import render, get_object_or_404
from .models import Station, SensorData
from .filters import StationFilter
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Count
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('station_list')
        else:
            # Pass the form back to the template with the entered data and errors
            form = UserCreationForm(request.POST)
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('station_list')
        else:
            # Pass the form back to the template with the entered data
            form = AuthenticationForm(request, data=request.POST)
            return render(request, 'registration/login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

# logout view
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def station_list(request):
    filter = StationFilter(request.GET, queryset=Station.objects.all())
    stations = filter.qs

    # Count active and inactive stations
    station_status = stations.values('status').annotate(total=Count('status'))
    active_stations = next((item for item in station_status if item["status"] == "active"), {}).get('total', 0)
    inactive_stations = next((item for item in station_status if item["status"] == "inactive"), {}).get('total', 0)

    paginator = Paginator(stations.order_by('-last_seen'), 10)  # Order by latest last seen time
    page_number = request.GET.get('page')
    
    # Get the Page object for the current page
    stations_page = paginator.get_page(page_number)

    return render(request, 'dashboard/list.html', {
        'stations': stations_page, 
        'filter': filter,
        'active_stations': active_stations,
        'inactive_stations': inactive_stations,
        'total_stations': active_stations + inactive_stations,
    })

def station_detail(request, pk):
    station = Station.objects.get(pk=pk)
    sensor_data = SensorData.objects.filter(station=station).order_by('-timestamp')[:10]
    return render(request, 'dashboard/detail.html', {'station': station, 'sensor_data': sensor_data})



def station_data(request, pk):
    station = get_object_or_404(Station, pk=pk)
    sensor_data = SensorData.objects.filter(station=station).order_by('-timestamp')[:10]
    data = [{'timestamp': data.timestamp, 'temperature': data.temperature, 'humidity': data.humidity} for data in sensor_data]
    return JsonResponse(data, safe=False)

