from django.shortcuts import render
from django.db.models import Q
from ice_cream.models import IceCream


def index(request):
    template_name = 'homepage/index.html'
    ice_cream_list = IceCream.objects.values(  # .select_related('category')
        'id', 'title', 'description', 'category__title').filter(
        is_published=True,
        category__is_published=True
    ).filter(
            (Q(is_on_main=True) & Q(is_published=True))
            | (Q(title__contains='пломбир') & Q(is_published=True))
    ).order_by(
        'category__output_order',  # сортировка по порядку отображения категории
        'title'                 # затем по названию мороженого
    )[:4]  # ограничение до 4 записей
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template_name, context)
