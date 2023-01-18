from django.urls import path 
from my_library.api import views as api_views
from my_library.api import views


urlpatterns = [
   path('logout/', views.LogoutAPIView.as_view()),
   path('refresh/', views.RefreshAPIView.as_view()),
   path('user/', views.UserAPIView.as_view()),
   path('login/', views.LoginAPIView.as_view()),
   path('register/', views.Register.as_view()),
   path('books/',api_views.BookListCreateAPIView.as_view(), name='book-list' ),
   path('books/<int:pk>', api_views.BookDetailAPIView.as_view(), name='book-info'),
 
   path('authors/', api_views.AuthorListCreateAPIView.as_view(), name='authors-list'),
   path('authors/<int:pk>', api_views.AuthorDetailAPIView.as_view(), name='author-detail'),
   path('category/',api_views.CategoryListCreateAPIView.as_view(), name='category'),
   path('category/<int:pk>/', api_views.CategoryDetailAPIView.as_view(), name='name'),
   path('category/<int:category_id>/books', views.CategoryBooksView.as_view()),
   path('category/<int:category_id>/authors', views.CategoryAuthorsView.as_view()),

]