from .api_registry import OpenApiRegistry
from src.settings import APP_NAME, DESCRIPTION, VERSION, DOMAIN

openapi = OpenApiRegistry()

if openapi.infos is None:
    infos = {
        "title": APP_NAME,
        "description": DESCRIPTION,
        "contact": {
            "name": f"{APP_NAME} API Support - A Valbou Project",
            "url": "http://www.valbou.fr/contact",
            "email": "contact@valbou.fr",
        },
        "license": {
            "name": "AGPL v3",
            "url": "https://www.gnu.org/licenses/agpl-3.0.en.html",
        },
        "version": VERSION,
    }
    openapi.register_infos(infos)

    openapi.register_server(DOMAIN, "Production API")

    api_error = {
        "type": "object",
        "properties": {
            "error": {
                "type": "string",
            },
            "status": {
                "type": "integer",
                "format": "int32",
            },
        },
    }
    openapi.register_schemas_components("APIError", api_error)

    api_security = {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "bearer",
    }
    openapi.register_security("bearerAuth", api_security)
