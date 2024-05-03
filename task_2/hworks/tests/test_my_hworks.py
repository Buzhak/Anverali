import pytest

from hworks.models import Hwork


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
