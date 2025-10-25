import graphene
from shop.schema import Query as ShopQuery
from shop.schema import UpdateCart, CreateOrder


class Query(ShopQuery, graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    updateCart = UpdateCart.Field()
    create_order = CreateOrder.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
