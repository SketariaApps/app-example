from flask import Blueprint, render_template
APP_NAME = "example"
router = Blueprint("fileshare", __name__, static_folder=f"apps/{APP_NAME}/static", template_folder=f"apps/{APP_NAME}/static")


@router.route('/')
def index():
    return render_template("index.html")
