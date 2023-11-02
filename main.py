from flask import Blueprint, render_template
APP_NAME = "example"
router = Blueprint(APP_NAME, __name__, static_folder="static", template_folder="templates")


@router.route('/')
def index():
    return render_template("index.html")
