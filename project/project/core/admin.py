from django.contrib import admin
from models import (Publicacao,
                    Referencia,
                    Pessoa,
                    MoradorDeFavela,
                    Empresario,
                    EntidadeEmpresarial,
                    Estatal,
                    AssociacaoDeFavela)

@admin.register(Publicacao)
class PublicacaoAdmin(admin.ModelAdmin):
    list_filter = ('titulo',)


@admin.register(Referencia)
class ReferenciaAdmin(admin.ModelAdmin):
    list_filter = ('titulo',)


class FuncionalismoPublicoInline(admin.TabularInline):
    model = Pessoa.cargo_publico.through


class MembroDeAssociacaoInline(admin.TabularInline):
    model = MoradorDeFavela.associacao_de_favela.through


class MembroDeEntidadeInline(admin.TabularInline):
    model = Empresario.entidade_empresarial.through


@admin.register(MoradorDeFavela)
class MoradorDeFavelaAdmin(admin.ModelAdmin):
    inlines = [
        FuncionalismoPublicoInline,
        MembroDeAssociacaoInline,
    ]
    exclude = ('cargo_publico', 'associacao_de_favela')


@admin.register(Empresario)
class EmpresarioAdmin(admin.ModelAdmin):
    inlines = [
        FuncionalismoPublicoInline,
        MembroDeEntidadeInline,
    ]
    exclude = ('cargo_publico', 'entidade_empresarial')


@admin.register(EntidadeEmpresarial)
class EntidadeEmpresarialAdmin(admin.ModelAdmin):
    inlines = [
        MembroDeEntidadeInline,
    ]


@admin.register(Estatal)
class EstatalAdmin(admin.ModelAdmin):
    inlines = [
        FuncionalismoPublicoInline,
    ]


@admin.register(AssociacaoDeFavela)
class AssociacaoDeFavelaAdmin(admin.ModelAdmin):
    inlines = [
        MembroDeAssociacaoInline,
    ]


