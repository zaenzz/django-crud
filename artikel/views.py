from django.urls import reverse_lazy
from django.views.generic import (
    FormView,
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    )

from .models import Artikel
from .forms import ArtikelForm

# Create your views here.
class ArtikelDeleteView(DeleteView):
    model = Artikel
    template_name = "artikel/artikel_delete_confirm.html"
    success_url = reverse_lazy('artikel:manage')


class ArtikelUpdateView(UpdateView):
    form_class = ArtikelForm
    model = Artikel
    template_name = "artikel/artikel_update.html"


class ArtikelCreateView(CreateView):
    form_class = ArtikelForm
    model = Artikel
    template_name = "artikel/artikel_form.html"

class ArtikelPerKategori():
    model= Artikel

    def get_latest_artikel(self):
        category_list = self.model.objects.values_list('category', flat=True).distinct()
        queryset = []

        for category in category_list:
            artikel = self.model.objects.filter(category=category).latest('publish')
            queryset.append(artikel)

        return queryset

class ManageArtikelView(ListView):
    model = Artikel
    template_name = "artikel/artikel_manage.html"
    context_object_name = "artikel_list"
    ordering = ['-publish']

class ArtikelCategoryListView(ListView):
    model = Artikel
    template_name = "artikel/artikel_category.html"
    context_object_name = "artikel_list"
    ordering = ['-publish']
    paginate_by = 3

    def get_queryset(self):
        self.queryset = self.model.objects.filter(category=self.kwargs['category'])
        return super().get_queryset()

    def get_context_data(self, *args, **kwargs):
        category_list = self.model.objects.values_list('category', flat=True).distinct().exclude(category=self.kwargs['category'])
        self.kwargs.update({'category_list':category_list})
        kwargs = self.kwargs 
        return super().get_context_data(*args, **kwargs)
    

class ArtikelListView(ListView):
    model = Artikel
    template_name = "artikel/artikel_list.html"
    context_object_name = "artikel_list"
    ordering = ['-publish']
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        category_list = self.model.objects.values_list('category', flat=True).distinct()
        self.kwargs.update({'category_list':category_list})
        kwargs = self.kwargs 
        return super().get_context_data(*args, **kwargs)

class ArtikelDetailView(DetailView):
    model = Artikel
    template_name = "artikel/artikel_detail.html"
    context_object_name = "artikel"

    def get_context_data(self, *args, **kwargs):
        category_list = self.model.objects.values_list('category', flat=True).distinct()
        self.kwargs.update({'category_list':category_list})
        
        artikel_serupa = self.model.objects.filter(category=self.object.category).exclude(id=self.object.id)
        self.kwargs.update({'artikel_serupa':artikel_serupa})

        kwargs = self.kwargs 
        return super().get_context_data(*args, **kwargs)

    
""" class ArtikelCreateView(CreateView):
    class_form = ArtikelForm
    model = Artikel
    tamplate_name = "artikel/create_artikel.html"
    fields = [
        'judul',
        'body',
        'penulis',
        'category',
        ]
 """