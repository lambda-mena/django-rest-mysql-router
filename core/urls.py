from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.authentication.views import SignUp
from django.urls import path, include

urlpatterns = [
    path("api/", include("apps.tasks.urls")),
    path("api/auth/sign-up/", SignUp.as_view(), name="sign_up"),
    path("api/auth/sign-in/", TokenObtainPairView.as_view(), name="sign_in"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
