from django.contrib import admin
from django.urls import path
from app_1.views import plans, delete_plan, register, LoginView, LogoutView

urlpatterns = [
    path('', LoginView, name='login'),
    path('register/', register, name='reg'),
    path('admin/', admin.site.urls),
    path('plans/', plans, name='ToDo'),
    path('plans/<int:num>/',  delete_plan),
    path('logout/', LogoutView, name='logout')
]
