import pytest


class TestProfileView:
    @pytest.mark.django_db(transaction=True)
    def test_profile_guest_get(self, client, seller_1):
        response = client.get(f'/profile/{seller_1.get_username()}/')
        assert response.status_code == 302, (
            '/profile/<username>/ - гостю не должны '
            'быть доступны профили пользователей.'
        )

    @pytest.mark.django_db(transaction=True)
    def test_profile_users_get(self, customer_1_client, seller_1, customer_1):
        response = customer_1_client.get(f'/profile/{customer_1.get_username()}/')
        assert response.status_code == 200, (
            '/profile/<username>/ - клиенту должна быть достапна его страница профиля'
        )
        response = customer_1_client.get(f'/profile/{seller_1.get_username()}/')
        assert response.status_code == 200, (
            '/profile/<username>/ - клиенту должна '
            'быть достапна страница профиля продавца'
        )
