from django.urls import path,include
from .views import RegisterView, LoginView, UserViewSet
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import FollowUserView, UnfollowUserView


router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('', include(router.urls)),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),

]