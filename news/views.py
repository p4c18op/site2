from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import New

class NewsList(ListView):
    model = New
    ordering = 'name'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['novosti'] = "ТОЛЬКО СВЕЖАЯ ИНФОРМАЦИЯ!"
        return context
class NewDetail(DetailView):
    model = New
    template_name = 'new.html'
    context_object_name = 'new'
