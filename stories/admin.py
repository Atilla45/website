from django.contrib import admin

# Register your models here.
from stories.models import Recipe,Category,Contact,Story,Tag,Comments

class RecipeAdmin(admin.ModelAdmin):
    list_display=('title','created_at',)
    
admin.site.register(Recipe,RecipeAdmin)
admin.site.register([Category,Contact,Story,Tag])

class CommentsAdmin(admin.ModelAdmin):
    list_display=('comment_msg','story','recipe','created_at',)
admin.site.register(Comments,CommentsAdmin)