from fastapi.routing import APIRouter

from titanic_examp.web.api import docs, echo, monitoring, titanic

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(docs.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
# api_router.include_router(dummy.router, prefix="/dummy", tags=["dummy"])
api_router.include_router(titanic.router, prefix="/titanic", tags=["titanic"])
