from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.authentication.views.avatar import avatar
from apps.authentication.views.registration import RegisterView
from apps.authentication.views.user import UserRetrieveUpdateAPIView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name="sign_up"),
    path('user/', UserRetrieveUpdateAPIView.as_view(), name='retrieve_or_update_user'),
    path('user/avatar/', avatar, name='avatar'),
]
