import pytest

from hworks.models import Hwork, Order


class TestCreateView:
    @pytest.mark.django_db(transaction=True)
    def test_index_view_anonim_or_customer_get(self, client, customer_1_client, hwork_1, hwork_2, hwork_3):
        clients = [client, customer_1_client]
        for c in clients:
            try:
                response = c.get('/')
            except Exception as e:
                assert False, f'''Главная страница работает неправильно. Ошибка: `{e}`'''
            assert response.status_code == 200, (
                'Главная страница работает неправильно.'
            )
            # проверка моделей
            response_text = response.content.decode()

            hworks = Hwork.objects.filter(is_archived=False).all()
            for hwork in hworks:
                assert hwork.title in response_text, (
                    'Убедитесь, что на главной странице выводятся все Хворки '
                    'не находящиеся в архиве'
                )
    
    @pytest.mark.django_db(transaction=True)
    def test_index_view_seller_get(self, seller_1 ,seller_1_client, hwork_1, hwork_2, hwork_3, order_1, order_2, order_3):
            try:
                response = seller_1_client.get('/')
            except Exception as e:
                assert False, f'''Главная страница работает неправильно. Ошибка: `{e}`'''
            assert response.status_code == 200, (
                'Главная страница работает неправильно.'
            )
            # проверка моделей
            response_text = response.content.decode()
            orders = Order.objects.filter(is_finished=False, seller=seller_1.get_username()).all()
            for order in orders:
                assert order.title in response_text, (
                    'Убедитесь, что на главной странице залогиненого продавца'
                    'выводятся активные заказы'
                )
            order = Order.objects.get(pk=order_3.id)
            assert order.title not in response_text, (
                    'Убедитесь, что на главной странице залогиненого продавца'
                    'не выводятся заказы других пользователей'
                )
