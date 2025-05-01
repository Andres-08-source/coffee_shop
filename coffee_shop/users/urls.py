from django.contrib.auth.views import LoginView
from django.urls import path
from . import views  # asegúrate de importar tus vistas

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/', views.register, name='register'),  
]
