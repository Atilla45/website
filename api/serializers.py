from rest_framework import serializers
from stories.models import Recipe, Category,EmailSub,Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta():
        model=Tag
        fields=(
            'id',
            'title',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model=Category
        fields=(
            'id',
            'title',
            'image',
        )

class ReadRecipeSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    tags=TagSerializer()
    class Meta():
        model=Recipe
        fields=(
            'id',
            'title',
            'image',
            'short_description',
            'category',
            'author',
            'tags',
        )

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields=(
            'title',
            'image',
            'short_description',
            'category',
            'author',
            'tags',
        )


class EmailSubSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmailSub
        fields=(
            'subemail',
            'created_at',
            'updated_at',

        )