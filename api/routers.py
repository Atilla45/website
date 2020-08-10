from rest_framework.routers import DefaultRouter
from api.viewsets import RecipeViewSet,EmailSubViewSet

router=DefaultRouter()
router.register('recipe',RecipeViewSet)
router.register('emailsub',EmailSubViewSet)
