from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.station_list, name='station_list'),
    path('dashboard/<int:pk>/', views.station_detail, name='station_detail'),
    path('dashboard/data/<int:pk>/', views.station_data, name='station_data'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]