from django.forms import ValidationError
from rest_framework.generics import GenericAPIView

from my_library.api.serializers import BookSerializer, AuthorSerializer, CategorySerializer, CategoryAuthorSerializer, UserSerializer
from rest_framework import generics
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from my_library.models import Book,  Author, Category, User
from rest_framework.generics import get_object_or_404
from rest_framework import permissions, filters, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter #search ile filtrelemek için
from my_library.api.authentication import create_access_token, create_refresh_token, decode_refresh_token, decode_access_token
from rest_framework.exceptions import ValidationError  ### HTTP 400 Döndürebilmemiz için bunu import etmeyi unutmayalım
from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import AuthenticationFailed


class Register(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginAPIView(APIView):
    serializer_class = UserSerializer
    def post(self, request):
        email=request.data['email']
        password=request.data['password']

        user=User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')


        access_token =create_access_token(user.id)
        refresh_token =create_refresh_token(user.id)

        response= Response()

        response.set_cookie(key='refreshToken',value=refresh_token,httponly=True)

        response.data={
            'token':access_token
        }

        return response


class UserAPIView(APIView):

    def get(self,request):
        auth=get_authorization_header(request).split()

        if auth and len(auth)==2:
            token=auth[1].decode('utf-8')
            id=decode_access_token(token)

            user= User.objects.filter(pk=id).first()

            return Response(UserSerializer(user).data)

        raise AuthenticationFailed('unauthenticated')


class RefreshAPIView(APIView):
      def post(self, request):
        refresh_token= request.COOKIES.get('refreshToken')
        id=decode_refresh_token(refresh_token)
        access_token=create_access_token(id)
        return Response({
            'token':access_token
        })


class LogoutAPIView(APIView):
    def post(self, request):
        response=Response()
        response.delete_cookie(key='refreshToken')
        response.data={
            'message':'success'
        }
        return response

class BookListCreateAPIView(generics.ListCreateAPIView):  # list kullanmazsak geti getirmez
        queryset = Book.objects.all()
        serializer_class = BookSerializer
       #  permission_classes = [IsAdminUserOrReadOnly]
class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Book.objects.all()
        serializer_class = BookSerializer
       # permission_classes = [IsAdminUserOrReadOnly]



class AuthorListCreateAPIView(generics.ListCreateAPIView):  # list kullanmazsak geti getirmez
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends=[SearchFilter]#birden fazla filtreleme ekleyebilirim
    search_fields=['surname']#birden fazla alan ekleyebiliriz, kitap modelinden

class AuthorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
 
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 

class CategoryBooksView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "category"

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        return self.queryset.filter(category=category_id)


class CategoryAuthorsView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = "category"

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        return self.queryset.filter(category=category_id)

class CategoryAuthorView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = CategoryAuthorSerializer
    lookup_field = "category"

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        return self.queryset.filter(category=category_id)