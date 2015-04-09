#coding: utf-8
from django.db import models

class Publicacao(models.Model):
    titulo = models.CharField(max_length=200)

    def __unicode__(self):
        return self.titulo


class Referencia(models.Model):
    titulo = models.CharField(max_length=200)

    def __unicode__(self):
        return self.titulo


class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    nascimento = models.DateField(null=True, blank=True)
    morte = models.DateField(null=True, blank=True)
    nacionalidade = models.CharField(max_length=30, null=True, blank=True)
    moradia = models.CharField(max_length=100, null=True, blank=True)
    formacao = models.CharField(max_length=100, null=True, blank=True)
    ocupacao = models.CharField(max_length=100, null=True, blank=True)

    observacoes = models.CharField(max_length=1000, null=True, blank=True)

    #Publicacao
    publicacoes = models.ManyToManyField(to=Publicacao,
                                    related_name="contribuidores_individuais",
                                    null=True,
                                    blank=True)

    #Referencia
    referencias = models.ManyToManyField(to=Referencia,
                                    related_name="pessoas_citadas",
                                    null=True,
                                    blank=True)


    def __unicode__(self):
        return self.nome


class MoradorDeFavela(Pessoa):
    class Meta:
        proxy = True


class Empresario(Pessoa):
    class Meta:
        proxy = True


class Entidade(models.Model):
    nome = models.CharField(max_length=200)
    fundacao = models.DateField(null=True, blank=True)
    encerramento = models.DateField(null=True, blank=True)
    fundador = models.CharField(max_length=200, null=True, blank=True)
    objetivos = models.CharField(max_length=200, null=True, blank=True)
    carater = models.CharField(max_length=200, null=True, blank=True)
    financiamento = models.CharField(max_length=100, null=True, blank=True)
    acoes = models.CharField(max_length=200, null=True, blank=True)

    grupos_representados = models.CharField(max_length=200, null=True, blank=True)

    observacoes = models.CharField(max_length=1000, null=True, blank=True)

    #Publicacao
    publicacoes = models.ManyToManyField(to=Publicacao,
                                    related_name="contribuidores_coletivos",
                                    null=True,
                                    blank=True)

    #Referencia
    referencias = models.ManyToManyField(to=Referencia,
                                    related_name="entidades_citadas",
                                    null=True,
                                    blank=True)

    #Pessoa
    diretores = models.ManyToManyField(Pessoa, through="CargoDeDirecao")
    funcionarios_publicos = models.ManyToManyField(Pessoa,
                                        through="FuncionalismoPublico",
                                        related_name="funcionalismo_publico")
    empresarios_membros = models.ManyToManyField(Empresario,
                                        through="MembroEntidadeEmpresarial",
                                        related_name="membro_entidade")
    morador_associado = models.ManyToManyField(MoradorDeFavela,
                                        through="MoradorAssociado",
                                        related_name="associacao")


    def __unicode__(self):
        return self.nome


class Estatal(Entidade):
    class Meta:
        proxy = True


class EntidadeEmpresarial(Entidade):
    class Meta:
        proxy = True


class AssociacaoDeFavela(Entidade):
    class Meta:
        proxy = True


class CargoDeDirecao(models.Model):
    pessoa = models.ForeignKey(Pessoa)
    entidade = models.ForeignKey(Entidade)

    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)


class FuncionalismoPublico(models.Model):
    pessoa = models.ForeignKey(Pessoa)
    entidade = models.ForeignKey(Entidade)

    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)


class MembroEntidadeEmpresarial(models.Model):
    pessoa = models.ForeignKey(Empresario)
    entidade = models.ForeignKey(Entidade)

    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)



class MoradorAssociado(models.Model):
    pessoa = models.ForeignKey(MoradorDeFavela)
    entidade = models.ForeignKey(Entidade)

    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)


