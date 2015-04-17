from django.contrib import admin
from models import (Publicacao,
                    Referencia,
                    Pessoa,
                    MoradorDeFavela,
                    Empresario,
                    Burocrata,
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


class PessoaPublicacaoInline(admin.TabularInline):
    model = Pessoa.publicacoes.through


class PessoaReferenciaInline(admin.TabularInline):
    model = Pessoa.referencias.through


class EntidadePublicacaoInline(admin.TabularInline):
    model = Entidade.publicacoes.through


class EntidadeReferenciaInline(admin.TabularInline):
    model = Entidade.referencias.through


@admin.register(MoradorDeFavela)
class MoradorDeFavelaAdmin(admin.ModelAdmin):
    fields = (('nome', 'nascimento', 'morte', 'nacionalidade'),
              ('moradia', 'formacao', 'ocupacao', 'observacoes'),
            )
    inlines = [
        FuncionalismoPublicoInline,
        MembroDeAssociacaoInline,
        DirecaoInline,
        PessoaPublicacaoInline,
        PessoaReferenciaInline,
    ]
    list_filter = ('nome', 'nascimento', 'morte', 'nacionalidade',
        'moradia', 'formacao', 'ocupacao', 'observacoes',)
    ordering = ('nome', 'nascimento')


@admin.register(Empresario)
class EmpresarioAdmin(admin.ModelAdmin):
    fields = (('nome', 'nascimento', 'morte', 'nacionalidade'),
              ('moradia', 'formacao', 'ocupacao', 'observacoes'),
            )
    inlines = [
        FuncionalismoPublicoInline,
        MembroDeEntidadeInline,
        DirecaoInline,
        PessoaPublicacaoInline,
        PessoaReferenciaInline,
    ]
    list_filter = ('nome', 'nascimento', 'morte', 'nacionalidade',
                   'moradia', 'formacao', 'ocupacao', 'observacoes',)


@admin.register(Burocrata)
class BurocrataAdmin(admin.ModelAdmin):
    fields = (('nome', 'nascimento', 'morte', 'nacionalidade'),
              ('moradia', 'formacao', 'ocupacao', 'observacoes'),
            )
    inlines = [
        FuncionalismoPublicoInline,
        DirecaoInline,
        PessoaPublicacaoInline,
        PessoaReferenciaInline,
    ]
    list_filter = ('nome', 'nascimento', 'morte', 'nacionalidade',
                   'moradia', 'formacao', 'ocupacao', 'observacoes',)


@admin.register(EntidadeEmpresarial)
class EntidadeEmpresarialAdmin(admin.ModelAdmin):
    fields = (('nome', 'fundacao', 'encerramento', 'fundador'),
              ('objetivos', 'carater', 'financiamento', 'acoes'),
              ('observacoes'),
            )
    inlines = [
        MembroDeEntidadeInline,
        DirecaoInline,
        RelacaoEstadoBurguesiaInline,
        RelacaoEntidadeAssociacaoInline,
        EntidadePublicacaoInline,
        EntidadeReferenciaInline,
    ]
    list_filter = ('nome', 'fundacao', 'encerramento', 'fundador',
                   'objetivos', 'carater', 'financiamento', 'acoes',
                   'observacoes',)


@admin.register(Estatal)
class EstatalAdmin(admin.ModelAdmin):
    fields = (('nome', 'fundacao', 'encerramento', 'fundador'),
              ('objetivos', 'carater', 'financiamento', 'acoes'),
              ('observacoes'),
            )
    inlines = [
        FuncionalismoPublicoInline,
        DirecaoInline,
        RelacaoEstadoMovimentoSocialInline,
        RelacaoEstadoBurguesiaInline,
        EntidadePublicacaoInline,
        EntidadeReferenciaInline,
    ]
    list_filter = ('nome', 'fundacao', 'encerramento', 'fundador',
                   'objetivos', 'carater', 'financiamento', 'acoes',
                   'observacoes',)


@admin.register(AssociacaoDeFavela)
class AssociacaoDeFavelaAdmin(admin.ModelAdmin):
    fields = (('nome', 'fundacao', 'encerramento', 'fundador'),
              ('objetivos', 'carater', 'financiamento', 'acoes'),
              ('observacoes'),
            )
    inlines = [
        MembroDeAssociacaoInline,
        DirecaoInline,
        RelacaoEstadoMovimentoSocialInline,
        RelacaoEntidadeAssociacaoInline,
        EntidadePublicacaoInline,
        EntidadeReferenciaInline,
    ]
    list_filter = ('nome', 'fundacao', 'encerramento', 'fundador',
                   'objetivos', 'carater', 'financiamento', 'acoes',
                   'observacoes',)


