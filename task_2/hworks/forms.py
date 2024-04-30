from django.forms import ModelForm

from .models import Hwork


class CreateHworkForm(ModelForm):
    class Meta:
        model = Hwork
        fields = ('title', 'description', 'price', 'group')


class HworkForm(ModelForm):
    class Meta:
        model = Hwork
        fields = ('title', 'description', 'price', 'group', 'user')
