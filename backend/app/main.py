from fastapi import FastAPI

from app.config import settings
from app.routes import router as api_router
from app.websocket import router as ws_router


def init_routers(app: FastAPI):
    app.include_router(api_router, prefix=settings.api_v1_str)
    app.include_router(ws_router, prefix=settings.api_v1_str)


app = FastAPI(title=settings.project_name, **settings.fastapi_info)
init_routers(app)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app=settings.app_string,
        host="0.0.0.0",
        port=8989,
        reload=settings.app_env == "dev",
    )
