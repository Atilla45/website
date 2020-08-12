from django.shortcuts import render,redirect,reverse
from stories.models import Recipe,Category,Story,EmailSub,Contact,Comments
from datetime import datetime
from stories.forms import ContactForm,EmailForm,StoryForm,CommentForm
from django.contrib import messages
from django.views.generic import CreateView,ListView,DetailView
from stories.tasks import dump_celery
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin





# Create your views here.
def home(request):
    stories=Story.objects.all().order_by('-created_at')[:4]
    recipes=Recipe.objects.all().order_by('-created_at')[:2]
    form=EmailForm()
    if request.method=='POST':
        form=EmailForm(data=request.POST)
        if form.is_valid():
            print('okkkkkkk')
            form.save()
            messages.success(request,'Bildirişiniz qeydə alındi.Bizi seçdiyiniz üçün təşəkkürlər!')
            return redirect('/')
    else:
        form=EmailForm() 
    contex={
        'stories':stories,
        'recipes':recipes,  }
    return render(request,'index.html',contex)

def about(request):
    return render(request,'about.html')



def dump_celery(request):
    return render(request,'dump_celery.html')


class Create_StoryView(CreateView):
    template_name='create_story.html'
    success_url='/'
    form_class=StoryForm
    
    def form_valid(self, form):
        story = form.save(commit=False)
        story.author = self.request.user
       
        story.save()
        return super().form_valid(form)


class ContactView(CreateView):
    model=Contact
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/'
    def form_valid(self,*args,**kwargs):
        messages.success(self.request,'Bildirişiniz qeydə alındi.Bizi seçdiyiniz üçün təşəkkürlər!')
        return super().form_valid(*args,**kwargs)


class StoryList(ListView):
    model=Story
    template_name='stories.html'
    paginate_by = 3
    context_object_name='stories'




# def recipes(request):
#     recipe_list=Recipe.objects.all()
#     myDate = datetime.now()
#     formatedDate = myDate.strftime('%b %d, %Y')
#     contex={
#         'date': formatedDate,
#         'recipes':recipe_list
#     }
#     return render(request,'recipes.html',contex)
class RecipeList(ListView):
    model=Recipe
    template_name='recipes.html'
    paginate_by = 2
    context_object_name='recipes'


class RecipeDetails(FormMixin,DetailView,):
    model=Recipe
    template_name='single.html'
    context_object_name='recipe'
    form_class=CommentForm

    def get_success_url(self):
        return reverse("home")

    def get_context_data(self, **kwargs):
        context = super(RecipeDetails, self).get_context_data(**kwargs)
        context["forms"] = self.get_form()
        recipe=self.object
        context['comments'] = recipe.comments.filter(parent_msg__isnull=True)
        
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        print(self.request.user)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self,form):
        user=self.request.user
        print(user)
        form.instance.user=user
        form.save()
        return super().form_valid(form)



    # def update(self, request,user):
    #     if request.method == "POST":
    #         form=CommentForm({'user': request.user})
    #         if form.is_valid():
    #             user = request.user
    #             form.save()
    #             return redirect('/')
    #         else:
    #             return redirect('/recipes')

    
   


class UserProfile(ListView,LoginRequiredMixin):
    model=Recipe
    template_name='user-profile.html'
    
    def get_queryset(self):
        user=self.request.user
        queryset=super().get_queryset()
        return queryset.filter(author=user)


class Comment_Mixin(DetailView,):
    model=Comments
