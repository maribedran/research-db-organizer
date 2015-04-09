from django.contrib import admin
from models import (Publicacao,
                    Referencia,
                    Pessoa,
                    MoradorDeFavela,
                    Empresario,
                    Entidade,
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
    model = Entidade.funcionarios_publicos.through


class MembroDeAssociacaoInline(admin.TabularInline):
    model = Entidade.morador_associado.through


class MembroDeEntidadeInline(admin.TabularInline):
    model = Entidade.empresarios_membros.through


@admin.register(MoradorDeFavela)
class MoradorDeFavelaAdmin(admin.ModelAdmin):
    fields = (('nome', 'nascimento', 'morte', 'nacionalidade'),
              ('moradia', 'formacao', 'ocupacao', 'observacoes'),
              ('publicacoes', 'referencias'),
            )
    inlines = [
        FuncionalismoPublicoInline,
        MembroDeAssociacaoInline,
    ]


@admin.register(Empresario)
class EmpresarioAdmin(admin.ModelAdmin):
    fields = (('nome', 'nascimento', 'morte', 'nacionalidade'),
              ('moradia', 'formacao', 'ocupacao', 'observacoes'),
              ('publicacoes', 'referencias'),
            )
    inlines = [
        FuncionalismoPublicoInline,
        MembroDeEntidadeInline,
    ]


@admin.register(EntidadeEmpresarial)
class EntidadeEmpresarialAdmin(admin.ModelAdmin):
    fields = (('nome', 'fundacao', 'encerramento', 'fundador'),
              ('objetivos', 'carater', 'financiamento', 'acoes'),
              ('observacoes'),
              ('publicacoes', 'referencias'),
            )
    inlines = [
        MembroDeEntidadeInline,
    ]


@admin.register(Estatal)
class EstatalAdmin(admin.ModelAdmin):
    fields = (('nome', 'fundacao', 'encerramento', 'fundador'),
              ('objetivos', 'carater', 'financiamento', 'acoes'),
              ('observacoes'),
              ('publicacoes', 'referencias'),
            )
    inlines = [
        FuncionalismoPublicoInline,
    ]


@admin.register(AssociacaoDeFavela)
class AssociacaoDeFavelaAdmin(admin.ModelAdmin):
    fields = (('nome', 'fundacao', 'encerramento', 'fundador'),
              ('objetivos', 'carater', 'financiamento', 'acoes'),
              ('observacoes'),
              ('publicacoes', 'referencias'),
            )
    inlines = [
        MembroDeAssociacaoInline,
    ]


