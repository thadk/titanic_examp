import uvicorn

from titanic_examp.gunicorn_runner import GunicornApplication
from titanic_examp.settings import settings


def main() -> None:
    """Entrypoint of the application."""
    if settings.reload:
        uvicorn.run(
            "titanic_examp.web.application:get_app",
            workers=settings.workers_count,
            host=settings.host,
            port=settings.port,
            reload=settings.reload,
            log_level=settings.log_level.value.lower(),
            factory=True,
        )
    else:
        # We choose gunicorn only if reload
        # option is not used, because reload
        # feature doen't work with Uvicorn workers.
        GunicornApplication(
            "titanic_examp.web.application:get_app",
            host=settings.host,
            port=settings.port,
            workers=settings.workers_count,
            factory=True,
            accesslog="-",
            loglevel=settings.log_level.value.lower(),
            access_log_format='%r "-" %s "-" %Tf',  # noqa: WPS323
        ).run()


if __name__ == "__main__":
    main()
