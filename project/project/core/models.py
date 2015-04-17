#coding: utf-8
from django.db import models

class Publicacao(models.Model):
    titulo = models.CharField(max_length=200)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = u"Publicação"
        verbose_name_plural = u"Publicações"


class Referencia(models.Model):
    titulo = models.CharField(max_length=200)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = u"Referência"
        verbose_name_plural = u"Referências"


class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    nascimento = models.DateField(null=True, blank=True)
    morte = models.DateField(null=True, blank=True)
    nacionalidade = models.CharField(max_length=30, null=True, blank=True)
    moradia = models.CharField(max_length=100, null=True, blank=True)
    formacao = models.CharField(max_length=100,
                                null=True,
                                blank=True,
                                verbose_name=u"formação")
    ocupacao = models.CharField(max_length=100,
                                null=True,
                                blank=True,
                                verbose_name=u"ocupação")

    observacoes = models.CharField(max_length=1000,
                                   null=True,
                                   blank=True,
                                   verbose_name=u"observações")

    #Publicacao
    publicacoes = models.ManyToManyField(
        to=Publicacao,
        through="PessoaPublicacao",
        related_name="contribuidores_individuais",
        null=True,
        blank=True,
        verbose_name=u"publicações"
    )

    #Referencia
    referencias = models.ManyToManyField(
        to=Referencia,
        through="PessoaReferencia",
        related_name="pessoas_citadas",
        null=True,
        blank=True,
        verbose_name=u"referências"
    )


    def __unicode__(self):
        return self.nome


class MoradorDeFavela(Pessoa):

    class Meta:
        verbose_name_plural = u"Moradores de favelas"


class Empresario(Pessoa):

    class Meta:
        verbose_name = u"Empresário"
        verbose_name_plural = u"Empresários"


class Burocrata(Pessoa):

    pass


class Entidade(models.Model):
    nome = models.CharField(max_length=200)
    fundacao = models.DateField(null=True,
                                blank=True,
                                verbose_name=u"fundação")
    encerramento = models.DateField(null=True, blank=True)
    fundador = models.CharField(max_length=200, null=True, blank=True)
    objetivos = models.CharField(max_length=200, null=True, blank=True)
    carater = models.CharField(max_length=200,
                               null=True,
                               blank=True,
                               verbose_name=u"caráter")
    financiamento = models.CharField(max_length=100, null=True, blank=True)
    acoes = models.CharField(max_length=200,
                             null=True,
                             blank=True,
                             verbose_name=u"ações")

    grupos_representados = models.CharField(max_length=200, null=True, blank=True)

    observacoes = models.CharField(max_length=1000,
                                   null=True,
                                   blank=True,
                                   verbose_name=u"observações")

    #Publicacao
    publicacoes = models.ManyToManyField(
        to=Publicacao,
        through="EntidadePublicacao",
        related_name="contribuidores_coletivos",
        null=True,
        blank=True,
        verbose_name=u"publicações"
    )

    #Referencia
    referencias = models.ManyToManyField(to=Referencia,
        through="EntidadeReferencia",
        related_name="entidades_citadas",
        null=True,
        blank=True,
        verbose_name=u"referências"
    )

    #Pessoa
    diretores = models.ManyToManyField(Pessoa,
        through="CargoDeDirecao"
    )


    def __unicode__(self):
        return self.nome


class AssociacaoDeFavela(Entidade):
    moradores_associados = models.ManyToManyField(MoradorDeFavela,
        through="MoradorAssociado",
        related_name="associacao_favela"
    )

    class Meta:
        verbose_name = u"Associação de favela"
        verbose_name_plural = u"Associações de favelas"


class EntidadeEmpresarial(Entidade):
    empresarios_membros = models.ManyToManyField(Empresario,
        through="MembroEntidadeEmpresarial",
        related_name="membro_entidade_empresarial",
        verbose_name=u"empresários membros"
    )

    associacoes_de_favela = models.ManyToManyField(AssociacaoDeFavela,
            through="RelacaoEntidadeAssociacao",
            related_name="entidades_empresariais",
    )

    class Meta:
        verbose_name_plural = u"Entidades empresariais"


class Estatal(Entidade):
    funcionarios_publicos = models.ManyToManyField(Pessoa,
        through="FuncionalismoPublico",
        related_name="cargo_publico",
        verbose_name=u"funcionários públicos"
    )

    entidades_empresariais = models.ManyToManyField(EntidadeEmpresarial,
            through="RelacaoEstadoBurguesia",
            related_name="estatais",
            verbose_name=u"Relação Estado Burguesia"
    )

    associacoes_de_favela = models.ManyToManyField(AssociacaoDeFavela,
            through="RelacaoEstadoMovimentoSocial",
            related_name="Estatais",
            verbose_name=u"Relação Estado Movimentos Sociais"
    )

    class Meta:
        verbose_name_plural = u"Estatais"


class CargoDeDirecao(models.Model):
    pessoa = models.ForeignKey(Pessoa)
    entidade = models.ForeignKey(Entidade)

    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = u"Cargo de direção"
        verbose_name_plural = u"Cargos de direção"

class FuncionalismoPublico(models.Model):
    pessoa = models.ForeignKey(Pessoa)
    estatal = models.ForeignKey(Estatal)

    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = u"Funcionalismo público"
        verbose_name_plural = u"Cargos no funcionalismo público"

class MembroEntidadeEmpresarial(models.Model):
    empresario = models.ForeignKey(Empresario)
    entidade_empresarial = models.ForeignKey(EntidadeEmpresarial)

    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = u"Membro de entidade empresarial"
        verbose_name_plural = u"Membros de entidades empresariais"


class MoradorAssociado(models.Model):
    morador = models.ForeignKey(MoradorDeFavela)
    associacao = models.ForeignKey(AssociacaoDeFavela,
            verbose_name=u"associação")

    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = u"Morador associado"
        verbose_name_plural = u"Moradores associados"


class RelacaoEstadoBurguesia(models.Model):
    estatal = models.ForeignKey(Estatal)
    entidades_empresarial = models.ForeignKey(EntidadeEmpresarial)

    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)


class RelacaoEstadoMovimentoSocial(models.Model):
    estatal = models.ForeignKey(Estatal)
    associacao_favela = models.ForeignKey(AssociacaoDeFavela)

    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)


class RelacaoEntidadeAssociacao(models.Model):
    entidade_empresarial = models.ForeignKey(EntidadeEmpresarial)
    associacao_favela = models.ForeignKey(AssociacaoDeFavela)

    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)


class PessoaPublicacao(models.Model):
    pessoa = models.ForeignKey(Pessoa)
    publicacao = models.ForeignKey(Publicacao)

    pagina = models.CharField(max_length=100)
    observacoes = models.CharField(max_length=200)


class PessoaReferencia(models.Model):
    pessoa = models.ForeignKey(Pessoa)
    referencia = models.ForeignKey(Referencia)

    pagina = models.CharField(max_length=100)
    observacoes = models.CharField(max_length=200)


class EntidadePublicacao(models.Model):
    entidade = models.ForeignKey(Entidade)
    publicacao = models.ForeignKey(Publicacao)

    pagina = models.CharField(max_length=100)
    observacoes = models.CharField(max_length=200)


class EntidadeReferencia(models.Model):
    entidade = models.ForeignKey(Entidade)
    referencia = models.ForeignKey(Referencia)

    pagina = models.CharField(max_length=100)
    observacoes = models.CharField(max_length=200)


