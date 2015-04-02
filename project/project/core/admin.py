from django.contrib import admin
from models import (Publicacao,
                    Referencia,
                    Pessoa,
                    Entidade,
                    EntidadeEmpresarial,
                    Estatal,
                    AssociacaoDeFavela)


class PublicacaoAdmin(admin.ModelAdmin):
    list_filter = ('titulo',)


class ReferenciaAdmin(admin.ModelAdmin):
    list_filter = ('titulo',)


class PessoaAdmin(admin.ModelAdmin):
    list_filter = ('nome', 'publicacoes', 'referencias')
    list_display = ('nome',)
    list_select_related = ('publicacoes', 'referencias', 'cargo_de_direcao', 'cargo_publico',
    'entidade_empresarial')


class EntidadeAdmin(admin.ModelAdmin):
    pass


class EntidadeEmpresarialAdmin(admin.ModelAdmin):
    pass


class EstatalAdmin(admin.ModelAdmin):
    pass


class AssociacaoDeFavelaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Publicacao, PublicacaoAdmin)
admin.site.register(Referencia, ReferenciaAdmin)
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Entidade, EntidadeAdmin)
admin.site.register(EntidadeEmpresarial, EntidadeEmpresarialAdmin)
admin.site.register(Estatal, EstatalAdmin)
admin.site.register(AssociacaoDeFavela, AssociacaoDeFavelaAdmin)
