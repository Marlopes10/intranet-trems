from intranet_trems import _
from intranet_trems import validadores
from plone.dexterity.content import Container
from plone.schema.email import Email
from plone.supermodel import model
from plone.supermodel.model import Schema
from zope import schema
from zope.interface import implementer

import re


class IArea(Schema):
    """Definição de uma Área no TRE-MS."""

    # Informações básicas
    title = schema.TextLine(title="Nome da Área", required=True)
    description = schema.Text(title="Descrição", required=False)

    # Contato
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


@implementer(IArea)
class Area(Container):
    """Área no TRE-MS."""
