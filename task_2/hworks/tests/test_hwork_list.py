import pytest

from hworks.models import Hwork


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
