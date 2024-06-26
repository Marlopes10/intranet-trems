from intranet_trems import _
from intranet_trems import validadores
from plone.app.vocabularies.catalog import StaticCatalogVocabulary
from plone.dexterity.content import Container
from plone.schema.email import Email
from plone.supermodel import model
from plone.supermodel.model import Schema
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope import schema
from zope.interface import implementer

import re


class IPessoa(Schema):
    """Definição de uma pessoa no TRE-MS."""

    title = schema.TextLine(title=_("Nome Completo"), required=True)
    description = schema.Text(title=_("Biografia"), required=False)

    model.fieldset(
        "estrutura",
        _("Estrutura"),
        fields=[
            "cargo",
            "area",
        ],
    )
    cargo = schema.TextLine(title="Cargo", required=True)
    area = RelationList(
        title="Área",
        required=False,
        default=[],
        value_type=RelationChoice(
            title="Área", vocabulary=StaticCatalogVocabulary({"portal_type": ["Area"]})
        ),
    )

    #model.fieldset(
    #    "contato",
    #    _("Contato"),
    #    fields=[
    #        "email",
    #        "ramal",
    #    ],
    #)
    #email = Email(
    #    title=_("Email"),
    #    required=True,
    #    constraint=validadores.is_valid_email,
    #)
    #ramal = schema.TextLine(
    #    title=("Ramal"),
    #    required=True,
    #    constraint=validadores.is_valid_extension,
    #)


@implementer(IPessoa)
class Pessoa(Container):
    """Uma pessoa no TRE-MS."""
