from rest_framework.routers import SimpleRouter

from apps.users.views.user import UsersViewSet

router = SimpleRouter()
router.register(r'users', UsersViewSet, basename='users')

urlpatterns = router.urls  # type: ignore # noqa: PGH003
