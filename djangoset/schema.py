import graphene
from shop.schema import Query as ShopQuery


class Query(ShopQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
