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


class DirecaoInline(admin.TabularInline):
    model = Entidade.diretores.through


class FuncionalismoPublicoInline(admin.TabularInline):
    model = Estatal.funcionarios_publicos.through


class MembroDeAssociacaoInline(admin.TabularInline):
    model = AssociacaoDeFavela.moradores_associados.through


class MembroDeEntidadeInline(admin.TabularInline):
    model = EntidadeEmpresarial.empresarios_membros.through


class RelacaoEstadoBurguesiaInline(admin.TabularInline):
    model = Estatal.entidades_empresariais.through


class RelacaoEstadoMovimentoSocialInline(admin.TabularInline):
    model = Estatal.associacoes_de_favela.through


class RelacaoEntidadeAssociacaoInline(admin.TabularInline):
    model = EntidadeEmpresarial.associacoes_de_favela.through


@admin.register(MoradorDeFavela)
class MoradorDeFavelaAdmin(admin.ModelAdmin):
    fields = (('nome', 'nascimento', 'morte', 'nacionalidade'),
              ('moradia', 'formacao', 'ocupacao', 'observacoes'),
              ('publicacoes', 'referencias'),
            )
    inlines = [
        FuncionalismoPublicoInline,
        MembroDeAssociacaoInline,
        DirecaoInline,
    ]
    list_filter = ('nome', 'nascimento', 'morte', 'nacionalidade',
                   'moradia', 'formacao', 'ocupacao', 'observacoes',
                   'publicacoes', 'referencias')
    ordering = ('nome', 'nascimento')


@admin.register(Empresario)
class EmpresarioAdmin(admin.ModelAdmin):
    fields = (('nome', 'nascimento', 'morte', 'nacionalidade'),
              ('moradia', 'formacao', 'ocupacao', 'observacoes'),
              ('publicacoes', 'referencias'),
            )
    inlines = [
        FuncionalismoPublicoInline,
        MembroDeEntidadeInline,
        DirecaoInline,
    ]
    list_filter = ('nome', 'nascimento', 'morte', 'nacionalidade',
                   'moradia', 'formacao', 'ocupacao', 'observacoes',
                   'publicacoes', 'referencias')


@admin.register(EntidadeEmpresarial)
class EntidadeEmpresarialAdmin(admin.ModelAdmin):
    fields = (('nome', 'fundacao', 'encerramento', 'fundador'),
              ('objetivos', 'carater', 'financiamento', 'acoes'),
              ('observacoes'),
              ('publicacoes', 'referencias'),
            )
    inlines = [
        MembroDeEntidadeInline,
        DirecaoInline,
        RelacaoEstadoBurguesiaInline,
        RelacaoEntidadeAssociacaoInline,
    ]
    list_filter = ('nome', 'fundacao', 'encerramento', 'fundador',
                   'objetivos', 'carater', 'financiamento', 'acoes',
                   'observacoes', 'publicacoes', 'referencias',
    )


@admin.register(Estatal)
class EstatalAdmin(admin.ModelAdmin):
    fields = (('nome', 'fundacao', 'encerramento', 'fundador'),
              ('objetivos', 'carater', 'financiamento', 'acoes'),
              ('observacoes'),
              ('publicacoes', 'referencias'),
            )
    inlines = [
        FuncionalismoPublicoInline,
        DirecaoInline,
        RelacaoEstadoMovimentoSocialInline,
        RelacaoEstadoBurguesiaInline,
    ]
    list_filter = ('nome', 'fundacao', 'encerramento', 'fundador',
                   'objetivos', 'carater', 'financiamento', 'acoes',
                   'observacoes', 'publicacoes', 'referencias',
    )


@admin.register(AssociacaoDeFavela)
class AssociacaoDeFavelaAdmin(admin.ModelAdmin):
    fields = (('nome', 'fundacao', 'encerramento', 'fundador'),
              ('objetivos', 'carater', 'financiamento', 'acoes'),
              ('observacoes'),
              ('publicacoes', 'referencias'),
            )
    inlines = [
        MembroDeAssociacaoInline,
        DirecaoInline,
        RelacaoEstadoMovimentoSocialInline,
        RelacaoEntidadeAssociacaoInline,
    ]
    list_filter = ('nome', 'fundacao', 'encerramento', 'fundador',
                   'objetivos', 'carater', 'financiamento', 'acoes',
                   'observacoes', 'publicacoes', 'referencias',
    )


