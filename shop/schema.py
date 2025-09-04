import graphene
from djangoset.types import CategoryType, TeaItemsType
from shop.models import Category, TeaItems


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    tea_items = graphene.List(TeaItemsType, category_id=graphene.Int(required=False))

    def resolve_categories(root, info):
        return Category.objects.all()

    def resolve_tea_items(root, info, category_id=None):
        if category_id:
            return TeaItems.objects.filter(item_category_id=category_id)
        return TeaItems.objects.all()
