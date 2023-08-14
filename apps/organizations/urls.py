from rest_framework.routers import SimpleRouter

from apps.organizations.views import OrganizationViewSet

router = SimpleRouter()
router.register('organization', OrganizationViewSet, basename='organization')


urlpatterns = router.urls
