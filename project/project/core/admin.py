from django.contrib import admin
from models import (Publicacao,
                    Referencia,
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


@admin.register(MoradorDeFavela)
class MoradorDeFavelaAdmin(admin.ModelAdmin):
    pass


@admin.register(Empresario)
class EmpresarioAdmin(admin.ModelAdmin):
    pass


@admin.register(EntidadeEmpresarial)
class EntidadeEmpresarialAdmin(admin.ModelAdmin):
    pass


@admin.register(Estatal)
class EstatalAdmin(admin.ModelAdmin):
    pass


@admin.register(AssociacaoDeFavela)
class AssociacaoDeFavelaAdmin(admin.ModelAdmin):
    pass


