"""food_stories URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from stories.views import *
from django.conf import settings
from django.conf.urls.static import static
from django_email_verification import urls as mail_urls
from django.contrib.auth.views import LogoutView
from django.urls import include
from stories.views import UserProfile
urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls,name='administrator'),
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',ContactView.as_view(),name='contact'),
    path('api/v1.0/',include('api.urls')),
    path('stories/',StoryList.as_view(),name='story'),
    path('user-profile/',UserProfile.as_view(),name='user_profile'),
    path('create_story/',Create_StoryView.as_view(),name='create_story'),
    path('recipes/',RecipeList.as_view(),name='recipes'),
    path('single/<int:pk>/',RecipeDetails.as_view(),name='single'),
    path('accounts/',include('accounts.urls')),
    path('email/', include(mail_urls)),
    
    path('dump/',dump_celery,name='dump'),
    path('', include('social_django.urls', namespace='social')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
