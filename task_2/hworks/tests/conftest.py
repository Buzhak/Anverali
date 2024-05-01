import pytest

from hworks.models import Group, Hwork, Order
from . import constants


@pytest.fixture
def seller_1(django_user_model):
    return django_user_model.objects.create_user(
        username=constants.SELLER_1,
        password=constants.PASS,
        is_freelancer=True
    )


@pytest.fixture
def seller_2(django_user_model):
    return django_user_model.objects.create_user(
        username=constants.SELLER_2,
        password=constants.PASS,
        is_freelancer=True
    )


@pytest.fixture
def customer_1(django_user_model):
    return django_user_model.objects.create_user(
        username=constants.CUSTOMER_1,
        password=constants.PASS,
    )


@pytest.fixture
def seller_1_client(seller_1, client):
    client.force_login(seller_1)
    return client


@pytest.fixture
def seller_2_client(seller_2, client):
    client.force_login(seller_2)
    return client


@pytest.fixture
def customer_1_client(customer_1, client):
    client.force_login(customer_1)
    return client


@pytest.fixture
def group_1():
    return Group.objects.create(
        title=constants.GROUP_1_TITLE,
        description=constants.GROUP_1_DES
    )


@pytest.fixture
def hwork_1(seller_1, group_1):
    return Hwork.objects.create(
        title=constants.HWORK_1['title'],
        description=constants.HWORK_1['description'],
        price=constants.HWORK_1['price'],
        user=seller_1,
        group=group_1,
    )


@pytest.fixture
def hwork_2(seller_1, group_1):
    return Hwork.objects.create(
        title=constants.HWORK_2['title'],
        description=constants.HWORK_2['description'],
        price=constants.HWORK_2['price'],
        user=seller_1,
        group=group_1,
        is_archived=True
    )


@pytest.fixture
def hwork_3(seller_2, group_1):
    return Hwork.objects.create(
        title=constants.HWORK_3['title'],
        description=constants.HWORK_3['description'],
        price=constants.HWORK_3['price'],
        user=seller_2,
        group=group_1,
        is_archived=True
    )


@pytest.fixture
def order_1(customer_1, hwork_1, seller_1):
    return Order.objects.create(
        title=hwork_1.title,
        description='Some_text',
        price=hwork_1.price,
        customer=customer_1,
        seller=seller_1.get_username(),
        hwork=hwork_1,

    )


@pytest.fixture
def order_2(customer_1, hwork_2, seller_1):
    return Order.objects.create(
        title=hwork_2.title,
        description='Some_text',
        price=hwork_2.price,
        customer=customer_1,
        seller=seller_1.get_username(),
        hwork=hwork_2,
        is_ready=True,
        is_finished=True,
    )


@pytest.fixture
def order_3(customer_1, hwork_3, seller_2):
    return Order.objects.create(
        title=hwork_3.title,
        description='Some_text',
        price=hwork_3.price,
        customer=customer_1,
        seller=seller_2.get_username(),
        hwork=hwork_3,
    )
