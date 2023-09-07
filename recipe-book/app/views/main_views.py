from flask import Blueprint, url_for, current_app, render_template
from werkzeug.utils import redirect

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/hello")
def hello_pybo():
    return "Hello, recipe!"


# 메인 페이지 라우팅 함수
@bp.route("/")
def index():
    current_app.logger.info("Logging level: INFO")

    return render_template("index.html")
