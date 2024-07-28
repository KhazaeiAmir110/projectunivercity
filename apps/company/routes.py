from flask import Blueprint, render_template

from apps.company.models import Company

blueprint = Blueprint('company', __name__)


@blueprint.route('/')
def home():

    return render_template('company/page1.html', companies=Company.objects.filter(is_active=1))