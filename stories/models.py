from django.db import models
from django.utils import timezone
from accounts.models import UserModel

User=UserModel
# Create your models here.
class Category(models.Model):
    title=models.CharField('Title',max_length=80)
    image=models.ImageField('Şəkil',upload_to='media',null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name='Kateqoriya'
        verbose_name_plural='Kateqoriyalar'


    def  __str__(self):
        return f"{self.title}"




class Recipe(models.Model):
    title=models.CharField(max_length=80,unique=True)
    image=models.ImageField(upload_to='recipes')
    short_description=models.TextField(max_length=1000)
    long_description=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    

    # @property
    # def get_comment():
    #     def _get_comment(self,recipe):
        
    #         return recipe
    #     return dict(get_comment=_get_comment)
    class Meta:
        verbose_name='Resept'
        verbose_name_plural='Reseptlər'
        ordering='created_at',

    def __str__(self):
        return self.title

    @property
    def get_comment(self,recipe):
        return '12'

class Contact(models.Model):
    username=models.CharField('Username',max_length=60)
    email=models.EmailField('Email',max_length=100)
    subject=models.CharField('Subject',max_length=105)
    message=models.TextField('Message')
    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Contact'
        verbose_name_plural='Contacts'
        
    def __str__(self):
        return self.username


class Tag(models.Model):
    title=models.CharField('Title', max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)



class Story(models.Model):
    title=models.CharField('Basliq',max_length=255)
    image=models.ImageField(upload_to='stories')
    long_description=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='stories')
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='stories')
    tags=models.ManyToManyField(Tag,related_name='story')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name='Hekaye'
        verbose_name_plural='Hekayeler'
    
    def __str__(self):
        return self.title


class EmailSub(models.Model):
    subemail=models.EmailField(unique=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE,related_name='comments',null=True, blank=True)
    story=models.ForeignKey(Story,on_delete=models.CASCADE,related_name='comments',null=True, blank=True)
    comment_msg=models.TextField('Comment', max_length=1001)
    parent_msg=models.ForeignKey('self',on_delete=models.CASCADE,related_name='comments',null=True, blank=True)


    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    
