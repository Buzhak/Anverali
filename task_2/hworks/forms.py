from django.forms import ModelForm

from .models import Hwork, Order


class CreateHworkForm(ModelForm):
    class Meta:
        model = Hwork
        fields = ('title', 'description', 'price', 'group')


class CreatOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('description', )
