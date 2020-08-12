from django import forms
from stories.models import Contact,EmailSub,Story,Comments
from django.forms import TextInput

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        widgets={
            'username':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Your name',
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'Email',
            }),
            'subject':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Subject',
            }),
            'message':forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Message',
            })
        }

class EmailForm(forms.ModelForm):
    class Meta:
        model=EmailSub
        fields='__all__'
        widgets={
           'subemail':forms.EmailInput(attrs={
            'class':'form-control',
            'placeholder':'Enter email address',
           })
       }

class StoryForm(forms.ModelForm):
     
    class Meta:
        model=Story
        fields = (
            'title',
            'image',
            'long_description',
            'tags',
            'category',
            'author',
        )
        widgets={
            'title':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Title',
            }),
            'long_description':forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Long Description',
            }),
           
            'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Category',
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields='__all__'
        widgets=({
            'comment_msg':forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Message',
                
            }),
            'user': forms.TextInput(attrs={'readonly': 'readonly'}),
        })
    def update(self, request,user):
        if request.method == "POST":
            form=CommentForm({'user': request.user})
            if form.is_valid():
                user = request.user
                form.save()
                return redirect('/')
            else:
                return redirect('/recipes')