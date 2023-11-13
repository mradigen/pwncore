from fastapi import FastAPI

from tortoise.contrib.fastapi import register_tortoise

import pwncore.docs as docs
import pwncore.routes as routes

app = FastAPI(
    title="Pwncore", openapi_tags=docs.tags_metadata, description=docs.description
)

app.include_router(routes.router)

register_tortoise(
    app,
    db_url="sqlite://:memory:",
    modules={"models": ["pwncore.db"]},
    generate_schemas=True,
    add_exception_handlers=True
)
