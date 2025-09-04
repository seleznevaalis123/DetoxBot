from graphene_django import DjangoObjectType
from shop.models import Category
from shop.models import TeaItems


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "category_name", "category_desc", "category_photo")


class TeaItemsType(DjangoObjectType):
    class Meta:
        model = TeaItems
        fields = (
            "id",
            "item_category",
            "item_name",
            "item_desc",
            "item_price_idr",
            "item_price_thb",
            "item_price_aed",
            "item_price_rub",
            "item_weight",
            "item_photo",
        )