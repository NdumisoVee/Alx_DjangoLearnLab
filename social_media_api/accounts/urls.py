from django.urls import path,include
from .views import RegisterView, LoginView, UserViewSet
from django.contrib import admin
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('', include(router.urls)),

]