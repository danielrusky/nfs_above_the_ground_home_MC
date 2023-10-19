from django.shortcuts import render, get_object_or_404

import magazine
from magazine.models import Autocar, Marka
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, ListView, UpdateView, DeleteView


class AutocarCreateView(CreateView):
    model = Autocar
    fields = ('name', 'description', 'price', 'image', 'marka')
    success_url = reverse_lazy('home')


class AutocarListView(ListView):
    model = Autocar
    template_name = 'magazine/home.html'


# def home(request):
#     autocar_list = Autocar.objects.all()
#     context = {
#         'object_list': autocar_list
#     }
#     return render(request, 'magazine/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'У вас новое сообщение от: {name} (телефон: {phone}): {message}')
    return render(request, 'magazine/contacts.html')


class AutocarDetailView(DetailView):
    model = Autocar


class AutocarUpdateView(UpdateView):
    model = Marka
    fields = ('name', 'description')
    success_url = reverse_lazy('home')


class MarkaUpdateView(UpdateView):
    model = Marka
    fields = ('name', 'description')
    success_url = reverse_lazy('home')


class AutocarDeleteView(DeleteView):
    model = Marka
    success_url = reverse_lazy('home')


class MarkaDeleteView(DeleteView):
    model = Marka
    success_url = reverse_lazy('home')


# def view_product(request, pk):
#     autocar_item = get_object_or_404(Autocar, pk=pk)
#     context = {
#         'object': autocar_item
#     }
#     return render(request, 'magazine/autocar_detail.html', {'product': Autocar.objects.get(pk=pk)})


#

class MarkaCreateView(CreateView):
    model = Marka
    fields = ('name', 'description')
    success_url = reverse_lazy('home')


# def marka_create(request):
#     if request.method == 'POST':
#         cat_name = request.POST.get('marka_name')
#         cat_desc = request.POST.get('marka_desc')
#         Marka.objects.create(name=marka_name, description=marka_desc)
#         return redirect('home')
#     return render(request, 'magazine/marka_form.html')


# def autocar_create(request):
#     if request.method == 'POST':
#         prod_category = request.POST.get('autocar_category')
#         name = request.POST.get('autocar_name')
#         price = request.POST.get('autocar_price')
#         description = request.POST.get('autocar_desc')
#         prod_image = request.FILES.get('autocar_image')
#         Autocar.objects.create(name=name, description=description, price=price,
#                                image=autocar_image, category=Marka.objects.get(id=autocar_category))
#         print(f"Данные:\n"
#               f"Название: {name}\n"
#               f"Описание: {description}\n"
#               f"Цена: {price}\n"
#               f"Фото: {autocar_image}\n"
#               f"Категория: {autocar_category}")
#     return render(request, 'magazine/autocar_form.html', {'autocar_create': Marka.objects.all()})

def toggle_active(request, slug):
    materials = get_object_or_404(magazine, slug=slug)
    if materials.to_publish:
        materials.to_publish = False
    else:
        materials.to_publish = True
    materials.save()
    return redirect('blog_detail', slug=materials.slug)
