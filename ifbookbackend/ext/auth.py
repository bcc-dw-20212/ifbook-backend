from typing import NoReturn
from flask import Flask
from flask_jwt_extended import JWTManager


# Place here the extension's dependencies


# Place here your extension globals
jwt = JWTManager()


def init_app(app: Flask) -> NoReturn:
    """Init your global objects which do need to connect to flask object."""
    jwt.init_app(app)
