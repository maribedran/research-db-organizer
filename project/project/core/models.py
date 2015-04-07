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


    def __unicode__(self):
        return self.nome


class Estatal(Entidade):

    pass

    # entidades relaiconadas


class EntidadeEmpresarial(Entidade):

    pass

    # poder publico


class AssociacaoDeFavela(Entidade):

    pass

    # outras associacoes
    # entidades


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

    #Entidade
    cargo_de_direcao = models.ManyToManyField(to=Entidade,
                                              related_name="diretores",
                                              null=True,
                                              blank=True)

    cargo_publico = models.ManyToManyField(to=Estatal,
                                           related_name="funcionarios_publicos",
                                           null=True,
                                           blank=True)

    def __unicode__(self):
        return self.nome


class MoradorDeFavela(Pessoa):
    associacao_de_favela = models.ManyToManyField(to=AssociacaoDeFavela,
                                                  related_name="assciados",
                                                  null=True,
                                                  blank=True)


class Empresario(Pessoa):
    entidade_empresarial = models.ManyToManyField(to=EntidadeEmpresarial,
                                                  related_name="membros",
                                                  null=True,
                                                  blank=True)

