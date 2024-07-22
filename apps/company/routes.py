from flask import Blueprint

blueprint = Blueprint('company', __name__)


@blueprint.route('/')
def get_list_companies():
    pass
