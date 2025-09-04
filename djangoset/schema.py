import graphene
from graphene_django import DjangoObjectType
from shop.models import Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "category_name", "category_desc", "category_photo")


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    def resolve_categories(root, info):
        return Category.objects.all()


schema = graphene.Schema(query=Query)
