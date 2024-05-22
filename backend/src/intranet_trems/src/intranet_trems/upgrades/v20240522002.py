from intranet_trems import logger
from plone import api


def alterar_permissionamento_estrutura(context):
    portal = api.portal.get()
    estutura = portal["estrutura"]
    permission_id = "intranet_trems: Add Area"
    roles = [
        "Contributor",
        "Editor",
        "Manager",
        "Site Administrator",
    ]
    estutura.manage_permission(permission_id, roles=roles)
    logger.info(f"Alterado permissionamento em {estutura}.")
