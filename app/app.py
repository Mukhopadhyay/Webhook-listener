from api import router
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.utils import get_openapi

app = FastAPI()

app.include_router(router)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Python FastAPI Webhook Listener",
        version="1.0.0",
        description="A simple, asynchronous, state-less FastAPI boilerplate for a Webhook listener",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

# Adding mkdocs documentation route
try:
    app.mount(
        "/documentation",
        StaticFiles(directory="../documentation", html=True),
        name="documentation",
    )
except Exception as err:
    print("[FastAPI] Documentation not built!")
