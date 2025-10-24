from django.test import TestCase
from graphene.test import Client
from shop.models import Category, TeaItems
from djangoset.schema import schema

class GraphQLTests(TestCase):
    def setUp(self):
        # Создаем тестовые категории
        self.cat1 = Category.objects.create(
            category_name="Зеленый чай",
            category_desc="Описание зеленого чая"
        )
        self.cat2 = Category.objects.create(
            category_name="Пуэр",
            category_desc="Описание пуэра"
        )

        # Создаем тестовые TeaItems
        self.tea1 = TeaItems.objects.create(
            item_category=self.cat1,
            item_name="Сенча",
            item_desc="Высококачественный японский чай",
            item_price_rub=500
        )
        self.tea2 = TeaItems.objects.create(
            item_category=self.cat2,
            item_name="Шу Пуэр",
            item_desc="Черный китайский пуэр",
            item_price_rub=700
        )

        # GraphQL клиент
        self.client = Client(schema)

    # ------------------ Тест категорий ------------------
    def test_categories_query(self):
        query = """
        query {
            categories {
                id
                categoryName
                categoryDesc
            }
        }
        """
        executed = self.client.execute(query)

        if executed.get("errors"):
            print("GraphQL Errors:", executed["errors"])

        categories_data = executed.get("data", {}).get("categories")
        self.assertIsNotNone(categories_data)
        self.assertEqual(len(categories_data), 2)
        self.assertEqual(categories_data[0]["categoryName"], "Зеленый чай")
        self.assertEqual(categories_data[1]["categoryName"], "Пуэр")

    # ------------------ Тест TeaItems ------------------
    def test_tea_items_query(self):
        query = """
        query {
            teaItems {
                id
                itemName
                itemDesc
                itemPriceRub
                itemCategory {
                    id
                    categoryName
                }
            }
        }
        """
        executed = self.client.execute(query)

        if executed.get("errors"):
            print("GraphQL Errors:", executed["errors"])

        tea_items_data = executed.get("data", {}).get("teaItems")
        self.assertIsNotNone(tea_items_data)
        self.assertEqual(len(tea_items_data), 2)
        self.assertEqual(tea_items_data[0]["itemCategory"]["categoryName"], "Зеленый чай")
        self.assertEqual(tea_items_data[1]["itemCategory"]["categoryName"], "Пуэр")
