from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views  # asegúrate de importar tus vistas

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/', views.register, name='register'),  
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

]
