from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('users/', views.users, name='users'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)