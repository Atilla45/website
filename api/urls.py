from django.urls import path,include
from api.views import recipes,recipe_detail
from api.routers import router

urlpatterns = [
   
    path('recipes/', recipes, name='api_recipes'),   
    path('recipe_detail/<int:id>',recipe_detail, name='api_recipe_detail')
] + router.urls