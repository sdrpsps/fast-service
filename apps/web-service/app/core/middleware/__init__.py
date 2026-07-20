import inspect

from fastapi import FastAPI

from app.core.middleware import process_time, response, cors

MIDDLEWARES = [process_time.MIDDLEWARE, cors.MIDDLEWARE, response.MIDDLEWARE]


def register_middleware(app: FastAPI) -> None:
    for callable_obj, kwargs in MIDDLEWARES:
        if inspect.isclass(callable_obj):
            app.add_middleware(callable_obj, **kwargs)
        else:
            app.middleware("http")(callable_obj)
