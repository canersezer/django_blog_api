from rest_framework import serializers

from .models import Category,Blog



class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = '__all__'
        read_only_fields = ['id']


class BlogSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    class Meta():
        model = Blog
        fields = '__all__'
        read_only_fields =['id','category_name']

    def get_category_name(self,obj):
        return obj.category.name