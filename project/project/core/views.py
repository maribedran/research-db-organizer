from django.views.generic.base import TemplateView

from project.core.models import MoradorDeFavela, Empresario, Burocrata, AssociacaoDeFavela, EntidadeEmpresarial, Estatal

class HomeView(TemplateView):

    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['favelados'] = MoradorDeFavela.objects.all()
        context['empresarios'] = Empresario.objects.all()
        context['burocratas'] = Burocrata.objects.all()
        context['associacoes'] = AssociacaoDeFavela.objects.all()
        context['entidades'] = EntidadeEmpresarial.objects.all()
        context['estatais'] = Estatal.objects.all()

        return context
