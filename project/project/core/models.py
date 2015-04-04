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


    # moradia
    # empresas relacionadas
    # tipo ???

    def __unicode__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)


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
    diretores = models.ManyToManyField(to=Pessoa,
                                  related_name="cargo_de_direcao")

    def __unicode__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)


class Estatal(Entidade):

    funcionarios_publicos = models.ManyToManyField(to=Pessoa,
                                              related_name="cargo_publico")

    # entidades relaiconadas


class EntidadeEmpresarial(Entidade):

    membros = models.ManyToManyField(to=Pessoa,
                                related_name="entidade_empresarial")

    # poder publico


class AssociacaoDeFavela(Entidade):

    associados = models.ManyToManyField(to=Pessoa,
                                   related_name="membro_de_associacao")

    # outras associacoes
    # entidades


