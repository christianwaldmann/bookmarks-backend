from django.urls import path, include
from .views import RegisterView, LoginView, UserView, DeleteView
from knox import views as knox_views


urlpatterns = [
    path('auth', include('knox.urls')),
    path('auth/register', RegisterView.as_view()),
    path('auth/login', LoginView.as_view()),
    path('auth/user', UserView.as_view()),
    path('auth/logout', knox_views.LogoutView.as_view()),
    path('auth/delete', DeleteView.as_view()),
]
