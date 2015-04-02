#coding: utf-8

from django.test import TestCase

from project.core.models import Pessoa, Entidade

class PersonTestCase(TestCase):

    def setUp(self):
        self.instance = Pessoa(nome='João das Neves', idade=30, naturalidade='Rio de Janeiro')
        self.instance.save()

    def test_instance_is_created_correctly(self):

        self.assertEqual('João das Neves', self.instance.nome)
        self.assertEqual(30, self.instance.idade)
        self.assertEqual('Rio de Janeiro', self.instance.naturalidade)
        self.assertFalse(self.instance.entidades.exists())

    def test_entity_is_correctly_saved(self):
        entidade = Entidade()
        entidade.save()
        self.instance.entidades.add(entidade)
        self.instance.save()
        self.assertEqual(entidade, self.instance.entidades.all()[0])
