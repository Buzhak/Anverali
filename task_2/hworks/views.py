from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from django.http import Http404, HttpResponseForbidden, HttpResponseNotAllowed
from django.core.exceptions import PermissionDenied

from .forms import CreateHworkForm, HworkForm
from .models import Hwork, Order

User = get_user_model()


def index_view(request):
    '''
    view главной страницы
    '''
    template = 'hworks/index.html'
    context = {}
    if request.user.is_authenticated:
        if request.user.is_freelancer:  
            orders = Order.objects.prefetch_related("hwork").filter(hwork__user=request.user, is_finished=False)
            context = {
                'orders': orders
            }
        else:
            hworks = Hwork.objects.filter(is_archived=False).all()
            context = {
                'hworks': hworks
            }
    else:
        hworks = Hwork.objects.filter(is_archived=False).all()
        context = {
            'hworks': hworks
        }
    return render(request, template, context)


@login_required
def profile_view(request, username):
    '''
    view профиля пользователя username
    '''
    user = get_object_or_404(User, username=username)
    context = {'user_profile': user}
    template_name = 'hworks/profile.html'
    return render(request, template_name, context)


def hworks_user_list(request, username):
    '''
    view хворков пользователя username
    '''
    user = get_object_or_404(User, username=username)
    hworks = Hwork.objects.filter(user=user, is_archived=False)
    context = {
        'hworks': hworks,
        'seller': user.username
    }
    template = 'hworks/hwork_list.html'
    return render(request, template, context)


class HworkList(ListView):
    Model = Hwork
    template_name = 'hworks/hwork_list.html'
    context_object_name = 'hworks'
    def get_queryset(self):
        return Hwork.objects.filter(is_archived=False).all()


@login_required
def my_hworks(request):
    '''
    view текущего пользователя
    '''
    user = get_object_or_404(User, username=request.user)
    hworks = Hwork.objects.filter(user=user)
    context = {
        'hworks': hworks
    }
    template = 'hworks/my_hworks.html'
    return render(request, template, context)


@login_required
def hwork_archive_view(request, pk):
    '''
    view изменения статуса хворкка
    '''
    if request.method == 'POST':
        previous_url = request.META.get('HTTP_REFERER')
        user = get_object_or_404(User, username=request.user)
        hwork = get_object_or_404(Hwork, pk=pk)
        if hwork.user == user:
            hwork.is_archived = not hwork.is_archived
            hwork.save()
            if previous_url:
                return redirect(previous_url)
            return redirect('hworks:index')
        else:
            return HttpResponseForbidden()
    else:
        return HttpResponseNotAllowed('POST')


@method_decorator(login_required, name='dispatch')
class HworkCreate(CreateView):
    '''
    view создания хворка
    '''
    form_class = CreateHworkForm
    success_url = reverse_lazy('hworks:my_hworks')
    template_name = 'hworks/hwork_create.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Новый Hwork создан!')
        return super(HworkCreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class HworkUpdate(UpdateView):
    '''
    view обновления данных хворка
    '''
    model = Hwork
    fields = ['title', 'description', 'price', 'group']
    success_url = reverse_lazy('hworks:my_hworks')
    template_name = 'hworks/hwork_update.html'
    def get_object(self, queryset=None):
        obj = super(HworkUpdate, self).get_object()
        if not obj.user == self.request.user:
            raise PermissionDenied()
        return obj
    def form_valid(self, form):
        messages.success(self.request, 'Hwork успешно обновлен!')
        return super().form_valid(form)


@login_required
def orders_list_view(request):
    '''
    view заказов пользователя
    '''
    template_name = 'hworks/order_list.html'
    if request.user.is_freelancer:  
        orders = Order.objects.prefetch_related("hwork").filter(hwork__user=request.user)
        context = {
            'orders': orders,
        }
    else:
        orders = Order.objects.filter(customer=request.user).select_related('hwork__user')
        context = {
            'orders': orders
        }
    return render(request, template_name, context)


@login_required
def order_ready_view(request, pk):
    '''
    view подтверждение готовности к сдачи заказа
    '''
    if request.method == 'POST':
        previous_url = request.META.get('HTTP_REFERER')
        order = Order.objects.filter(pk=pk, is_finished=False).select_related('hwork__user').first()
        if not order:
            raise Http404('Заказ не найден')
        if order.hwork.user == request.user:
            order.is_ready = not order.is_ready
            order.save()
            if previous_url:
                return redirect(previous_url)
            return redirect('hworks:index')
        else:
            return HttpResponseForbidden()
    else:
        return HttpResponseNotAllowed('POST')
    

@login_required
def order_finished_view(request, pk):
    '''
    view завершения заказа
    '''
    if request.method == 'POST':
        previous_url = request.META.get('HTTP_REFERER')
        order = Order.objects.filter(pk=pk, is_ready=True ,is_finished=False).first()
        if not order:
            raise Http404('Заказ не найден')
        if order.customer == request.user:
            order.is_finished = True
            order.save()
            if previous_url:
                return redirect(previous_url)
            return redirect('hworks:index')
        else:
            return HttpResponseForbidden()
    else:
        return HttpResponseNotAllowed('POST')
