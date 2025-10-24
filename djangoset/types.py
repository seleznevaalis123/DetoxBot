from graphene_django import DjangoObjectType
from shop.models import Category
from shop.models import TeaItems
from shop.models import Cards
from shop.models import Orders



class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id",
                  "category_name",
                  "category_desc",
                  "category_photo")


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

class CardsType(DjangoObjectType):
    class Meta:
        model = Cards
        fields = (
            "id",
            "user",
            "tea_item",
            "item_price",
            "quantity",
            "created_dt",
            "currency",
        )

class OrdersType(DjangoObjectType):
    class Meta:
        model = Orders
        fields = (
            "id",
            "user",
            "created_dt",
            "last_updated_dt",
            "status",
            "delivery_address",
        )