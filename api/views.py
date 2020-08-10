from django.shortcuts import render
from stories.models import Recipe
from api.serializers import RecipeSerializer,ReadRecipeSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED,HTTP_200_OK,HTTP_404_NOT_FOUND,HTTP_204_NO_CONTENT
from rest_framework.decorators import api_view


# Create your views here.

@api_view(('GET','POST'))
def recipes(request):
    if request.method == 'GET':
        recipes=Recipe.objects.all()
        serializer=ReadRecipeSerializer(recipes,many=True, context={'request':request})
        return Response(serializer.data)

    elif request.method=='POST':
        serializer=RecipeSerializer(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return  Response(serializer.data,status=HTTP_201_CREATED)
    
@api_view(('GET','PUT','PATCH','DELETE'))
def recipe_detail(request,id):
    try:
        recipe=Recipe.objects.get(id=id)
    except:
        return Response(status=HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer=ReadRecipeSerializer(recipe, context={'request':request})
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'PUT':
        data = request.data
        serializer=RecipeSerializer(data=data, instance=recipe,  context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'PATCH':
        data = request.data
        serializer=RecipeSerializer(data=data, instance=recipe, partial=True,context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == "DELETE":
        recipe.delete()
        return Response(status=HTTP_204_NO_CONTENT)