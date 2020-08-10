from stories.models import Recipe,EmailSub
from api.serializers import RecipeSerializer,ReadRecipeSerializer,EmailSubSerializer
from  rest_framework.status import HTTP_201_CREATED
from django.contrib.messages.views import SuccessMessageMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet





class RecipeViewSet(ModelViewSet):
    queryset=Recipe.objects.all()
    http_method_names = ['post','get']
    read_serializer_class=ReadRecipeSerializer
    write_serializer_class=RecipeSerializer


class StoryViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticatedForCreate,)
    # serializer_class = StorySerializer
    serializer_classes = {
        'list': ReadRecipeSerializer,
        'retrieve': RecipeSerializer,
        'default': RecipeSerializer,
        # 'create': StorySerializer,
        # 'update': StorySerializer,
        # 'partial_update': StorySerializer,
        # 'delete': StorySerializer
    }
    queryset = Recipe.objects.all()

    def get_serializer_class(self):
        print(self.action)
        return self.serializer_classes.get(self.action, self.serializer_classes.get('default'))


class EmailSubViewSet(ModelViewSet,SuccessMessageMixin):
    queryset=EmailSub.objects.all()
    serializer_class=EmailSubSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        newdict= {"success": 'Email was added successfully'}
        newdict.update(serializer.data)
       
        return Response(newdict, status=HTTP_201_CREATED, headers=headers)