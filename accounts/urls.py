from django.urls import path
from .forms import LoginForm
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', authentication_form=LoginForm),
         name='login'),
    path('logout/', views.logout_view, name='logout')
]
