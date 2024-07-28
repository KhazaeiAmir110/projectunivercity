from flask import Blueprint, render_template

blueprint = Blueprint('company', __name__)


@blueprint.route('/')
def home():
    return render_template('company/page1.html')