from django.db import models

class Publicacao(models.Model):
    titulo = models.CharField(max_length=200)

    contribuidores_individuais = models.OneToMany(to=Pessoa)
    contribuidores_coletivos = models.OneToMany(to=Entidade)


class Referencia(models.Model):
    titulo = models.CharField(max_length=200)

    pessoas_citadas = models.OneToMany(to=Pessoa)
    entidades_citadas = models.OneToMany(to=Entidade)

class Entidade(models.Model):
    nome = models.CharField(max_length=200)
    fundacao = models.DateField()
    encerramento = models.DateField()
    fundador = models.CharField(max_length=200)
    objetivos = models.CharField(max_length=200)
    carater = models.CharField(max_length=200)
    financiamento = models.CharField(max_length=100)
    acoes = models.CharField(max_length=200)

    grupos_representados = models.CharField(max_length=200)

    observacoes = models.CharField(max_length=1000)

    #Publicacao
    publicacoes = models.ForeignKey(to=Publicacao,
                                    related_name="contribuidores_coletivos",
                                    null=True,
                                    blank=True)

    #Referencia
    referencias = models.ForeignKey(to=Referencia,
                                    related_name="entidades_citadas",
                                    null=True,
                                    blank=True)

    #Pessoa
    diretores = models.OneToMany(to=Pessoa)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)


class Estatal(Entidade):

    funcionarios_publicos = models.OneToMany(to=Pessoa)

    # entidades relaiconadas


class EntidadeEmpresarial(Entidade):

    membros = models.OneToMany(to=Pessoa)

    # poder publico


class AssociacaoDeFavela(Entidade):

    associados = models.OneToMany(to=Pessoa)

    # outras associacoes
    # entidades


class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    nascimento = models.DateField()
    morte = models.DateField()
    nacionalidade = models.CharField(max_length=30)
    formação = models.CharField(max_length=100)
    ocupação = models.CharField(max_length=100)

    observacoes = models.CharField(max_length=1000)

    #Publicacao
    publicacoes = models.ForeignKey(to=Publicacao,
                                    related_name="contribuidores_individuais",
                                    null=True,
                                    blank=True)

    #Referencia
    referencias = models.ForeignKey(to=Referencia,
                                    related_name="pessoas_citadas",
                                    null=True,
                                    blank=True)

    #Entidade
    cargo_de_direcao = models.ForeignKey(to=Entidade,
                                         related_name="diretores",
                                         null=True,
                                         blank=True)

    cargos_publicos = models.ForeignKey(to=Estatal,
                                        related_name="funcionarios_publicos",
                                        null=True,
                                        blank=True)

    entidades_empresariais = models.ForeignKey(to=EntidadeEmpresarial,
                                               related_name="membros",
                                               null=True,
                                               blank=True)

    associacoes = models.ForeignKey(to=Associacao,
                                    related_name="associados",
                                    null=True,
                                    blank=True)

    # moradia
    # empresas relacionadas
    # tipo ???

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)
