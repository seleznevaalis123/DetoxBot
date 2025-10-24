import graphene
from shop.schema import Query as ShopQuery
from shop.schema import AddToCart, CreateOrder


class Query(ShopQuery, graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    add_to_cart = AddToCart.Field()
    create_order = CreateOrder.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
