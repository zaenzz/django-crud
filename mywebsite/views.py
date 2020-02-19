from django.views.generic import TemplateView 
from artikel.views import ArtikelPerKategori

class BlogHomeView(TemplateView, ArtikelPerKategori):
    template_name = "index.html"

    def get_context_data(self):
        querysets = self.get_latest_artikel()
        context = {
            'artikel_latest':querysets,
        }
        return context


    