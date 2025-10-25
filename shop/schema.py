import graphene
from django.db import transaction

from djangoset.types import CategoryType, TeaItemsType, CardsType, OrdersType
from shop.models import Category, TeaItems, Cards, Orders, Users, OrderItems


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
        cards = Cards.objects.filter(user=user)

        for card in cards:
            card.item_price = card.tea_item.item_price_rub * card.quantity

        return cards

    def resolve_user_order(root, info, tg_id):
        user = Users.objects.get(tg_id=tg_id)
        return Orders.objects.filter(user=user)


# Mutation
_MAX_QUANTITY_PER_ITEM = 20

class UpdateCart(graphene.Mutation):
    class Arguments:
        tg_id = graphene.String(required=True)
        tea_item_id = graphene.Int(required=False)
        quantity = graphene.Int(required=False, default_value=1)
        action = graphene.String(required=True)  # "add", "remove", "clear"

    card = graphene.Field(CardsType)

    @staticmethod
    def mutate(root, info, tg_id, action, tea_item_id=None, quantity=1):
        user = Users.objects.get(tg_id=tg_id)
        action = (action or "").lower()

        if action not in ("add", "remove", "clear"):
            raise Exception("action должен быть 'add', 'remove' или 'clear'")

        if action == "add":
            tea_item = TeaItems.objects.get(id=tea_item_id)
            card, created = Cards.objects.get_or_create(
                user=user,
                tea_item=tea_item,
                defaults={
                    "quantity": quantity,
                    "item_price": tea_item.item_price_rub,
                    "currency": "RUB",
                },
            )
            if not created:
                # проверяем ограничение
                if card.quantity + quantity > _MAX_QUANTITY_PER_ITEM:
                    raise Exception(f"Максимальное количество одного товара — {_MAX_QUANTITY_PER_ITEM}")
                card.quantity += quantity
                card.save()
            return UpdateCart(card=card)

        elif action == "remove":
            tea_item = TeaItems.objects.get(id=tea_item_id)
            try:
                card = Cards.objects.get(user=user, tea_item=tea_item)
                if card.quantity > quantity:
                    card.quantity -= quantity
                    card.save()
                    return UpdateCart(card=card)
                else:
                    card.delete()
                    return UpdateCart(card=None)
            except Cards.DoesNotExist:
                raise Exception("Товар не найден в корзине")

        elif action == "clear":
            Cards.objects.filter(user=user).delete()
            return UpdateCart(card=None)




class CreateOrder(graphene.Mutation):
    class Arguments:
        tg_id = graphene.String(required=True)
        delivery_address = graphene.String(required=False)

    order = graphene.Field(OrdersType)

    @staticmethod
    def mutate(root, info, tg_id, delivery_address=None):
        user = Users.objects.get(tg_id=tg_id)
        cart_items = Cards.objects.filter(user=user)
        if not cart_items.exists():
            raise Exception("Cart is empty")
        order = Orders.objects.create(user=user, status="NEW", delivery_address=delivery_address or "")
        for card in cart_items:
            OrderItems.objects.create(
                order=order,
                tea_item=card.tea_item,
                price=card.item_price,
                quantity=card.quantity,
                currency=card.currency
            )
        cart_items.delete()
        return CreateOrder(order=order)

