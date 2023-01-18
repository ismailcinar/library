from rest_framework import serializers
from my_library.models import Book, Author, Category, User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
      
        
    def create(self, validated_data):
        password= validated_data.pop('password', None)
        instance =self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = '__all__' 

class CategorySerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
   
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'

class CategoryAuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'