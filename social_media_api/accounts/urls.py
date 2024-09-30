from django.urls import path
from .views import RegisterUserView, LoginUserView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),

]