from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.home, name='dashboard'),
    path('menu/', views.menu, name='menu'),
    path('scan/', views.scan, name='scan'),
    path('web-protection/', views.web_protection, name='web-protection'),
    path('alerts/', views.alerts, name='alerts'),

    # Password reset flow
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('reset-password/<uidb64>/<token>/', views.reset_password_view, name='reset_password'),
]