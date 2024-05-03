import pytest

from hworks.models import Hwork, Order


class TestIndexView:
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

class TestHworksListView:
    @pytest.mark.django_db(transaction=True)
    def test_hwork_list_get(self, client, customer_1_client, seller_1_client, hwork_1, hwork_2, hwork_3):
        clients = [client, customer_1_client, seller_1_client]
        for c in clients:
            try:
                response = c.get('/hwork/list/')
            except Exception as e:
                assert False, f'''Cтраница /hwork/list/ работает неправильно. Ошибка: `{e}`'''
            assert response.status_code == 200, (
                'Страница /hwork/list/ работает неправильно.'
            )
            # проверка моделей
            response_text = response.content.decode()

            hworks = Hwork.objects.filter(is_archived=False).all()
            for hwork in hworks:
                assert hwork.title in response_text, (
                    'Убедитесь, что на странице /hwork/list/ выводятся все Хворки '
                    'не находящиеся в архиве'
                )

class TestMyHworksView:
    @pytest.mark.django_db(transaction=True)
    def test_my_hvork_seller_get(self, seller_1_client, seller_1, hwork_1, hwork_2, hwork_3):
        try:
            response = seller_1_client.get('/hwork/my_hworks/')
        except Exception as e:
            assert False, f'''Cтраница hwork/my_hworks/ работает неправильно. Ошибка: `{e}`'''
        assert response.status_code == 200, (
            'Страница /hwork/my_hworks/ работает неправильно.'
        )
        # проверка моделей
        response_text = response.content.decode()

        hworks = Hwork.objects.filter(user=seller_1).all()
        for hwork in hworks:
            assert hwork.title in response_text, (
                'Убедитесь, что на странице /hwork/my_hworks/ выводятся абсолютно все Хворки '
                'продавца переходящено на эту страницу.'
            )

    @pytest.mark.django_db(transaction=True)
    def test_my_hworks_guest_get(self, client):
        response = client.get('/hwork/my_hworks/')
        assert response.status_code == 302, (
            '/hwork/my_hworks/ - гостя не должно пускать на эту страницу.'
        )
    
    @pytest.mark.django_db(transaction=True)
    def test_my_hworks_customer_get(self, customer_1_client):
        response = customer_1_client.get('/hwork/my_hworks/')
        assert response.status_code == 403, (
            '/hwork/my_hworks/ - у заказчика не должно быть доступа на эту страницу.'
        )

class TestMyHworksView:
    @pytest.mark.django_db(transaction=True)
    def test_profile_guest_get(self, client, seller_1):
        response = client.get(f'/profile/{seller_1.get_username()}/')
        assert response.status_code == 302, (
            '/profile/<username>/ - гостю не должны быть доступны профили пользователей.'
        )
    
    @pytest.mark.django_db(transaction=True)
    def test_profile_users_get(self, customer_1_client, seller_1, customer_1):
        response = customer_1_client.get(f'/profile/{customer_1.get_username()}/')
        assert response.status_code == 200, (
            '/profile/<username>/ - клиенту должна быть достапна его страница профиля'
        )
        response = customer_1_client.get(f'/profile/{seller_1.get_username()}/')
        assert response.status_code == 200, (
            '/profile/<username>/ - клиенту должна быть достапна страница профиля продавца'
        )
