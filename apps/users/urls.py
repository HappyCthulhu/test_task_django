from rest_framework.routers import SimpleRouter

from apps.users.models.user import UsersViewSet

router = SimpleRouter()
router.register(r'users', UsersViewSet, basename='users')

urlpatterns = router.urls # type: ignore # noqa: PGH003
