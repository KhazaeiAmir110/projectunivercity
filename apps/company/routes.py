from flask import Blueprint, render_template, request, redirect

from apps.company.models import Company
from apps.users.models import User

blueprint = Blueprint('company', __name__)


@blueprint.route('/', methods=("GET", "POST"))
def home():
    if request.method == "POST":
        company_slug = request.form.get('company_slug')
        if company_slug:
            return redirect('company.company_detail', company_slug)

    return render_template('company/page1.html',
                           companies=Company.objects.filter(is_active=1),
                           join_table=Company.objects.left_join(join_table=User,
                                                                join_condition='company.user_id=user.id')
                           )


@blueprint.route('/<company_slug>')
def company_detail(company_slug):
    return render_template('company/page2.html', company=Company.objects.get(slug=company_slug))
