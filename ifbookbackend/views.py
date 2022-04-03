from flask import render_template

from .models import User


def root():
    return render_template("index.html")
