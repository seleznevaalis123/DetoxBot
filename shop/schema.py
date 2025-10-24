import graphene
from djangoset.types import CategoryType, TeaItemsType, CardsType, OrdersType
from shop.models import Category, TeaItems, Cards, Orders, Users


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    tea_items = graphene.List(TeaItemsType, category_id=graphene.Int(required=False))
    user_card = graphene.List(CardsType, tg_id=graphene.String(required=True))
    user_order = graphene.List(OrdersType, tg_id=graphene.String(required=True))

    def resolve_categories(root, info):
        return Category.objects.all()

    def resolve_tea_items(root, info, category_id=None):
        if category_id:
            return TeaItems.objects.filter(item_category_id=category_id)
        return TeaItems.objects.all()

    def resolve_user_card(root, info, tg_id):
        user = Users.objects.get(tg_id=tg_id)
        return Cards.objects.filter(user=user)

    def resolve_user_order(root, info, tg_id):
        user = Users.objects.get(tg_id=tg_id)
        return Orders.objects.filter(user=user)
