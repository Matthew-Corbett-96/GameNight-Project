from sys import stdout
from celery import Celery, Task
from flask import Flask
import logging


def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object(app.config["CELERY_CONFIG"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app


def logger_init_app(app: Flask) -> None:
    logging.basicConfig(
        stream=stdout, 
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
        )
